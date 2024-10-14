from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Userモデルマネージャー
class UserManager(BaseUserManager):
    def create_user(self, email, password=None): 
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email)) 
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None): 
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True  # 管理者はスタッフにも含まれる
        user.save(using=self._db)
        return user

# カスタムユーザーモデル
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # スタッフ権限
    is_superuser = models.BooleanField(default=False)  # スーパーユーザ権限

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # 権限のためのメソッド
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# Bookモデル
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    description = models.TextField(blank=True)
    cover_image = models.URLField(blank=True)
    page_count = models.IntegerField(blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True)

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
