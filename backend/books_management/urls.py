from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import HttpResponse

# ホームページ用のビューを追加
def home(request):
    return HttpResponse("Welcome to the API!")

urlpatterns = [
    path('', home, name='home'),  # 空のパスに対してホームページビューを追加
    path('admin/', admin.site.urls),
    path('api/', include('apps.books.urls')),  # 'apps.books' のURLをインクルード
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # トークンリフレッシュエンドポイント
]
