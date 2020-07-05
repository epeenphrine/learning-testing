import React, { useContext } from "react";

import { UserContext } from "./UserContext";

export default function About() {
  const {user, setUser}= useContext(UserContext);
  return (
    <React.Fragment>
      <h2>About</h2>
      <pre>{JSON.stringify(user, null, 2)}</pre>
    </React.Fragment>
  );
}
