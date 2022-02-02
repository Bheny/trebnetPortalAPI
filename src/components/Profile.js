// import "./Profile.css";
import { useAuth } from "../Contexts/AuthContext";
function Profile() {
  const { currentUser } = useAuth();
  return (
    <div className="flex flex-col justify-center items-center text-white">
      <img
        src={currentUser.profile_pic}
        alt="profile-pic"
        className="w-[100px] h-[100px] rounded-full object-cover ring-2 ring-blue-600"
      />
      <div className="profile-name mt-2">
        {currentUser.first_name + " " + currentUser.last_name}
      </div>
      <div className="profile-mail">{currentUser.email}</div>
    </div>
  );
}

export default Profile;
