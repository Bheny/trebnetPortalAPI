import { Add, Cancel } from "@mui/icons-material";
import { useState } from "react";

function CustomProfileModal({
  heading,
  titlePlaceholder,
  inputPlaceholder,
  handler,
  handleClose,
  changeHandler,
  titleChangeHandler,
}) {
  return (
    // <div className={open ? "block" : "hidden"}>
    <div
      className={`w-screen h-screen bg-white absolute top-0 left-0 bg-opacity-50 content-center sm:place-content-center grid`}
    >
      <div className=" w-full h-fit rounded border-2 shadow bg-white z-10 opacity-100 py-10 relative">
        <header className="text-xl font-bold w-full bg-primary__blue text-center px-5 py-2 text-white absolute top-0 rounded-tl rounded-tr flex justify-between">
          {heading}
          <button onClick={(e) => handleClose(e)}>
            <Cancel />
          </button>
        </header>
        <main className="px-10 grid gap-5 mt-5 sm:w-[600px]">
          {titlePlaceholder && (
            <input
              type="text"
              placeholder={titlePlaceholder}
              className="profile-input"
              onChange={titleChangeHandler}
            />
          )}
          <input
            type="text"
            placeholder={inputPlaceholder}
            className="profile-input"
            onChange={changeHandler}
          />

          <button
            className="bg-green-500 text-white rounded py-2 "
            onClick={handler}
          >
            <Add />
          </button>
        </main>
      </div>
    </div>
    // </div>
  );
}

export default CustomProfileModal;
