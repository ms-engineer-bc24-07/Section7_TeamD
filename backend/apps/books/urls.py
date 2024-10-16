from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookViewSet, 
    BookshelfViewSet, 
    ReadingNoteViewSet, 
    add_book_to_shelf, 
    update_shelf_status,
    UserViewSet,
    search_and_select_books,
    select_book,
    MyTokenObtainPairView  # 追加
)

# REST framework のルーターを使用してルーティングを設定
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'my-bookshelves', BookshelfViewSet)
router.register(r'reading-notes', ReadingNoteViewSet)
router.register(r'users', UserViewSet)  # UserViewSetのルーティングを追加

urlpatterns = [
    # Google Books API で書籍を検索してフロントに返すエンドポイント
    path('search-books/', search_and_select_books, name='search_and_select_books'),

    # ユーザーが選択した書籍をデータベースに保存するエンドポイント
    path('books/select/', select_book, name='select_book'),

    # 特定の書籍を本棚に追加するためのエンドポイント
    path('my-bookshelves/add/', add_book_to_shelf, name='add_book_to_shelf'), 

    # ステータスの部分更新
    path('my-bookshelves/<int:pk>/status/', update_shelf_status, name='update_shelf_status'),      

    # 認証関連のエンドポイントを追加
    path('auth/login/', MyTokenObtainPairView.as_view(), name='login'),  # ログイン
    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name='register'),  # ユーザー登録

    # 自動生成されたルーティング
    path('', include(router.urls)),
]
