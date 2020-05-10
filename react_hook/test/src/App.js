import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

import Testing from './components/Testing'

function App() {
  const [something, setSomething] = useState(
    {
      text: "hello this is working",
      status: true

    }
  )
  return (
    <div className="App">
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
