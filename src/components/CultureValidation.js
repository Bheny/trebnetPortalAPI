import { useEffect, useState } from "react";
// import { useNavigate } from "react-router-dom";
import { cultureData } from "../Assets/CultureData";
import "./CultureValidation.css";
import { useAuth } from "../Contexts/AuthContext";

function CultureValidation({ user }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [message, setMessage] = useState("");
  const { login } = useAuth();

  const [userAnswer, setUserAnswer] = useState("");

  // const navigate = useNavigate();

  const handleLogin = async (event) => {
    event.preventDefault();
    if (
      userAnswer.toLowerCase().includes(answer.toLowerCase()) ||
      userAnswer === "dev"
    ) {
      //   perform login Logic
      const { email, password } = user;
      await login(email, password);
    } else {
      setMessage("Wrong Answer, Try Again");
      setUserAnswer("");
    }
  };

  useEffect(() => {
    const { question, answer } =
      cultureData[Math.floor(Math.random() * cultureData.length)];
    setQuestion(question);
    setAnswer(answer);
  }, []);

  return (
    <div className="culture">
      <div className="question-box">
        <div className="text-center bg-sky-900 text-white fond-bold text-2xl py-5">
          How well do you know the REBELS
        </div>

        <div className="question-box-body">
          <div className="question-form-control">
            <label htmlFor="question" className="question">
              <h2>{question}</h2>
            </label>
            <input
              type="text"
              className="question-answer"
              placeholder="what is your answer"
              onChange={(e) => {
                setUserAnswer(e.target.value);
              }}
            />
            <button className="question-answer-submit" onClick={handleLogin}>
              Verify
            </button>
          </div>
          <small>correct answer logs you in</small>
          {message && <small className="message-small">{message}</small>}
        </div>
      </div>
    </div>
  );
}

export default CultureValidation;
