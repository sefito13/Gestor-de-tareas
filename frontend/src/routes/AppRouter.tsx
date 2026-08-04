import { BrowserRouter, Routes, Route } from "react-router-dom"
import LoginPage from "../pages/LoginPage"
import DashboardPage from "../pages/DashboardPage"
import NotFoundPage from "../pages/NotFoundPage"
import MisTareasPage from "../pages/MisTareasPage"
import MainLayout from "../layouts/MainLayout"
import ProtectedRoute from "../components/ProtectRoute"

function AppRouter() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<LoginPage />} />

                <Route element={<ProtectedRoute />}>
                    <Route element={<MainLayout />}>
                        <Route path="dashboard" element={<DashboardPage />} />
                        <Route path="mis-tareas" element={<MisTareasPage />} />
                    </Route>
                </Route>
                
                <Route path="*" element={<NotFoundPage />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRouter;