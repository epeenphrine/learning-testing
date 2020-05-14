import React, {useState, useMemo} from 'react'
import { BrowserRouter as Router, Route, Link } from "react-router-dom"

import Index from "./Index"
import About from "./About"


import { UserContext } from './UserContext'

export default function TestingUseContext() {
 
    const [user, setUser] = useState('hello this is from state')
    const providerValue = useMemo(() => ({user, setUser}, [user, setUser]))
    return (
        <div>
            <Router >
                <ul>
                    <li>
                        <Link to="/">
                            Home
                        </Link>
                    </li>
                    <li>
                        <Link to="/about/">
                            About
                        </Link>
                    </li>
                </ul>
                <UserContext.Provider value={providerValue}>
                    <Route path="/" component={Index} />
                    <Route path="/about/" component={About} />
                </UserContext.Provider>
            </Router>
        </div>
    )
}
