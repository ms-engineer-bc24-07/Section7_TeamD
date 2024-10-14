from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookshelfViewSet, ReadingNoteViewSet, add_book_to_shelf, UserViewSet

# REST framework のルーターを使用してルーティングを設定
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'my-bookshelves', BookshelfViewSet)
router.register(r'reading-notes', ReadingNoteViewSet)
router.register(r'users', UserViewSet)  # UserViewSetのルーティングを追加


urlpatterns = [
    # 自動生成されたルーティング
    path('', include(router.urls)),
    
    # 特定の書籍を本棚に追加するためのエンドポイント
    path('bookshelves/add/', add_book_to_shelf, name='add_book_to_shelf'),
]
