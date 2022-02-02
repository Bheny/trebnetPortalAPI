import { Leaderboard } from "@mui/icons-material";
import { Badge } from "@mui/material";
// import "./Lead.css";
function Lead({ logo, position, name }) {
  return (
    <div className="grid grid-cols-3 items-center shadow rounded w-[90%] py-2 px-3">
      <img src={logo} alt="lead-pic" className="w-12 h-12 rounded-full" />

      <div className="w-full">
        <h4 className="text-gray-700 font-bold">{name}</h4>
      </div>

      <div className="flex justify-center ">
        <Badge badgeContent={position}>
          <Leaderboard />
        </Badge>
      </div>
    </div>
  );
}

export default Lead;
