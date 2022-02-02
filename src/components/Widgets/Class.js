// import "./Class.css";
function Class({ userClass, userRank }) {
  return (
    <div className="widget grid-cols-2 text-gray-700 bg-white ">
      <div className="grid col-span-1 gap-6 ">
        <div className="text-sm md:text-2xl ">
          Class
          <br />
          <span className="text-lg md:text-xl font-bold">
            {userClass ? userClass : "No Class yet"}
          </span>
        </div>
      </div>

      <div className="grid gap-6 col-span-1 ml-2">
        <div className="text-sm md:text-2xl ">
          Rank <br />
          <span className="text-lg md:text-xl font-bold">
            {userRank ? userRank : "No rank available"}
          </span>
        </div>
      </div>
    </div>
  );
}

export default Class;
