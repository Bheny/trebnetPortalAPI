import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "./Contexts/AuthContext";
function PrivateRoute({ children }) {
  let auth = useAuth();
  let location = useLocation();
  console.log(auth);

  if (!auth.currentUser) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

export default PrivateRoute;
