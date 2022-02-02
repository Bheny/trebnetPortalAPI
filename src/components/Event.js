import { useState } from "react";

// import "./Event.css";
function Event({ logo, title, desc }) {
  const [showDetails, setShowDetails] = useState(false);
  return (
    <div className="shadow grid rounded place-content-center">
      <img src={logo} alt="event-pic" className="object-cover w-72 h-32" />

      <div className="pt-3 px-5 grid gap-0">
        <h3 className="text-lg font-bold text-gray-500">{title}</h3>
        <section className=" font-light text-sm ">
          <button
            className="text-sky-400 cursor-pointer"
            onClick={() => {
              setShowDetails(!showDetails);
            }}
          >
            details...
          </button>
          {showDetails && (
            <p className="w-60 h-32 overflow-hidden overflow-y-scroll mt-2">
              {desc}
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus
              voluptas modi maxime, ipsum ratione aut velit eaque iste
              consequatur accusamus laudantium eligendi eum, fugit, vero cumque
              nam error non quisquam quos repellendus sapiente odio expedita
              recusandae. Exercitationem sequi eaque sit laborum dolorem,
              repellat dolores nesciunt nihil, quisquam qui reiciendis maiores!
            </p>
          )}
        </section>
        <small className="font-semibold">Are you coming ?</small>
      </div>
      <div className="grid grid-cols-2 mb-4 mt-2 text-sm px-5 gap-5 ">
        <button className="w-full rounded  uppercase cursor-pointer shadow p-1 bg-primary__accept text-white ">
          Yes, I am
        </button>
        <button className="w-full rounded   uppercase cursor-pointer  shadow p-1 bg-primary__decline text-white">
          No, I Can't
        </button>
      </div>
    </div>
  );
}

export default Event;
