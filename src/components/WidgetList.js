import Credit from "../components/Widgets/Credit";
import Project from "../components/Widgets/Project";
import Class from "../components/Widgets/Class";
import { useAuth } from "../Contexts/AuthContext";

function WidgetList() {
  const { currentUser } = useAuth();
  return (
    <div className="grid md:grid-cols-3 gap-5 w-full">
      <Project projects={currentUser.user_projects} />
      <Credit credit={currentUser.user_credit} />

      <Class
        userClass={currentUser.user_class}
        userRank={currentUser.user_rank}
      />
    </div>
  );
}

export default WidgetList;
