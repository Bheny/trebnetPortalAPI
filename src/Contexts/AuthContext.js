import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ProfilePic from "../Assets/Bernard.jpeg";
const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  const testUser = {
    profile_pic: ProfilePic,
    first_name: "John",
    last_name: "Doe",
    email: "johndoe@gmail.com",
    password: "password123",
    role: 1,
    user_class: "Noob (A)",
    user_rank: "30th",
    user_credit: 550,
    user_projects: 1,
    user_dev_links: [
      {
        title: "Github",
        link: "https://example.com/",
      },
      {
        title: "LinkedIn",
        link: "https://example.com/",
      },
      {
        title: "Twitter",
        link: "https://example.com/",
      },
      {
        title: "Dev",
        link: "https://example.com/",
      },
      {
        title: "Medium",
        link: "https://example.com/",
      },
    ],
    user_field: [
      "Web Design",
      "Web Development",
      "UI/UX",
      "Artificial Intelligence",
    ],
    stack: [
      "React",
      "Node Js",
      "MySql",
      "C#",
      "Kotlin",
      "Flutter",
      "git",
      "Figma",
    ],
    user_preferences: [
      "Tech",
      "Web Development",
      "Hiking",
      "Tech Jobs",
      "Crypto",
    ],
  };

  const setUserStorage = (user) => {
    window.sessionStorage.setItem("user", JSON.stringify(user));
  };

  //   login function here
  const login = (email, password) => {
    // have login logic here but currently lets use email as testuser@gmail.com and password as password123
    // await axios
    //   .post("url", { email, password }, { timeout: 40000 })
    //   .then((res) => {
    //     setCurrentUser(res.data);
    // sessionStorage.setItem("user", res.data);
    //   })
    //   .catch((err) => {
    //     alert("couldn't login");
    //   });

    if (email === "testuser@gmail.com" && password === "password123") {
      setCurrentUser(testUser);
      setLoading(false);
      navigate("/dashboard");
      return true;
    }
  };

  useEffect(() => {
    setCurrentUser(JSON.parse(window.sessionStorage.getItem("user")));
  }, []);

  useEffect(() => {
    // setCurrentUser(currentUser);
    setUserStorage(currentUser);
    setLoading(false);
    console.log("mounted");
  }, [currentUser]);

  // logOut function here
  const logout = () => {
    setCurrentUser("");
    sessionStorage.removeItem("user");

    setLoading(false);
  };

  const value = {
    currentUser,
    login,
    logout,
  };
  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
