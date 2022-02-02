// import "./LeaderBoard.css";
import BigWidget from "./Layout/BigWidget";
import Lead from "./Lead";
import { LeaderBoardData } from "../Assets/LeaderBoardData";

function LeaderBoard() {
  return (
    <>
      <BigWidget title="The leaderboard" name="leaderboard">
        <div className="h-[300px] flex flex-col items-center gap-5">
          {LeaderBoardData.map((lead, index) => {
            return (
              <Lead
                key={index}
                logo={lead.image}
                name={lead.name}
                position={lead.position}
              />
            );
          })}
        </div>
      </BigWidget>
    </>
  );
}

export default LeaderBoard;
