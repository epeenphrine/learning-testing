import React, {useEffect, useRef}  from "react";

export default function Hello() {
  const renders = useRef(0)
  console.log("hello renders", renders.current++)//add renders
  return <div>hello</div>
}
