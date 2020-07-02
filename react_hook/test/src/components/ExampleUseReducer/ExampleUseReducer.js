import React, { useReducer, useState} from "react";

// take current state and action
// current state is the value and action is the function that gets called

function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return state + 1;
    case "decrement":
      return state - 1;
    case "add-todo":
      return {
        
      }
    default:
      return state;
  }
}

export default function ExampleUseReducer() {
  const [{ todos }, dispatch] = useReducer(reducer, {
    todos: [],
  });
  const [text, setText] = useState("")
  return (
    <React.Fragment>
      <form
        action="
      "
      onSubmit={e => {
        e.preventDefault()
        dispatch({type: 'add-todo',text })
      }}
      >
        <input type="text" />
      </form>
    </React.Fragment>
  );
}
