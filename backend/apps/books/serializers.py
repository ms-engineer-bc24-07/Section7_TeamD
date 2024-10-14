from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Book, Bookshelf, ReadingNote
from django.contrib.auth import get_user_model

# Userシリアライザー（ユーザー情報のシリアライズ）
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # カスタムユーザーモデル
        fields = ['id', 'email', 'date_joined']  # 必要なフィールドを指定

# Bookシリアライザー
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Bookshelfシリアライザー
class BookshelfSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # ユーザー情報をネストして表示
    book = BookSerializer(read_only=True)  # 本の情報をネストして表示

    class Meta:
        model = Bookshelf
        fields = '__all__'

# ReadingNoteシリアライザー
class ReadingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingNote
        fields = '__all__'

# カスタムJWTシリアライザー (emailで認証)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 任意でカスタムクレームを追加できます
        token['email'] = user.email
        return token

    # emailで認証を行うためのカスタマイズ
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            try:
                # emailでユーザーを検索
                user = get_user_model().objects.get(email=email)
            except get_user_model().DoesNotExist:
                raise serializers.ValidationError('User with this email does not exist.')

            if not user.check_password(password):
                raise serializers.ValidationError('Incorrect password.')

            attrs['user'] = user
        else:
            raise serializers.ValidationError('Both "email" and "password" are required.')

        return super().validate(attrs)
