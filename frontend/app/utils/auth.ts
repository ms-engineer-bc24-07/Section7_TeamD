// src/utils/auth.ts
export const loginUser = async (email: string, password: string) => {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/login/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }), // JSON形式でデータを送信
    });

    const result = await response.json();

    if (!response.ok) {
        return { error: result.detail || "無効なメールアドレスまたはパスワードです。" }; // エラーメッセージ
    }

    // 認証成功時、ユーザーデータまたはトークンを返す
    return result; // 必要に応じて適切なデータを返す
};
