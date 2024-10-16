from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Book, Bookshelf, ReadingNote  # 全てのモデルをインポート

# カスタムUserAdminの設定
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'date_joined', 'is_staff', 'is_active', 'is_superuser')  # is_superuserを追加
    list_filter = ('is_staff', 'is_active', 'is_superuser')  # is_superuserを追加
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),  # is_superuserを追加
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),  # is_superuserを追加
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Bookモデルの管理設定
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date')
    search_fields = ('title', 'author', 'isbn')

# Bookshelfモデルの管理設定
class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'start_date', 'end_date')
    list_filter = ('status',)
    search_fields = ('user__email', 'book__title')

# ReadingNoteモデルの管理設定
class ReadingNoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at', 'updated_at')
    search_fields = ('user__email', 'book__title')

# 管理画面への登録
admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)
admin.site.register(ReadingNote, ReadingNoteAdmin)
