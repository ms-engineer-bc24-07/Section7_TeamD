# ベースイメージとしてPythonを使用
FROM python:3.9

# 作業ディレクトリの作成
WORKDIR /app

# 依存関係をインストールするためにrequirements.txtをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
