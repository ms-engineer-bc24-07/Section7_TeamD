// app/routes/_layout.tsx
import { Outlet } from "@remix-run/react";

export default function Layout() {
  return (
    <div>
      <header>
        <nav>
          <h1>読書管理アプリケーション</h1>
          <ul>
            <li><a href="/">ホーム</a></li>
            <li><a href="/books">書籍一覧</a></li>
            <li><a href="/about">検索</a></li>
          </ul>
        </nav>
      </header>
      
      <main>
        <Outlet /> {/* 各ページの内容がここに表示される */}
      </main>
      
      <footer>
        <p>&copy; 2024 My App. All rights reserved.</p>
      </footer>
    </div>
  );
}
