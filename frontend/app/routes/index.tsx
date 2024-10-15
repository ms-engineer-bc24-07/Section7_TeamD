export const meta: MetaFunction = () => {
};

import Header from "./layout_all/header";
import Footer from "./layout_all/footer";
import { Outlet } from "@remix-run/react";

export default function Index() {
    return (
        <div>
            <Header />
            <Outlet />
            <Footer />
        </div>
    );
}