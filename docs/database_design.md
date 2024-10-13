# データベース設計書

## 1. テーブル構造

### User（ユーザー）
| フィールド名   | 型          | オプション        | 説明                |
| -------------- | ----------- | ---------------- | ------------------- |
| id             | Integer     | PK, Auto         | ユーザーID（主キー） |
| email          | String(255) | Unique, Required | ユーザーのメールアドレス |
| password       | String(128) | Required         | ハッシュ化されたパスワード |
| date_joined    | DateTime    | Auto             | アカウント作成日      |

### Book（本）
| フィールド名   | 型          | オプション        | 説明                |
| -------------- | ----------- | ---------------- | ------------------- |
| id             | Integer     | PK, Auto         | 本のID（主キー）     |
| title          | String(255) | Required         | 本のタイトル         |
| author         | String(255) | Required         | 著者名              |
| isbn           | String(13)  | Unique, Required | ISBN番号            |
| published_date | Date        | Required         | 発行日              |
| description    | Text        |                  | 本の概要            |
| cover_image    | URL         |                  | カバー画像URL        |
| page_count     | Integer     |                  | ページ数            |
| categories     | String(255) |                  | カテゴリ            |

### Bookshelf（本棚）
| フィールド名   | 型          | オプション        | 説明                |
| -------------- | ----------- | ---------------- | ------------------- |
| id             | Integer     | PK, Auto         | 本棚のID（主キー）   |
| user_id        | Integer     | FK(User)         | ユーザーID           |
| book_id        | Integer     | FK(Book)         | 本のID               |
| status         | String(10)  | Default: 'to_read' | 本の状態（「読みたい」「読んでいる」「読み終わった」）|
| start_date     | Date        | Nullable         | 読書開始日          |
| end_date       | Date        | Nullable         | 読書終了日          |
| added_date     | Date        | Auto             | 本棚に追加した日     |
| updated_date   | Date        | Auto             | 状態が変更された日   |

### ReadingNote（読書メモ）
| フィールド名   | 型          | オプション        | 説明                |
| -------------- | ----------- | ---------------- | ------------------- |
| id             | Integer     | PK, Auto         | 読書メモID（主キー）|
| user_id        | Integer     | FK(User)         | ユーザーID           |
| book_id        | Integer     | FK(Book)         | 本のID               |
| content        | Text        | Required         | 読書メモの内容       |
| created_at     | DateTime    | Auto             | メモ作成日           |
| updated_at     | DateTime    | Auto             | メモ更新日           |

## 2. モデル間のリレーション

- **User と Bookshelf**: 1対多のリレーション（1人のユーザーは複数の本を本棚に追加できる）。
- **Bookshelf と Book**: 1対多のリレーション（本棚ごとに1つの本が登録され、その状態を管理する）。
- **User と ReadingNote**: 1対多のリレーション（1人のユーザーは複数の読書メモを持てる）。
- **Book と ReadingNote**: 1対多のリレーション（1冊の本に複数のメモが登録されるが、それぞれユーザーに紐づく）。
