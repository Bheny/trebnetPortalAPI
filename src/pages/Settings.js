import { Add, Save } from "@mui/icons-material";
import { useEffect, useRef, useState } from "react";
import CustomProfileModal from "../components/CustomProfileModal";
import { useAuth } from "../Contexts/AuthContext";
import { changePasswordSchema } from "../Schema/Schema";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

function Settings() {
  const { currentUser } = useAuth();
  const hiddenFileInputRef = useRef();
  const [profilePic, setProfilePic] = useState(currentUser.profile_pic);
  const [phone, setPhone] = useState("");
  const [preferences, setPreferences] = useState(currentUser.user_preferences);
  const [devLinks, setDevLinks] = useState(currentUser.user_dev_links);
  const [stacks, setStacks] = useState(currentUser.stack);
  const [preference, setPreference] = useState("");
  const [devLink, setDevLink] = useState({});
  const [devLinkTitle, setDevLinkTitle] = useState("");
  const [stack, setStack] = useState("");
  const [prefModalOpen, setPrefModalOpen] = useState(false);
  const [linkModalOpen, setLinkModalOpen] = useState(false);
  const [stackModalOpen, setStackModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const reader = new FileReader();

  const handleClick = () => {
    hiddenFileInputRef.current.click();
  };

  const handleFileUpload = (event) => {
    try {
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = (e) => {
        setProfilePic(e.target.result);
      };
    } catch (error) {
      setProfilePic(currentUser.profile_pic);
      console.log("Choose Image");
    }
  };

  const openPref = (e) => {
    e.preventDefault();
    console.log("modal open");

    setPrefModalOpen(true);
  };

  const openLink = (e) => {
    e.preventDefault();
    console.log("modal open");

    setLinkModalOpen(true);
  };

  const openStack = (e) => {
    e.preventDefault();
    console.log("modal open");

    setStackModalOpen(true);
  };

  const addToPref = (e, newPrefs) => {
    e.preventDefault();
    const allPrefs = [...preferences, newPrefs];
    console.log(allPrefs);
    setPreferences(allPrefs);
  };

  const addToLinks = (e, title, newLink) => {
    e.preventDefault();
    console.log("from add to links function");
    const allLinks = [...devLinks, { title: title, link: newLink }];
    console.log(devLinks);
    setDevLinks(allLinks);
  };

  const addToStack = (e, newStack) => {
    e.preventDefault();
    console.log("from add to stack function");
    const allStacks = [...stacks, newStack];
    console.log(allStacks);
    setStacks(allStacks);
  };

  const closeModals = (e) => {
    e.preventDefault();
    stackModalOpen && setStackModalOpen(false);

    linkModalOpen && setLinkModalOpen(false);

    prefModalOpen && setPrefModalOpen(false);

    console.log("modal close");
  };

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    resolver: yupResolver(changePasswordSchema),
  });

  const updateHandler = (data) => {
    const password = data.new_password;

    const updateData = {
      profilePic,
      phone,
      user_preferences: { ...preferences },
      stack: { ...stacks },
      user_dev_links: { ...devLinks },
      password,
    };
    // axios for the update function

    console.log(updateData);
    reset();
  };

  return (
    <div className="w-full h-screen overflow-hidden ">
      <header className="text-xl text-gray-700 font-bold my-5 pl-5 ">
        User Profile & Settings
      </header>

      <section className="flex place-content-center  w-full h-screen overflow-hidden overflow-y-scroll px-2 pt-5">
        <form className="grid gap-5 sm:w-[35rem] w-full pb-10">
          <div className="relative grid place-self-center ">
            <img
              src={profilePic}
              alt=""
              className="w-[100px] h-[100px] rounded-full ring-4 ring-blue-600 object-cover "
            />

            <label
              htmlFor="profilePicUpload"
              className="absolute -bottom-2 -right-2 cursor-pointer ring-2 ring-white rounded-full border-0 bg-blue-600 text-white p-2  hover:bg-blue-500"
              onClick={() => handleClick}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-5 w-5  "
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"
                />
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </label>
            <input
              id="profilePicUpload"
              type="file"
              accept="image/*"
              className="hidden"
              ref={hiddenFileInputRef}
              onChange={handleFileUpload}
            />
          </div>

          {/* form fields */}

          <div className="grid grid-cols-1 gap-10 mt-5">
            <div className="grid grid-cols-2 gap-5">
              <div>
                <label className="text-sm text-gray-700 font-light">
                  {" "}
                  First Name
                </label>
                <input
                  type="text"
                  value={currentUser.first_name}
                  disabled
                  className="profile-input"
                />
              </div>
              <div>
                <label className="text-sm text-gray-700 font-light">
                  {" "}
                  Last Name
                </label>
                <input
                  type="text"
                  value={currentUser.last_name}
                  disabled
                  className="profile-input"
                />
              </div>
            </div>
            <div>
              <label className="text-sm text-gray-700 font-light">Email</label>
              <input
                type="text"
                value={currentUser.email}
                className="profile-input"
                disabled
              />
            </div>
            <div>
              <label className="text-sm text-gray-700 font-light">
                {" "}
                Phone Number
              </label>
              <input
                type="tel"
                name="phone_number"
                accept=""
                className="profile-input"
                placeholder="+233 123 4567 89"
                onChange={(e) => {
                  setPhone(e.target.value);
                }}
              />
            </div>
            {/* user preferences */}
            <div className="grid gap-5">
              <label className="text-xl text-gray-700 font-bold">
                User Preferences
              </label>
              <ul className="spread ">
                {preferences.map((preference, index) => {
                  return (
                    <li key={index} className="spread-list bg-gray-500">
                      {preference}
                    </li>
                  );
                })}
                <button onClick={(e) => openPref(e)}>
                  <Add />
                </button>
              </ul>
              {/* additional stuff */}
              {prefModalOpen && (
                <CustomProfileModal
                  heading={"User Preference"}
                  inputPlaceholder={"add preference"}
                  handler={(e) => addToPref(e, preference)}
                  handleClose={closeModals}
                  changeHandler={(e) => {
                    setPreference(e.target.value);
                  }}
                />
              )}
            </div>
            {/* dev links */}
            <div className="grid gap-5">
              <label className="text-xl text-gray-700 font-bold">
                Developer Links
                <button onClick={(e) => openLink(e)}>
                  <Add />
                </button>
              </label>

              {devLinks.map((links, index) => {
                return (
                  <div key={index}>
                    <label> {links.title} </label>
                    <input
                      type="url"
                      defaultValue={links.link}
                      className="profile-input"
                    />
                  </div>
                );
              })}

              {/* additional stuff */}
              {linkModalOpen && (
                <CustomProfileModal
                  heading={"Dev Links"}
                  titlePlaceholder={"site name"}
                  inputPlaceholder={"https://www.mydevlink.com/id"}
                  handler={(e) => addToLinks(e, devLinkTitle, devLink)}
                  handleClose={closeModals}
                  titleChangeHandler={(e) => {
                    setDevLinkTitle(e.target.value);
                  }}
                  changeHandler={(e) => {
                    setDevLink(e.target.value);
                  }}
                />
              )}
            </div>
            {/* dev stack */}
            <div className="grid gap-5">
              <label className="text-xl text-gray-700 font-bold">
                Tech Stack
              </label>
              <ul className="spread">
                {stacks.map((stackItem, index) => {
                  return (
                    <li key={index} className="spread-list bg-sky-500">
                      {stackItem}
                    </li>
                  );
                })}
                <button onClick={(e) => openStack(e)}>
                  <Add />
                </button>
              </ul>

              {/* additional stuff */}
              {stackModalOpen && (
                <CustomProfileModal
                  heading={"Tech Stack"}
                  inputPlaceholder={"add tech stack"}
                  handler={(e) => addToStack(e, stack)}
                  handleClose={closeModals}
                  changeHandler={(e) => {
                    setStack(e.target.value);
                  }}
                />
              )}
            </div>
            {/* critical */}
            <div className=" border-rose-600 rounded h-fit border-2 relative">
              <header className="bg-rose-600 w-full text-center p-5 text-white absolute  text-xl font-bold">
                Critical
              </header>

              <div className="grid rounded px-6 py-6 gap-5 h-fit mt-14">
                <div>
                  <label className="text-sm text-gray-700 font-light">
                    Old Password
                  </label>
                  <input
                    type="password"
                    value={currentUser.password}
                    disabled
                    className="profile-input"
                  />
                </div>

                <div>
                  <label className="text-sm text-gray-700 font-light">
                    New Password
                  </label>
                  <input
                    {...register("new_password")}
                    type="password"
                    className="profile-input"
                    name="new_password"
                  />
                  <p className="error">{errors.new_password?.message}</p>
                </div>

                <div>
                  <label className="text-sm text-gray-700 font-light">
                    Confirm Password
                  </label>
                  <input
                    {...register("confirm_password")}
                    name="confirm_password"
                    type="password"
                    className="profile-input"
                  />
                  <p className="error">
                    {errors.confirm_password && "Passwords don't match"}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* submit button */}
          <button
            className="btn bg-green-500 text-center text-white fixed bottom-10 sm:top-5 sm:absolute sm:bottom-full rounded-full right-3 hover:bg-green-400 sm:px-10 sm:py-5 flex justify-center items-center gap-5 w-fit"
            onClick={handleSubmit(updateHandler)}
          >
            <span className="hidden  sm:block ">Save</span>
            <Save className="" />
          </button>
          <div className="w-full h-32"></div>
        </form>
      </section>
    </div>
  );
}

export default Settings;
