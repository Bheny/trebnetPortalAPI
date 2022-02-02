import { Link } from "react-router-dom";

import { Send } from "@mui/icons-material";
import Timeline from "react-time-line";
import "./Register.css";

function Register() {
  const events = [
    { text: "Email Submission" },
    { text: "Interview session with an Axlr8 general" },
    { text: "Account generation" },
    { text: "Account validation" },
    { text: "Full membership" },
  ];

  return (
    <div className="register">
      <div className="register-box">
        <div className="head">
          Interested in joining us ?
          <br />
          Enter Your Email to begin the process.
        </div>
        <div className="register-box-body">
          <form className="register-form">
            <div className="register-form-control">
              <input type="text" placeholder="mymail@mail.com" />
              <button className="register-btn">
                <Send />
              </button>
            </div>
          </form>
          <Timeline items={events} />
        </div>
        <span>
          Have an account? <Link to="/login">Sign In</Link>
        </span>
      </div>
    </div>
  );
}

export default Register;

// <li>Email Submission</li>
// <li>Interview session with Admin</li>
// <li>Account Generation and Validation</li>
// <li>Official Membership</li>
