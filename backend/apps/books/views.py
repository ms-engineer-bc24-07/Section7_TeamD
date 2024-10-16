from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Book, Bookshelf, ReadingNote
from django.contrib.auth import get_user_model
from .serializers import BookSerializer, BookshelfSerializer, ReadingNoteSerializer, MyTokenObtainPairSerializer, UserSerializer
from django.conf import settings
import requests

# テスト用ビュー
def test_view(request):
    return HttpResponse("Test view is working")

# Book用のビューセット
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Bookshelf用のビューセット
class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer
    permission_classes = [IsAuthenticated]

# ReadingNote用のビューセット
class ReadingNoteViewSet(viewsets.ModelViewSet):
    queryset = ReadingNote.objects.all()
    serializer_class = ReadingNoteSerializer
    permission_classes = [IsAuthenticated]

# カスタムトークン取得ビュー (emailで認証)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# User用のビューセット
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]

# Google Books APIから本を検索して結果を返す
@api_view(['GET'])
@permission_classes([AllowAny])
def search_and_select_books(request):
    query = request.query_params.get('query', '')
    if not query:
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    api_key = settings.GOOGLE_BOOKS_API_KEY
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return Response({"error": "Failed to fetch data from Google Books API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = response.json()
    books_data = data.get("items", [])

    if not books_data:
        return Response({"message": "No books found for the given query"})

    books = [
        {
            "title": book.get("volumeInfo", {}).get("title", "No title"),
            "authors": book.get("volumeInfo", {}).get("authors", ["Unknown Author"]),
            "cover_image": book.get("volumeInfo", {}).get("imageLinks", {}).get("thumbnail", ""),
            "isbn": book.get("volumeInfo", {}).get("industryIdentifiers", [{}])[0].get("identifier", "No ISBN"),
            "published_date": book.get("volumeInfo", {}).get("publishedDate", "No date"),
            "description": book.get("volumeInfo", {}).get("description", "No description"),
            "page_count": book.get("volumeInfo", {}).get("pageCount", "No page count"),
            "categories": book.get("volumeInfo", {}).get("categories", ["No categories"]),
        }
        for book in books_data
    ]

    return Response(books)

# ユーザーが選択した書籍をDBに保存する
@api_view(['POST'])
def select_book(request):
    title = request.data.get('title')
    authors = request.data.get('authors', ['Unknown Author'])
    isbn = request.data.get('isbn')

    if not title or not isbn:
        return Response({"error": "Title and ISBN are required"}, status=status.HTTP_400_BAD_REQUEST)

    if len(isbn) > 13:
        isbn = isbn[:13]

    if Book.objects.filter(isbn=isbn).exists():
        return Response({"message": "This book already exists in the database."})

    categories = ', '.join(request.data.get('categories', []))

    book_data = {
        "title": title,
        "author": authors[0],
        "isbn": isbn,
        "published_date": request.data.get('published_date', None),
        "description": request.data.get('description', ''),
        "cover_image": request.data.get('cover_image', ''),
        "page_count": request.data.get('page_count', 0),
        "categories": categories
    }

    serializer = BookSerializer(data=book_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 本棚に新しい本を追加する
@api_view(['POST'])
def add_book_to_shelf(request):
    user = request.user
    book_id = request.data.get('book_id')

    if not book_id:
        return Response({"error": "Book ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    status_value = request.data.get('status', 'to_read')
    VALID_STATUS = ['to_read', 'reading', 'finished']
    if status_value not in VALID_STATUS:
        return Response({"error": "Invalid status value"}, status=status.HTTP_400_BAD_REQUEST)

    bookshelf, created = Bookshelf.objects.get_or_create(
        user=user,
        book=book,
        defaults={'status': status_value}
    )

    if created:
        return Response({"message": "Book added to your shelf"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": "This book is already in your shelf"}, status=status.HTTP_200_OK)

# 本棚のステータスを更新する
@api_view(['PATCH'])
def update_shelf_status(request, pk):
    try:
        bookshelf = Bookshelf.objects.get(pk=pk, user=request.user)
    except Bookshelf.DoesNotExist:
        return Response({"error": "Bookshelf entry not found"}, status=status.HTTP_404_NOT_FOUND)

    status_value = request.data.get('status')
    VALID_STATUS = ['to_read', 'reading', 'finished']
    if status_value not in VALID_STATUS:
        return Response({"error": "Invalid status value"}, status=status.HTTP_400_BAD_REQUEST)

    bookshelf.status = status_value
    bookshelf.save()

    serializer = BookshelfSerializer(bookshelf)
    return Response(serializer.data)
