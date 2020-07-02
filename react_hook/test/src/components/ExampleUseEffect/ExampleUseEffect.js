import React, { useEffect, useState } from "react";
import { useForm } from "./useForm";

import Hello from "./Hello";
import { useFetch } from "./useFetch";

export default function ExampleUseState() {
  const [values, handleChange] = useForm({
    email: "",
    password: "",
    firstName: "",
  });


  // const [count, setCount] = useState(localStorage.getItem('count')); //get data from local storage
  const [count, setCount] = useState(0); //get data from local storage
  const { data, loading } = useFetch(`http://numbersapi.com/${count}/trivia`);

  //save to local storage 
  // useEffect(() => {
  //   localStorage.setItem('count', JSON.stringify(count))
  // }, [count])


  return (
    <React.Fragment>
      {/* <button onClick={() => setShowHello(!showHello)}>toggle</button>
      {showHello && <Hello />} */}
      <div>count : {count}</div>
      <button onClick={() => setCount((c) => c + 1)}>increment</button>
      <button onClick={() => setCount((c) => c - 1)}>decrement</button>
      <div>{loading ? "loading..." : data}</div>
      <input type="email" name="email" onChange={handleChange} />
      <input type="password" name="password" id="" onChange={handleChange} />
      <input type="firstname" name="firstName" id="" onChange={handleChange} />
    </React.Fragment>
  );
}
