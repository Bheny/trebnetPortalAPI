import { useState } from "react";
import { Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import loginpic from "../Assets/loginPicture.jpg";
import { registerSchema } from "../Schema/Schema";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import Loader from "../Assets/Loader.svg";

function MemberRegister() {
  const [isLoading, setIsLoading] = useState(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    resolver: yupResolver(registerSchema),
  });

  const handleRegister = async (data) => {
    setIsLoading(true);
    const { first_name, last_name, username, email, password } = data;
    await axios
      .post(
        "http://192.168.1.166:8000/users/",
        {
          first_name,
          last_name,
          username,
          email,
          password,
        },
        { timeout: 10000 }
      )
      .then((res) => {
        toast.success("Account created succesfully");
        setIsLoading(false);
        // do whatever from here
      })
      .catch((err) => {
        console.log(err);
        console.log("User Registration failed");
        toast.error("User Registration failed");
        setIsLoading(false);
      });

    reset();
  };

  return (
    <div className=" w-screen h-screen grid md:place-content-center">
      <div className="grid bg-slate-200 rounded-xl shadow-2xl  sm:w-[800px]">
        <div className="md:hidden grid ">
          <header
            className="flex items-center justify-center h-48  bg-fixed bg-contain object-center bg-no-repeat
           custom-img md:hidden w-screen"
          >
            <a
              href="#signUp"
              className="p-5 text-2xl text-white bg-gray-500 bg-opacity-50 rounded-xl text-center font-bold"
            >
              Join Axlr8
              <br />
              <span className="italic">today</span>
            </a>
          </header>
        </div>
        <form
          id="signUp"
          action=""
          className=" rounded border-1 w-fit h-full bg-white grid md:grid-cols-3 gap-2 pl-0"
        >
          <img
            src={loginpic}
            alt="login-icon"
            className=" md:rounded-tl md:rounded-bl  relative hidden md:block h-full md:col-span-1 object-cover"
          />
          <div className="sm:col-span-2 sm:p-10  pt-10  w-fit grid content-center pl-5 relative">
            {isLoading && (
              <div className="absolute bg-white shadow-2xl w-full h-full opacity-90  z-10  grid place-self-center place-content-center">
                <img src={Loader} alt="" />
              </div>
            )}
            <span className="text-gray-700 font-bold text-center text-2xl">
              Sign Up
            </span>
            <div className="all-form-control">
              <label htmlFor="first_name" className="label-base">
                First name :
              </label>
              <input
                {...register("first_name")}
                type="text"
                name="first_name"
                placeholder="John"
                required
                className="input-base md:col-span-2 w-full"
                // ref={register("first_name")}
              />
            </div>
            <p className="error">{errors.first_name?.message}</p>
            <div className="all-form-control">
              <label htmlFor="last_name" className="label-base">
                Last name :{" "}
              </label>
              <input
                {...register("last_name")}
                type="text"
                name="last_name"
                placeholder="Doe"
                required
                className="input-base md:col-span-2"
                // ref={register("last_name")}
              />
            </div>
            <p className="error">{errors.last_name?.message}</p>

            <div className="all-form-control">
              <label htmlFor="username" className="label-base">
                Username :{" "}
              </label>
              <input
                {...register("username")}
                type="text"
                name="username"
                placeholder="@username"
                required
                className="input-base md:col-span-2"
                // ref={register("username")}
              />
            </div>
            <p className="error">{errors.username?.message}</p>

            <div className="all-form-control">
              <label htmlFor="email" className="label-base">
                Email :{" "}
              </label>
              <input
                {...register("email")}
                type="email"
                name="email"
                placeholder="johndoe@mail.com"
                required
                className="input-base md:col-span-2"
                // ref={register("email")}
              />
            </div>
            <p className="error">{errors.email?.message}</p>

            <div className="all-form-control">
              <label htmlFor="password" className="label-base">
                Password :{" "}
              </label>
              <input
                {...register("password")}
                type="password"
                name="password"
                placeholder="password"
                required
                className="input-base md:col-span-2"
                // ref={register("password")}
              />
            </div>
            <p className="error">{errors.password?.message}</p>

            <div className="all-form-control">
              <label htmlFor="confirm_password" className="label-base">
                Confirm Password :{" "}
              </label>
              <input
                {...register("confirm_password")}
                type="password"
                name="confirm_password"
                placeholder="confirm password"
                required
                className="input-base md:col-span-2"
                // ref={...register}
              />
            </div>
            <p className="error">
              {errors.confirm_password && "Passwords don't match"}
            </p>
            <aside className="mt-3">
              By clicking signup you have agreed to our terms and conditions
              <Link to="/terms" className="text-blue-500 ml-2">
                read T&C's
              </Link>
            </aside>
            <div className="md:grid md:grid-cols-3 mt-3 gap-2">
              <button
                className="btn bg-blue-800 text-white text-lg mt-2 w-full md:col-span-2 hover:bg-blue-500 h-14"
                type="submit"
                onClick={handleSubmit(handleRegister)}
              >
                Sign Up
              </button>

              <div className="md:col-span-1 text-center grid content-center mb-5 p-4 md:p-0 md:mb-0">
                Have an account?
                <br />
                <span className="text-blue-500">
                  <Link to="/login">Login</Link>
                </span>
              </div>
            </div>
          </div>
        </form>
      </div>
      <ToastContainer />
    </div>
  );
}

export default MemberRegister;
