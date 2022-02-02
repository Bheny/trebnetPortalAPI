import * as yup from "yup";

const registerSchema = yup.object().shape({
  first_name: yup.string().required(),
  last_name: yup.string().required(),
  username: yup.string().min(5).max(15).required(),
  email: yup.string().email().required(),
  password: yup.string().min(8).max(16).required(),
  confirm_password: yup.string().oneOf([yup.ref("password"), null]),
});

const loginSchema = yup.object().shape({
  email: yup.string().email().required(),
  password: yup.string().required(),
});

const changePasswordSchema = yup.object().shape({
  new_password: yup.string().notRequired(),
  confirm_password: yup.string().oneOf([yup.ref("new_password"), null]),
});

export { registerSchema, loginSchema, changePasswordSchema };
