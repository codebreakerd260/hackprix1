// Conditionally render icons based on localStorage.getItem("role")

import { useEffect, useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";

const navItems = {
  user: [
    { name: "Home", path: "/home" },
    { name: "Report", path: "/report" },
    { name: "Emergency", path: "/emergency" },
    { name: "History", path: "/history" },
    { name: "Profile", path: "/profile" },
  ],
  admin: [
    { name: "Home", path: "/admin/home" },
    { name: "Report", path: "/admin/report" },
    { name: "Emergency", path: "/admin/emergency" },
    { name: "History", path: "/admin/history" },
    { name: "Profile", path: "/admin/profile" },
  ],
};

export default function BottomNavbar() {
  const [role, setRole] = useState("user"); // default fallback
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    const storedRole = localStorage.getItem("role");
    if (storedRole) setRole(storedRole);
  }, []);

  const activePath = location.pathname;

  return (
    <div className="fixed bottom-0 w-full bg-white border-t flex justify-around items-center h-14 shadow-md z-50">
      {navItems[role]?.map((item) => (
        <button
          key={item.name}
          onClick={() => navigate(item.path)}
          className={`flex flex-col items-center text-sm ${
            activePath === item.path
              ? "text-blue-600 font-bold"
              : "text-gray-500"
          }`}
        >
          <div className="text-lg">{iconFor(item.name)}</div>
          <span>{item.name}</span>
        </button>
      ))}
    </div>
  );
}

function iconFor(name) {
  const icons = {
    Home: "🏠",
    Report: "📝",
    Emergency: "🚨",
    History: "📜",
    Profile: "👤",
  };
  return icons[name] || "❔";
}
