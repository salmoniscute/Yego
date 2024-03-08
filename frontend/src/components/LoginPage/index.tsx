import React, { useState } from 'react';
import './index.scss';
import salmon from "./salmon.jpg";

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    if (username === 'admin' && password === 'password') {
      setLoggedIn(true);
    } else {
      alert('登入失敗，請檢查用戶名和密碼');
    }
  };

  return (
    <div className="container">
      <div className="card1">
          <h2>成功大學數位學習平台-登入</h2>
      </div>
      <div className="card2">
        <div className="left">
        <img src= {salmon} style={{ maxWidth: '80%', height: '80%' }}/>
        </div>
        <div className="right">
          {loggedIn ? (
            <h2>登入成功！歡迎回來，{username}！</h2>
          ) : (
            <div>
              <form>
                <input
                  type="text"
                  placeholder="用戶名"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)} />
                <input
                  type="password"
                  placeholder="密碼"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)} />
                <div className="remember-me">
                <input
                  type="checkbox"
                  id="rememberMe"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                />
                <p>記住我</p>
              
              </div>
                <button type="button" onClick={handleLogin}>
                  登入
                </button>
             
              </form>
            </div>
          )}
        </div>
        </div>
      </div>
  );
};

export default Login;