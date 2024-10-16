import { Links, Meta, Scripts, Outlet, } from "@remix-run/react";
import "./tailwind.css";
import Header from "./routes/layout_all/header";
import Footer from "./routes/layout_all/footer";

export default function App() {
  return (
    <html lang="ja">
        <Header />
      <body >
        <main className="p-6">
          <Outlet />
        </main>
        <Scripts />
      </body>
      <Footer />
    </html>
  );
}
