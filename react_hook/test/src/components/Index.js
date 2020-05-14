import React, { useContext } from 'react'

import { UserContext } from './UserContext'
import {login} from './login'

export default function Index() {
    const { user, setUser } = useContext(UserContext)
    return (
        <div>
            <h2>home</h2>
            <p>{JSON.stringify(user)}</p>
            <button onClick={async () => {
                const user = await login()
                setUser("changed!")
            }}
            >
                change value
                </button>
        </div>
    )
}
