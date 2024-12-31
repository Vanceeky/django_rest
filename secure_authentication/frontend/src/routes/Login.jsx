import React from 'react'
import { useState } from 'react'
import { login } from '../endpoints/api'

const Login = () => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleLogin = () => {
        login(username, password)
    }
     
    return (
    

        <div>
            <h1>login</h1>
            <input onChange={(e) => setUsername(e.target.value)} value={username} type="text" placeholder="username"></input>
            <input onChange={(e) => setPassword(e.target.value)} value={password} type="password" placeholder="password"></input>
            <button onClick={handleLogin}>Login</button>
        </div>
        
    )
}

export default Login