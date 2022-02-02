import { Link } from "react-router-dom";
import loginImage from "../Assets/login.png";
import "./index.css";
function Index() {
  return (
    <div className="index-main">
      <div className="welcome">
        <h2 className="welcome-title">
          Welcome to the Axlr8 portal <br />( a.k.a Rebel's Corner )
        </h2>
        <img src={loginImage} alt="welcome-img" className="welcome-img" />
        <Link to="/register" className="btn-action btn-register">
          Create new account
        </Link>
        <Link to="/login" className="btn-action btn-login">
          Login
        </Link>
        <br />
      </div>
    </div>
  );
}

export default Index;
