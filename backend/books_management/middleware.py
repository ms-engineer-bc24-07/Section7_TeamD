from django.utils.deprecation import MiddlewareMixin

class ForeignKeyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Middleware is executing")  # ミドルウェアが実行されているか確認
        from django.db import connection
        if connection.vendor == 'sqlite':
            print("Setting foreign keys ON for SQLite")  # SQLiteの判定が通ったか確認
            cursor = connection.cursor()
            cursor.execute('PRAGMA foreign_keys = ON;')
            print("Foreign keys are now ON")  # 外部キーの設定が実行されたか確認
