import React from 'react'


//handling props
export default function Testing(props) {
    return (
        <div>

            <div>
                {props.text}
            </div>
            <button onClick={() => props.setSomething({
                text: "from child"
            })}>setsomething button in child component</button>
        </div>


    )
}
