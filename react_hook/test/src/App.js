import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';


import TestingUseEffect from './components/TestingUseEffect'
import Testing from './components/TestingProps'
import TestingReducer from './components/TestingReducer'
import Navbar from './components/Navbar'


function App() {
  const [something, setSomething] = useState(
    {
      text: "hello this is working",
      status: true

    }
  )
  const [TweetApi, setTweetApi] = useState(
    {
      data: []
    }
  )
  
  async function getAPI() {
    const response = await fetch(`${process.env.REACT_APP_NEETCODE_API}`)
      .then(res => res.json()).catch(() => console.log("can't get api"))
    setTweetApi({
      data: response
    })
    console.log(response)
  }
  useEffect(() => {
    getAPI()
  }, [])
  //console.log(TweetApi.data)
  return (
    <div className="App">
      <Navbar />
      <Testing
        text={something.text}
        status={something.status}
        setSomething={setSomething}
      />
      <button onClick={() => setSomething({
        text: "you clicked this in the parent component "
      })}>this is the button in parent component</button>
      <TestingReducer />
      <TestingUseEffect />

    </div>

  );
}

export default App;
