import React, { useReducer, useState } from "react";

// take current state and action
// current state is the value and action is the function that gets called

function reducer(state, action) {
  switch (action.type) {
    case "add-todo":
      return {
        todos: [...state.todos, { text: action.text }],
      };
    case "toggle-todo":
      return {
        todos: state.todos.map((t, idx) =>
          idx === action.idx ? { ...t, completed: !t.completed } : t
        ),
      };
    case "toggle-reset":
      return {
        todos: [],
      };
    default:
      return state;
  }
}

export default function ExampleUseReducer() {
  const [{ todos }, dispatch] = useReducer(reducer, {
    todos: [],
  });
  const [text, setText] = useState("");
  return (
    <React.Fragment>
      <form
        action="
      "
        onSubmit={(e) => {
          e.preventDefault();
          dispatch({ type: "add-todo", text });
          setText("");
        }}
      >
        <input
          value={text}
          type="text"
          onChange={(e) => setText(e.target.value)}
        />
      </form>

      <button onClick={() => dispatch({ type: "toggle-reset" })}>
        reset button
      </button>
      {todos.map((t, idx) => (
        <div
          key={t.text}
          onClick={() => dispatch({ type: "toggle-todo", idx })}
          style={{
            textDecoration: t.completed ? "line-through" : "",
          }}
        >
          {t.text}
        </div>
      ))}
    </React.Fragment>
  );
}
