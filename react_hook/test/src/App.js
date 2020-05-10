import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

import Testing from './components/Testing'
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

    const response = await fetch('')
      .then(res => res.json())
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
    </div>
  );
}

export default App;
