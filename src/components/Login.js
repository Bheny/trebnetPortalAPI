import { useState } from "react";
import { Link } from "react-router-dom";
import loginImage from "../Assets/AccessAccount.png";
import sideImg from "../Assets/check.jpg";
import { loginSchema } from "../Schema/Schema";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";

import Modal from "react-modal";
import CultureValidation from "./CultureValidation";

// const

Modal.setAppElement("#root");

function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    resolver: yupResolver(loginSchema),
  });

  const [modalIsOpen, setIsOpen] = useState(false);
  const [user, setUser] = useState([]);

  const openModal = () => {
    setIsOpen(true);
  };

  const openModalView = (data) => {
    // console.log({ ...data });
    // const { email, password } = data;
    setUser({ ...data });
    openModal();
    reset();
  };

  const closeModal = () => {
    setIsOpen(false);
  };

  return (
    <div className=" w-screen h-screen grid md:place-content-center bg-gray-200">
      <div className="grid  rounded-xl shadow-2xl  sm:w-[800px] md:place-content-center ">
        <form className="rounded  border-1 w-full sm:w-fit h-full bg-white grid grid-cols-3 gap-2 pl-5 shadow-2xl mt-40 md:mt-0 mr-5 md:mr-0">
          <div className="sm:col-span-2 col-span-3 sm:p-10  pt-10 pr-10 grid content-center md:pr-5 relative ">
            <img
              src={loginImage}
              alt="login-img"
              className="rounded-full  h-48 w-48 p-10 mt-[-2rem] place-self-center absolute top-[-95px] bg-white shadow-xl"
            />
            <div className="text-center font-bold text-gray-600 mb-4 mt-[-60px] md:mt-10">
              Login to access your account
            </div>
            <div className="all-form-control">
              <label htmlFor="email" className="label-base">
                Username
              </label>
              <input
                {...register("email")}
                name="email"
                type="text"
                placeholder="Enter your email"
                className="input-base sm:col-span-2 w-full sm:w-80 sm:ml-[-65px]"
              />
            </div>
            <p className="error">{errors.email?.message}</p>

            <div className="all-form-control">
              <label htmlFor="password" className="label-base">
                Password
              </label>
              <input
                {...register("password")}
                name="password"
                type="password"
                placeholder="Enter your password"
                className="input-base sm:col-span-2 w-full sm:w-80 sm:ml-[-65px]"
              />
            </div>
            <p className="error">{errors.password?.message}</p>

            <div className="md:grid md:grid-cols-3 mt-3 gap-2">
              <button
                className="btn bg-green-500 text-white text-lg mt-2 w-full md:col-span-2 hover:bg-green-600 h-14"
                onClick={handleSubmit(openModalView)}
              >
                Login
              </button>

              <div className="md:col-span-1 text-center grid content-center mb-5 p-4 md:p-0 md:mb-0">
                Don't have an account ?
                <br />
                <span className="text-blue-500">
                  <Link to="/register">create an account</Link>
                </span>
              </div>
            </div>
          </div>
          <img
            src={sideImg}
            className="sm:rounded-tr sm:rounded-br  relative hidden sm:block h-full sm:col-span-1 object-cover"
            alt="stuff "
          />
        </form>
      </div>

      {/* modal for Culture Verification */}
      <div>
        <Modal
          isOpen={modalIsOpen}
          onRequestClose={closeModal}
          contentLabel="Example Modal"
          shouldCloseOnEsc={false}
          shouldCloseOnOverlayClick={false}
        >
          <CultureValidation user={user} />
          <button
            onClick={closeModal}
            className="bg-rose-700 text-2xl text-white p-5 cursor-pointer absolute sm:top-[20px] left-0  w-full sm:w-fit "
          >
            close
          </button>
        </Modal>
      </div>
    </div>
  );
}

export default Login;
