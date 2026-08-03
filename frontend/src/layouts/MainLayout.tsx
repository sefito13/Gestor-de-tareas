import { Outlet } from "react-router-dom";
import Header from "../layouts/Header"
import Sidebar from "../layouts/Sidebar"

function MainLayout() {
    return (
        <div className="min-h-screen hg-gray-100">

            <Header />

            <div className="flex">

                <Sidebar />

                <main className="flex-1 p-8">

                    <Outlet />

                </main>

            </div>

        </div>
    )
}

export default MainLayout;