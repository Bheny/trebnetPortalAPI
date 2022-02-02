// import "./Message.css";
import { Send } from "@mui/icons-material";
import { useState } from "react";
import { toast } from "react-toastify";

function Message({ logo, name, description }) {
  const [openReply, setOpenReply] = useState(false);
  const [message, setMessage] = useState("");

  const replyMessage = () => {
    toast.success(`message sent successfully to ${name}`);
    setOpenReply(false);
  };

  // console.log(message);

  return (
    <div className="sm:grid sm:grid-cols-5 w-[95%] shadow px-2 rounded py-3 items-center">
      <img
        src={logo}
        alt="logo"
        className="h-[50px] w-[50px] rounded-full shadow object-cover sm:place-self-center "
      />

      <div className="sm:col-span-2">
        <div className="text-left text-gray-700 font-extrabold">
          <h3>{name}</h3>
        </div>

        <div className="text-left text-gray-600 ">
          <p>{description}</p>
        </div>
      </div>
      <div className="text-sm font-extralight ">2 mins ago</div>

      {/* this is visible when open relpy is active */}

      {openReply && (
        <div className="grid grid-cols-7 bg-white w-full shadow rounded my-2 h-fit overflow-y-scroll col-span-5">
          <input
            type="text"
            className="w-full  focus:outline-2 focus:outline-green-400 px-3 py-2   col-span-6 border-0"
            placeholder="type your message here"
            multiple
            onChange={(e) => setMessage(e.target.value)}
          />
          <button className="text-green-400 w-full" onClick={replyMessage}>
            <Send fontSize="large" className="col-span-1 place-self-center" />
          </button>
        </div>
      )}

      {/* this is visible when open relpy is inactive */}
      {!openReply && (
        <button
          className=" text-white w-full bg-green-400 rounded shadow self-center"
          onClick={() => setOpenReply(!openReply)}
        >
          <Send fontSize="large" />
        </button>
      )}
    </div>
  );
}

export default Message;
