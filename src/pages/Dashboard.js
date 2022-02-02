import { Route, Routes } from "react-router-dom";
import Home from "./Home";
import Events from "./Events";
import Credits from "./Credits";
import Announcements from "./Announcements";
import Ideas from "./Ideas";
import Jobs from "./Jobs";
import Settings from "./Settings";
import Layout from "../components/Layout/Layout";
import NoMatch from "../pages/NoMatch";

function Dashboard() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="events" element={<Events />} />
        <Route path="credits" element={<Credits />} />
        <Route path="announcements" element={<Announcements />} />
        <Route path="idea-bank" element={<Ideas />} />
        <Route path="job-board" element={<Jobs />} />
        <Route path="settings" element={<Settings />} />
        <Route path="*" element={<NoMatch />} />
      </Route>
    </Routes>
  );
}

export default Dashboard;
