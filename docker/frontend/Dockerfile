# ベースイメージの指定
FROM node:16

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係をインストール
COPY package.json package-lock.json ./
RUN npm install

# アプリのソースコードをコピー
COPY . .

# アプリのビルド
RUN npm run build

# アプリのポートを公開
EXPOSE 3000

# アプリを起動
CMD ["npm", "run", "dev"]
