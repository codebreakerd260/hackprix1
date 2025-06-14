import "./App.css";

import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  Outlet,
} from "react-router-dom";
import Login from "@/features/auth/Login";
import ReportForm from "@/features/report/ReportForm";
import UserEmergency from "@/features/emergency/UserEmergency";
import AdminEmergency from "@/features/emergency/AdminEmergency";
import AdminReportList from "@/features/admin/AdminReportList";
import HistoryScreen from "@/features/history/HistoryScreen";
import BottomNavbar from "@/components/BottomNavbar";

// Dummy components
const Home = () => <div>Home Screen</div>;
const Profile = () => <div>Profile Screen</div>;
const NotFound = () => <div>404 Not Found</div>;

// Layout for routes that include BottomNavbar
const UserLayout = () => (
  <>
    <Outlet />
    <BottomNavbar />
  </>
);

export default function App() {
  return (
    <Router>
      <Routes>
        {/* Routes without navbar */}
        <Route path="/" element={<Navigate to="/auth/login" />} />
        <Route path="/auth/login" element={<Login />} />
        <Route path="/admin/emergency" element={<AdminEmergency />} />
        <Route path="/admin/reports" element={<AdminReportList />} />

        {/* Routes with BottomNavbar */}
        <Route element={<UserLayout />}>
          <Route path="/home" element={<Home />} />
          <Route path="/report" element={<ReportForm />} />
          <Route path="/emergency" element={<UserEmergency />} />
          <Route path="/history" element={<HistoryScreen />} />
          <Route path="/profile" element={<Profile />} />
        </Route>

        {/* Fallback */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}
