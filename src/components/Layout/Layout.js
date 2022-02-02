import { Outlet } from "react-router-dom";
import Sidebar from "../Sidebar";
import "./Layout.css";

function Layout() {
  return (
    <>
      <div className="flex max-h-screen relative bg-gray-100">
        <div className="z-10">
          <Sidebar />
        </div>

        <div className="flex-1 overflow-hidden overflow-y-scroll h-screen w-full">
          {" "}
          <Outlet />
        </div>
      </div>
    </>
  );
}

export default Layout;
