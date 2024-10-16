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
| `/api/search-books/?query={query}` | GET          | Google Books APIで書籍を検索                          |
| `/api/books/select/`             | POST         | ユーザーが選択した書籍をデータベースに保存             |
| `/api/books/`                    | GET          | データベースに登録された全ての書籍を取得              |
| `/api/books/{id}/`               | GET          | データベースにある特定の書籍を取得                    |
| `/api/books/{id}/`               | PUT          | 書籍情報を更新                                        |
| `/api/books/{id}/`               | DELETE       | 書籍を削除                                            |

## Bookshelf リソース

| エンドポイント                    | HTTPメソッド | 説明                                                   |
| ---------------------------------- | ------------ | ------------------------------------------------------ |
| `/api/my-bookshelves/?user_id={user_id}` | GET          | 特定のユーザーが本棚に登録した書籍を取得               |
| `/api/my-bookshelves/add/`                | POST         | 本棚に新しい本を追加                                   |
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

