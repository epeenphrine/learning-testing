import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

import Navbar from "./components/Navbar/Navbar";
import ExampleUseState from "./components/ExampleUseState/ExampleUseState";
import ExampleUseEffect from "./components/ExampleUseEffect/ExampleUseEffect";
import ExampleUseRef from "./components/ExampleUseRef/ExampleUseRef";
import ExampleUseReducer from "./components/ExampleUseReducer/ExampleUseReducer";
import ExampleUseContext from "./components/ExampleUseContext/ExampleUseContext";
// in vsc the command for commenting and uncommenting lines of codes is ctrl + /
function App() {
  return (
    <div className="App">
      <React.Fragment>
        <Navbar />
        {/* <ExampleUseState /> */}
        {/* <ExampleUseEffect /> */}
        {/* <ExampleUseRef /> */}
        {/* <ExampleUseReducer /> */}
        <ExampleUseContext />
      </React.Fragment>
    </div>
  );
}

export default App;
