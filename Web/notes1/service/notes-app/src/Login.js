import React, { useState } from 'react';

const Login = ({ onLogin }) => {
    const [username, setUsername] = useState('');

    const handleLogin = () => {
        if (username) {
            onLogin(username);
        }
    };

    return (
        <div style={{ padding: '20px', textAlign: 'center' }}>
            <h2>Login</h2>
            <input
                type="text"
                placeholder="Enter your username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
}

export default Login;