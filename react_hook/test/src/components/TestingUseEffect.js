import React, { useEffect, useState } from 'react'



//use this for displaying searchbox??
export default function TestingUseEffect() {

    const [values, handleChange] = useState({ email: "", password: "" })

    useEffect(() => {
        console.log("render")
        return () => {
            console.log("unmountt")
        }
    }, [])

    return (
        <div>
            <input name="email" value={values.email} onChange={handleChange} />
            <input type="password" name="password" value={values.password} onChange={handleChange} />
        </div>
    )
}
