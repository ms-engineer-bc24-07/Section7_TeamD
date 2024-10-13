from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 書籍管理アプリのルート
]
