import { useEffect, useState, useRef } from "react";

export const useFetch = (url) => {

  const isCurrent = useRef(true);
  const hello = useRef(() => console.log('hello') )

  const [state, setState] = useState({ data: null, loading: true });

  useEffect(() => {
    return () => {
      //called when the componenet is going to unmount
      isCurrent.current = false;
    };
  }, []);

  useEffect(() => {
    setState({ data: null, loading: true });
    fetch(url)
      .then((res) => res.text())
      .then((text) => {
        console.log(text);
        setTimeout(() => {
          if (isCurrent.current) {
            setState({
              data: text,
              loading: false,
            });
          }
        }, 2000);
      });
  }, [url, setState]);
  return state;
};
