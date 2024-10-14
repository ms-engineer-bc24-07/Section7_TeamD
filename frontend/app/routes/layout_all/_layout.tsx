// app/routes/_layout.tsx

import { Header } from "./header";
import { Footer } from "./footer";
import { Outlet } from "@remix-run/react";

export default function About() {
  return (
    <div>
      <Header />
      <h1>This is About Route</h1>
      <Outlet />
      <Footer />
    </div>
  );
}
