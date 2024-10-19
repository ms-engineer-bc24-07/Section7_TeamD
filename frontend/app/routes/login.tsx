import { Form, redirect, json } from "@remix-run/react"; // 必要なコンポーネントをインポート
import { ActionFunction } from "@remix-run/node"; // ActionFunctionをインポート
import { loginUser } from "../utils/auth"; // 認証用の関数をインポート

// ActionFunctionを使用
export const action: ActionFunction = async ({ request }) => {
    const formData = new URLSearchParams(await request.text());
    const email = formData.get("email");
    const password = formData.get("password");

    if (!email || !password) {
        return json({ error: "メールアドレスとパスワードは必須です。" }, { status: 400 });
    }

    const result = await loginUser(email, password);
    if (result.error) {
        return json({ error: result.error }, { status: 401 });
    }

    return redirect("/"); // 認証成功時にリダイレクト
};

export default function Login() {
    return (
        <div className="login-container">
            <h1>ログイン</h1>
            <Form method="post" action="/login">
                <div>
                    <label htmlFor="email">メールアドレス</label>
                    <input type="email" name="email" id="email" required />
                </div>
                <div>
                    <label htmlFor="password">パスワード</label>
                    <input type="password" name="password" id="password" required />
                </div>
                <button type="submit">ログイン</button>
            </Form>
        </div>
    );
}
