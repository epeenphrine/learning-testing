import React, { useEffect, useState } from "react";
import { useForm } from "./useForm";

export default function ExampleUseState() {
  //const [{ email, password }, setValue] = useState({ email: "", password: "" }); another way of doing things might be useful ???
  //const [email, setEmail] = useState("");
  //const [password, setPassword] = useState("");
  const [values, handleChange] = useForm({
    email: "",
    password: "",
    firstName: "",
  });

  return (
    <React.Fragment>
      {/* <button onClick={() => setShowHello(!showHello)}>toggle</button>
      {showHello && <Hello />} */}
      <input type="email" name="email" onChange={handleChange} />
      <input type="password" name="password" id="" onChange={handleChange} />
      <input type="firstname" name="firstName" id="" onChange={handleChange} />
    </React.Fragment>
  );
}
