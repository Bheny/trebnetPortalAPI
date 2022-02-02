import WidgetList from "../components/WidgetList";

import "./Home.css";
import JobListContainer from "../components/JobListContainer";
import MessageList from "../components/MessageList";
import EventList from "../components/EventList";
import LeaderBoard from "../components/LeaderBoard";
import RecentList from "../components/RecentList";

import { useAuth } from "../Contexts/AuthContext";

function Home() {
  const { currentUser } = useAuth();
  return (
    <div className="dashboard px-3">
      <div className="text-xl text-gray-800 font-extrabold mt-5">
        Welcome {currentUser.first_name}
      </div>

      {/* dash bar */}
      <div className="bg-primary__blue text-white px-5 py-3 rounded shadow w-full">
        <span className="text-xl font-bold">Dashboard</span>
      </div>

      {/* widgets */}
      <div className="widget-list">
        <WidgetList />
      </div>

      <div className="main-content">
        <div className="content">
          {/* joblist */}
          <JobListContainer />
          {/* messageList */}
          <MessageList />
        </div>

        <div className="mini-sidebar">
          <EventList />
          <LeaderBoard />
        </div>
      </div>

      <div className="base-content">
        {/* recent activity */}
        <RecentList />
      </div>
    </div>
  );
}

export default Home;
