from django.apps import AppConfig
from django.db.backends.signals import connection_created

def activate_foreign_keys(sender, connection, **kwargs):
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.books'

    def ready(self):
        # データベース接続が確立されたときに外部キー制約を有効にする
        connection_created.connect(activate_foreign_keys)
