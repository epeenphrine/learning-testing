import React, { useEffect } from "react";

export default function Hello() {
  useEffect(() => {
    console.log("render");
    return () => {
      console.log("unmount");
    };
  }, []);
  return (
    <React.Fragment>
      <h1>hello</h1>
    </React.Fragment>
  );
}
