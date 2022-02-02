// import "./Project.css";
function Project({ projects }) {
  return (
    <div className="widget text-gray-700 bg-white ">
      <div className="text-2xl">Projects</div>
      <div className="font-bold text-xl">{projects ? projects : "Null"}</div>
    </div>
  );
}

export default Project;
