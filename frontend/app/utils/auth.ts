//ユーザーの認証ロジックを作成
// utils/auth.ts
import { redirect } from "@remix-run/node";

// ダミーデータとしてユーザー情報を設定（実際にはデータベースから取得する）
const users = [
    { email: "test@example.com", password: "password123" }, // ハードコーディングは避けるべき
];

// メールアドレスからユーザーを取得
export const getUserByEmail = (email: string) => {
    return users.find(user => user.email === email);
};

// パスワードを検証
export const verifyPassword = (inputPassword: string, storedPassword: string) => {
    return inputPassword === storedPassword; // 実際のアプリケーションではハッシュ化されたパスワードを使用
};

// POSTリクエストを処理
export const loginUser = async (email: string, password: string) => {
    const user = getUserByEmail(email);

    if (!user || !verifyPassword(password, user.password)) {
        return { error: "無効なメールアドレスまたはパスワードです。" }; // エラーメッセージ
    }

    // 認証成功時、ホーム画面にリダイレクト
    return redirect("/");
};