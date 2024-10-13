from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Userモデル
class UserManager(BaseUserManager):
    def create_user(self, email, password=None): # 新規ユーザを作成する
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email)) # メールアドレス形式の標準化
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None): # 管理者権限保有ユーザの作成
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# Bookモデル
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    description = models.TextField()
    cover_image = models.URLField()
    page_count = models.IntegerField()
    categories = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Bookshelfモデル
class Bookshelf(models.Model):
    STATUS_CHOICES = [
        ('to_read', 'To Read'),
        ('reading', 'Reading'),
        ('finished', 'Finished')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_read')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.book.title}"

# ReadingNoteモデル
class ReadingNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note by {self.user.email} on {self.book.title}"
