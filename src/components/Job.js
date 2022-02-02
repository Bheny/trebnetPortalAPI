// import "./Job.css";
import { Cancel, CancelOutlined, Check } from "@mui/icons-material";
import { useState } from "react";

import { toast } from "react-toastify";

function Job({ logo, title, description, jclass }) {
  const [isDeclined, setIsDeclined] = useState();
  const [isAccepted, setIsAccepted] = useState();

  // logic to send user id and job id to admin on those who accepted task and declined task

  return (
    <div className="grid md:grid-cols-5  gap-2 items-center rounded shadow px-2 py-3 w-full relative">
      <img
        src={logo}
        alt="logo"
        className="rounded-lg md:rounded-full md:w-20 md:h-20 shadow-lg place-self-center "
      />

      <div className=" sm:col-span-2 w-fit">
        <h3 className="text-gray-800 font-extrabold text-lg">
          {title} -
          <span className="text-gray-600 font-bold text-md">
            Class {jclass}
          </span>
        </h3>

        <section className="font-light">{description}</section>
        <div className="text-md text-gray-400 font-bold">2 mins ago</div>
      </div>

      <div className="flex justify-evenly sm:col-span-2">
        <button
          className="rounded-xl py-2 px-3 uppercase font-bold cursor-pointer tracking-wider shadow transition ease-in duration-500 bg-primary__accept hover:bg-sky-500 hover:text-white "
          onClick={() => {
            toast.success("Contact Admin for furthur Info");
            setIsAccepted(true);
          }}
        >
          Accept
        </button>
        <button
          className="rounded-xl py-2 px-3 uppercase font-bold cursor-pointer tracking-wider shadow transition ease-in duration-500 bg-primary__decline text-white hover:bg-rose-600"
          onClick={() => {
            toast.error("Task declined");
            setIsDeclined(true);
          }}
        >
          Decline
        </button>
      </div>

      {isAccepted && (
        <div className="absolute w-full h-full bg-primary__blue opacity-95 font-extrabold text-[100px] flex justify-center items-center">
          <Check
            className="bg-green-500 text-white rounded-full"
            fontSize="inherit"
          />
        </div>
      )}

      {isDeclined && (
        <div className="absolute w-full h-full bg-primary__blue opacity-95 font-extrabold text-[100px] flex justify-center items-center">
          <Cancel className=" text-rose-500 rounded-full" fontSize="inherit" />
        </div>
      )}
    </div>
  );
}

export default Job;
