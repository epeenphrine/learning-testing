import React, { useEffect, useState, useRef} from "react";
import { useForm } from "./useForm";

import Hello from "./Hello";
import { useFetch } from "./useFetch";


//useRef to call back

export default function ExampleUseState() {

  //const [{ email, password }, setValue] = useState({ email: "", password: "" }); another way of doing things might be useful ???
  //const [email, setEmail] = useState("");
  // const [password, setPassword] = useState("");

  const [values, handleChange] = useForm({
    email: "",
    password: "",
    firstName: "",
  });

  // const [showHello, setShowHello] = useState(true);
  // const [count, setCount] = useState(localStorage.getItem('count')); //get data from local storage

  const [count, setCount] = useState(() => 0); //get data from local storage
  const { data, loading } = useFetch(`http://numbersapi.com/${count}/trivia`);

  //ref to specific react components 

  const inputRef = useRef()
  const [showHello, setShowHello] = useState(true)

  return (
    <React.Fragment>
      <button onClick={() => setShowHello(!showHello)}>toggle</button>
      {showHello && <Hello />}
      <div>count : {count}</div>
      <button onClick={() => setCount((c) => c + 1)}>increment</button>
      <button onClick={() => setCount((c) => c - 1)}>decrement</button>
      <div>{loading ? "loading..." : data}</div>
      <input ref={inputRef} name="email" value={values.email} onChange={handleChange}/>
      <input type="email" name="email" onChange={handleChange} />
      <input type="password" name="password" id="" onChange={handleChange} />
      <input type="firstname" name="firstName" id="" onChange={handleChange} />
      <button onClick={() => {
        inputRef.current.focus()
      }}>focus</button>
    </React.Fragment>
  );
}
