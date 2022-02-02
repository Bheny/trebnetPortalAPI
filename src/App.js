import "./App.css";

import { Route, Routes } from "react-router-dom";
import Index from "./pages";
import Register from "./components/Register";
import Login from "./components/Login";
import MemberRegister from "./components/MemberRegister";
import "react-toastify/dist/ReactToastify.css";
import { AuthProvider } from "./Contexts/AuthContext";

import NoMatch from "./pages/NoMatch";
import PrivateRoute from "./PrivateRoute";
import Dashboard from "./pages/Dashboard";
import { ToastContainer } from "react-toastify";

function App() {
  return (
    <>
      <AuthProvider>
        <Routes>
          <Route exact path="/" element={<Index />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<MemberRegister />} />
          <Route path="/request-account" element={<Register />} />
          <Route
            path="dashboard/*"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />
          ;
          <Route path="*" element={<NoMatch />} />
        </Routes>
      </AuthProvider>
      <ToastContainer />
    </>
  );
}

export default App;
