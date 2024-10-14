## **API設計書**

## User リソース

| エンドポイント              | HTTPメソッド | 説明                                     |
| --------------------------- | ------------ | ---------------------------------------- |
| `/api/users/`                | GET          | 全てのユーザーを取得                     |
| `/api/users/`                | POST         | 新しいユーザーを作成                     |
| `/api/users/{id}/`           | GET          | 特定のユーザーを取得                     |
| `/api/users/{id}/`           | PUT          | 特定のユーザー情報を更新                 |
| `/api/users/{id}/`           | DELETE       | 特定のユーザーを削除                     |

## Book リソース

| エンドポイント                  | HTTPメソッド | 説明                                                  |
| -------------------------------- | ------------ | ----------------------------------------------------- |
| `/api/books/search/?query={query}` | GET          | Google Books APIで書籍を検索                          |
| `/api/books/select/`             | POST         | ユーザーが選択した書籍をデータベースに保存             |
| `/api/books/`                    | GET          | データベースに登録された全ての書籍を取得              |
| `/api/books/{id}/`               | GET          | データベースにある特定の書籍を取得                    |
| `/api/books/{id}/`               | PUT          | 書籍情報を更新                                        |
| `/api/books/{id}/`               | DELETE       | 書籍を削除                                            |

## Bookshelf リソース

| エンドポイント                    | HTTPメソッド | 説明                                                   |
| ---------------------------------- | ------------ | ------------------------------------------------------ |
| `/api/my-bookshelves/?user_id={user_id}` | GET          | 特定のユーザーが本棚に登録した書籍を取得               |
| `/api/my-bookshelves/`                | POST         | 本棚に新しい本を追加                                   |
| `/api/my-bookshelves/{id}/`           | GET          | 特定の本棚エントリーを取得                             |
| `/api/my-bookshelves/{id}/`           | PUT          | 本棚エントリーを更新                                   |
| `/api/my-bookshelves/{id}/status`     | PATCH        | 本棚エントリーのステータスを部分更新                   |
| `/api/my-bookshelves/{id}/`           | DELETE       | 本棚エントリーを削除                                   |

## ReadingNote リソース

| エンドポイント               | HTTPメソッド | 説明                                     |
| ---------------------------- | ------------ | ---------------------------------------- |
| `/api/notes/?book_id={book_id}` | GET          | 特定の本に関連する読書メモを取得         |
| `/api/notes/`                 | POST         | 新しい読書メモを作成                     |
| `/api/notes/{id}/`            | GET          | 特定の読書メモを取得                     |
| `/api/notes/{id}/`            | PUT          | 読書メモを更新                           |
| `/api/notes/{id}/`            | PATCH        | 読書メモの一部を更新                     |
| `/api/notes/{id}/`            | DELETE       | 読書メモを削除                           |

## 認証関連エンドポイント

| エンドポイント           | HTTPメソッド | 説明                                     |
| ------------------------ | ------------ | ---------------------------------------- |
| `/api/auth/login/`        | POST         | ユーザーがログインする（トークン取得）   |
| `/api/auth/logout/`       | POST         | ログアウトしてセッショントークンを無効化 |
| `/api/auth/register/`     | POST         | 新しいユーザーを登録                     |

### **1. User リソース**

### 1.1. **GET /api/users/**

- **説明**: 全てのユーザーを取得。
- **詳細**: 管理者用に、システムに登録されているすべてのユーザー情報を取得します。

### 1.2. **POST /api/users/**

- **説明**: 新しいユーザーを作成（サインアップ）。
- **詳細**: 新規ユーザーを登録するために、メールアドレスとパスワードを受け取ってユーザーを作成します。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "email": "user@example.com",
      "password": "secure_password"
    }
    
    ```
    

### 1.3. **GET /api/users/{id}/**

- **説明**: 特定のユーザーを取得。
- **詳細**: 指定されたユーザーIDに基づいて、ユーザーの詳細情報を取得します。

### 1.4. **PUT /api/users/{id}/**

- **説明**: 特定のユーザー情報を更新。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "email": "new_email@example.com",
      "password": "new_password"
    }
    
    ```
    

### 1.5. **DELETE /api/users/{id}/**

- **説明**: 特定のユーザーを削除。
- **詳細**: 指定されたユーザーIDのユーザーをデータベースから削除します。

