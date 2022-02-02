import { useNavigate, Link, useLocation } from "react-router-dom";
import Profile from "./Profile";
// import "./Sidebar.css";
import { Links } from "./SidebarData";
import { useAuth } from "../Contexts/AuthContext";
import { useState } from "react";

function Sidebar() {
  const [isToggled, setIsToggled] = useState(false);

  const { logout } = useAuth();
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await logout();
      navigate("/login");
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <>
      {/* mobile nav */}
      <nav
        className={`bg-primary__blue h-screen w-14 flex flex-col gap-10 items-center md:hidden`}
      >
        <div className="text-white text-lg cursor-pointer grid mt-3 ">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className={`h-6 w-6 `}
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            onClick={() => {
              setIsToggled(true);
              console.log("navOpen");
            }}
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
        </div>
        <div className="">
          {Links.map((links, index) => (
            <CustomNavLink
              to={links.link}
              key={index}
              activeClassName="text-dark__blue bg-white hover:text-white"
              className=" text-white px-4 justify-start text-left hover:bg-dark__blue rounded-l-3xl flex content-center w-full py-2 "
            >
              <div className="grid place-items-center">{links.icon}</div>
            </CustomNavLink>
          ))}
        </div>
      </nav>
      {/* mobile nav end */}

      <div
        className={`bg-primary__blue h-screen sm:w-full pt-10  content-start pl-1 sm:pl-3 rounded-tr-lg rounded-br-lg shadow-lg absolute md:relative inset-y-0 left-0 transform md:translate-x-0 transition duration-400 ease-in-out ${
          isToggled ? "translate-x-0" : "-translate-x-full "
        }`}
      >
        {/* grid */}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className={`h-6 w-6 text-white sm:hidden  text-lg -mt-5 mb-4 cursor-pointer ${
            isToggled
              ? "absolute right-0 top-10 mr-5"
              : "grid place-self-center"
          }`}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          onClick={() => {
            isToggled ? setIsToggled(false) : setIsToggled(true);
            console.log("navOpen");
          }}
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M4 6h16M4 12h16M4 18h16"
          ></path>
        </svg>

        <div className={`mb-5`}>
          <Profile />
        </div>

        <nav className="mb-5">
          {Links.map((links, index) => (
            <CustomNavLink
              to={links.link}
              key={index}
              activeClassName="text-dark__blue bg-white hover:text-white"
              className=" text-white px-4 justify-start text-left hover:bg-dark__blue rounded-l-3xl flex content-center w-full py-2 "
            >
              <div className="grid place-items-center sm:selection:flex-[30%]">
                {links.icon}
              </div>
              <div
                className={`${
                  isToggled ? "block" : "hidden"
                } sm:block ml-2 sm:flex-[70%] `}
              >
                {links.title}
              </div>
            </CustomNavLink>
          ))}
        </nav>

        <button
          onClick={handleLogout}
          className={`btn hover:bg-rose-700 text-white bg-slate-400 w-fit sm:block `}
        >
          Log Out
        </button>
      </div>
    </>
  );
}

function CustomNavLink({
  to,
  className,
  inActiveClassName,
  activeClassName,
  ...rest
}) {
  const location = useLocation();
  const isActive = location.pathname === to;

  const allClassNames =
    className + (isActive ? `${activeClassName}` : `${inActiveClassName}`);
  return <Link to={to} {...rest} className={allClassNames} />;
}

export default Sidebar;
