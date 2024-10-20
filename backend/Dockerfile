# ベースイメージとしてPythonを使用
FROM python:3.12

# 作業ディレクトリを作成して移動
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードをコンテナにコピー
COPY . .

# サーバーを起動するためのコマンドを指定
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
