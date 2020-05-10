import React from 'react'

export default function Testing(props) {
    return (
        <div>

            <div>
                {props.text}
            </div>
            <button onClick={() => props.setSomething({
                text: "you clicked it man"
            })}>setsomething button in child component</button>
        </div>


    )
}
