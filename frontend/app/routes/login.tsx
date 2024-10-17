import { Form, redirect, json } from "@remix-run/react"; // 追加
import { useActionData } from "@remix-run/react"; // 追加
import { getUserByEmail, verifyPassword } from "~/utils/auth"; // ユーザー認証のための関数を作成する
import { loginUser } from "~/utils/auth";
import { ActionFunction } from "@remix-run/node";

export default function Login() {
    const actionData = useActionData <{ error?: string }>(); // 追加

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

                {actionData?.error && <p>{actionData.error}</p>} {/* エラーメッセージ表示 */}
                <button type="submit">ログイン</button>
            </Form>
        </div>
    );
}


export const action: ActionFunction = async ({ request }) => {
    // 型が指定されたのでエラーが解消されます
    const formData = new URLSearchParams(await request.text());
    const email = formData.get("email");
    const password = formData.get("password");

    if (!email || !password) {
        return json({ error: "メールアドレスとパスワードは必須です。" }, { status: 400 });
    }
    const result = await loginUser(email, password);
}