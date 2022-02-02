function BigWidget({ title, badge, children, name }) {
  return (
    <>
      <div
        className="w-full shadow-lg rounded pb-10 relative"
        style={{
          backgroundColor: name === "recents" ? "#EDF2F7" : "",
        }}
      >
        <div className="w-full bg-primary__blue text-white font-bold text-xl text-center py-3 px-3 rounded-tl rounded-tr">
          {title}{" "}
          {badge !== null && (
            <span className="absolute rounded-lg bg-white text-gray-600 font-bold right-0 mr-2 px-5 text-center">
              {badge}
            </span>
          )}
        </div>
        <div
          className="w-full"
          style={{
            overflowY: name === "jobs" ? "hidden" : "scroll",
          }}
        >
          <div className="items-center w-full">{children}</div>
        </div>
      </div>
    </>
  );
}

export default BigWidget;
