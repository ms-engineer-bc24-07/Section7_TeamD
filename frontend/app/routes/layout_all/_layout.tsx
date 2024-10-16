// app/routes/_layout.tsx

import Header from "./header";
import Footer from "./footer";
import { Outlet } from "@remix-run/react";

export default function About() {
  return (
    <div>
      <Header />
      <Outlet />
      <Footer />
    </div>
  );
}
