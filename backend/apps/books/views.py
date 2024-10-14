from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Bookshelf, ReadingNote
from django.contrib.auth import get_user_model  # 追加
from .serializers import BookSerializer, BookshelfSerializer, ReadingNoteSerializer, MyTokenObtainPairSerializer, UserSerializer
from django.conf import settings
import requests
import logging

# ロギング設定
logger = logging.getLogger(__name__)

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
    queryset = get_user_model().objects.all()  # 全ユーザー取得
    serializer_class = UserSerializer  # UserSerializerを使用
        # create (POST) メソッドには AllowAny (認証不要) を設定
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]  # 新規ユーザー作成は認証不要
        else:
            self.permission_classes = [IsAuthenticated]  # それ以外は認証が必要
        return super().get_permissions()

# Google Books APIから本を取得して保存する関数
def fetch_and_save_books_from_google(query):
    api_key = settings.GOOGLE_BOOKS_API_KEY
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info(f"Google Books API response: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch data from Google Books API for query '{query}': {e}")
        return None

    if response.status_code == 200:
        data = response.json()
        books_data = data.get("items", [])
        
        if not books_data:
            logger.info(f"No books found for query '{query}'")
            return "No books found"

        for book_data in books_data:
            volume_info = book_data.get("volumeInfo", {})
            title = volume_info.get("title", "No title")
            authors = volume_info.get("authors", ["Unknown Author"])
            isbn_list = volume_info.get("industryIdentifiers", [])
            isbn = None
            for identifier in isbn_list:
                if identifier['type'] == 'ISBN_13':
                    isbn = identifier['identifier']
                    break
            if not isbn:
                isbn = "No ISBN"
            published_date = volume_info.get("publishedDate", "0000-00-00")

            # 日付がYYYY-MM形式の場合にYYYY-MM-DD形式に変換
            if len(published_date) == 7:  # YYYY-MM形式の場合
                published_date = f"{published_date}-01"

            description = volume_info.get("description", "")
            page_count = volume_info.get("pageCount", 0)
            categories = volume_info.get("categories", ["Unknown Category"])[0]
            cover_image = volume_info.get("imageLinks", {}).get("thumbnail", "")

            # Bookモデルにデータを保存
            try:
                Book.objects.update_or_create(
                    isbn=isbn,
                    defaults={
                        "title": title,
                        "author": authors[0],
                        "published_date": published_date,
                        "description": description,
                        "page_count": page_count,
                        "categories": categories,
                        "cover_image": cover_image,
                    }
                )
                logger.info(f"Book saved: {title} by {authors[0]}")
            except Exception as e:
                logger.error(f"Failed to save book '{title}' with ISBN '{isbn}': {e}")
        
        return "Books successfully fetched and saved"
    else:
        logger.error(f"Unexpected status code {response.status_code} from Google Books API for query '{query}'")
        return None

# Google Books APIから本を検索して保存するビュー
@api_view(['GET'])
def search_and_save_books(request):
    print("search_and_save_books was called")  # デバッグ用のログを追加
    query = request.query_params.get('query', '')

    if not query:
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    result = fetch_and_save_books_from_google(query)

    if result is None:
        return Response({"error": "Failed to fetch data from Google Books API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif result == "No books found":
        return Response({"message": "No books found for the given query"}, status=status.HTTP_200_OK)

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

# 本棚に書籍を追加するビュー
@api_view(['POST'])
def add_book_to_shelf(request):
    user = request.user
    isbn = request.data.get('isbn')

    if not isbn:
        return Response({"error": "ISBN is required"}, status=400)

    # ISBNでBookを検索。存在しない場合は404エラーを返す
    try:
        book = Book.objects.get(isbn=isbn)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    # ステータスのバリデーション
    status_value = request.data.get('status', 'to_read')
    VALID_STATUS = ['to_read', 'reading', 'finished']
    if status_value not in VALID_STATUS:
        return Response({"error": "Invalid status value"}, status=400)

    # Bookshelfに本を追加。既に存在していれば、新たに作成しない
    bookshelf, created = Bookshelf.objects.get_or_create(
        user=user,
        book=book,
        defaults={'status': status_value}
    )

    if created:
        return Response({"message": "Book added to your shelf"}, status=201)
    else:
        return Response({"message": "This book is already in your shelf"}, status=200)
