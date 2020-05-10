import React, { useState } from 'react'

export default function Test(props) {
    const [count, setCount] = useState(0)
    return (
        <div>
            <p>
                {count}
            </p>
            <button onClick={() => setCount(count+1)}>
                click me
            </button>
            <p>
                {props.todo.text}
            </p>
            <p>
                {String(props.todo.isCompleeted)}
            </p>
        </div>
    )
}
