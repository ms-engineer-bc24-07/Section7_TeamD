from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from apps.books.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.books.urls')),  # 'apps.books' のURLをインクルード
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
