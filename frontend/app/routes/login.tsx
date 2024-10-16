import { Form } from "@remix-run/react";

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