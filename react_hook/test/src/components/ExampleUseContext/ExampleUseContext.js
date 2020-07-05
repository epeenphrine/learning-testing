import React, { Fragment, useState, useMemo } from "react";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import About from "./About";
import Index from "./Index";
import { UserContext } from "./UserContext";

//access data from anywhere no matter where you are in the component trees
export default function ExampleUseContext() {
  const [user, setUser] = useState(null);
  const value = useMemo(() => ({ user, setUser }), [user, setUser]);
  return (
    <Router>
      <Fragment>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about/">about</Link>
            </li>
          </ul>
        </nav>
        {/* can also pass in user, setUser if not using memo*/}
        <UserContext.Provider value={value}>
          <Route path="/" exact component={Index} />
          <Route path="/about/" exact component={About} />
        </UserContext.Provider>
      </Fragment>
    </Router>
  );
}
