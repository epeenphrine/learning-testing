
import React, { useContext, } from 'react'
import { UserContext } from './UserContext'

export default function Index() {
    const {user, setUser} = useContext(UserContext)
    return (
        <div>
            <h2>
                About
            </h2>
            <p>{JSON.stringify(user)}</p>
        </div>
    )
}
