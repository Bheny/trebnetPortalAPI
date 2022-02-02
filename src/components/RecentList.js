import BigWidget from "./Layout/BigWidget";
import Recent from "./Recent";
import "./RecentList.css";
function RecentList() {
  return (
    <div className="recent-list">
      <BigWidget title="Your Recent Activity" name="recents">
        <div className="recents bg-primary__white h-80 overflow-hidden overflow-y-scroll w-full">
          <Recent />
        </div>
      </BigWidget>
    </div>
  );
}

export default RecentList;