---

### **2. Book リソース**

### 2.1. **GET /api/books/search/?query=**

- **説明**: Google Books APIを使って書籍を検索。
- **詳細**: クエリパラメータで検索キーワードを指定して、Google Books APIから書籍情報を取得します。

### 2.2. **POST /api/books/import/**

- **説明**: Google Books APIから取得した書籍を自分のデータベースにインポート。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "title": "Harry Potter and the Sorcerer's Stone",
      "author": "J.K. Rowling",
      "isbn": "9780439708180",
      "published_date": "1997-09-01",
      "description": "A boy discovers he is a wizard...",
      "cover_image": "http://books.google.com/harrypotter.jpg",
      "page_count": 309,
      "categories": "Fantasy"
    }
    
    ```
    

### 2.3. **GET /api/books/**

- **説明**: 自分のデータベースに登録された全ての書籍を取得。

### 2.4. **GET /api/books/{id}/**

- **説明**: 自分のデータベースにある特定の書籍を取得。

### 2.5. **PUT /api/books/{id}/**

- **説明**: 書籍情報を更新。

### 2.6. **DELETE /api/books/{id}/**

- **説明**: 書籍を削除。

---

### **3. Bookshelf リソース**

### 3.1. **GET /api/bookshelves/?user_id={user_id}**

- **説明**: 特定のユーザーが本棚に登録した全ての書籍を取得。
- **詳細**: 特定のユーザーが本棚に登録した書籍とそのステータス（「読みたい」「読んでいる」「読み終わった」）を取得。

### 3.2. **POST /api/bookshelves/**

- **説明**: 本棚に新しい本を追加（書籍IDとユーザーIDを指定）。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "user_id": 1,
      "book_id": 1,
      "status": "to_read"
    }
    
    ```
    

### 3.3. **GET /api/bookshelves/{id}/**

- **説明**: 特定の本棚エントリーの詳細を取得。

### 3.4. **PUT /api/bookshelves/{id}/**

- **説明**: 本棚エントリーを更新（ステータスや読書開始日を変更）。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "status": "reading",
      "start_date": "2024-01-01"
    }
    
    ```
    

### 3.5. **PATCH /api/bookshelves/{id}/status**

- **説明**: 特定の本棚エントリーのステータスを部分的に更新。

### 3.6. **DELETE /api/bookshelves/{id}/**

- **説明**: 本棚エントリーを削除（ユーザーが本棚から本を削除）。

---

### **4. ReadingNote リソース**

### 4.1. **GET /api/notes/?book_id={book_id}**

- **説明**: 特定の本に関連する全ての読書メモを取得。

### 4.2. **POST /api/notes/**

- **説明**: 新しい読書メモを作成。
- **リクエスト例**:
    
    ```json
    json
    コードをコピーする
    {
      "user_id": 1,
      "book_id": 1,
      "content": "This book was fascinating!"
    }
    
    ```
    

### 4.3. **GET /api/notes/{id}/**

- **説明**: 特定の読書メモを取得。

### 4.4. **PUT /api/notes/{id}/**

- **説明**: 読書メモを更新。

### 4.5. **PATCH /api/notes/{id}/**

- **説明**: 読書メモを部分的に更新。

### 4.6. **DELETE /api/notes/{id}/**

- **説明**: 読書メモを削除。

---

### **5. 認証関連エンドポイント**

### 5.1. **POST /api/auth/login/**

- **説明**: ユーザーがログインする。トークンを取得。

### 5.2. **POST /api/auth/logout/**

- **説明**: ログアウトしてセッショントークンを無効にする。

### 5.3. **POST /api/auth/register/**

- **説明**: 新しいユーザーを登録。

---

### **API設計のポイント**

- **Google Books APIの連携**: 書籍検索（`GET /api/books/search`）とインポート（`POST /api/books/import`）がGoogle Books APIの活用を前提に設計されています。
- **BookshelfとReadingNoteのリレーション**: 設計書に記載されたリレーションに基づき、ユーザーが本棚に追加した書籍や、書籍に対する読書メモの管理が適切にAPIでカバーされています。
- **ステータス管理と部分更新**: BookshelfやReadingNoteのステータスや内容を部分的に更新するための`PATCH`エンドポイントも設置しています。