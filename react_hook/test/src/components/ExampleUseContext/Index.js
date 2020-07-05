import React, { useContext } from "react";
import { UserContext } from "./UserContext";
import { login } from "./login";

export default function Index() {
  const { user, setUser } = useContext(UserContext);
  return (
    <React.Fragment>
      <h1>Home</h1>
      <pre>{JSON.stringify(user, null, 2)}</pre>
      {user ? (
        <button onClick={() => setUser(null)}>logout</button>
      ) : (
        <button
          onClick={async () => {
            const user = await login();
            setUser(user);
          }}
        >
          login
        </button>
      )}
    </React.Fragment>
  );
}
