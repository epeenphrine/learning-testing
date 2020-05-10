import React, { useReducer, useState } from 'react'


// for a component that may be involved with multiple function 
function reducer(state, action) {
    switch (action.type) {
        case "add-todo":
            return { todos: [...state.todos, { text: action.text, completed: false }] };
        case "toggle-todo":
            return {
                todos: state.todos.map((t, idx) => idx === action.idx ? { ...t, completed: !t.completed } : t)
            };
        default:
            return state;
    }
}


export default function Testing1() {
    const [{ todos }, dispatch] = useReducer(reducer, { todos: [] })
    const [text, setText] = useState()
    return (
        <div className="some-button-thing">
            <form onSubmit={
                e => {
                    e.preventDefault()
                    dispatch({ type: "add-todo", text })
                    setText("")
                }
            }>
                <input value={text} onChange={e => setText(e.target.value)} />
            </form>
            
            {todos.map((t, idx) => (
                <div
                    key={t.text}
                    onClick={() => dispatch({ type: "toggle-todo", idx })}
                    style={{
                        textDecoration: t.completed ? "line-through" : ""
                    }}
                >
                    {t.text}
                </div>
            ))}
        </div >
    )
}
