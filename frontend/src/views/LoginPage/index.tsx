import { ReactElement, useState } from 'react';

import { login } from 'api/login';

import salmon from "./salmon.jpg";

import './index.scss';
import { useNavigate } from 'react-router-dom';

export default function LoginPage(): ReactElement {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  const setNavigate = useNavigate();

  const handleLogin = () => {
    login(username, password).then(() => {
      setNavigate("/");
    }).catch(() => {
      alert('登入失敗，請檢查用戶名和密碼');
    })
  };

  return (
    <div className="container">
      <div className="card1">
        <h2>成功大學數位學習平台-登入</h2>
      </div>
      <div className="card2">
        <div className="left">
        </div>
        <div className="right">
          <div>
            <form>
              <input
                type="text"
                placeholder="帳號"
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
                <p>記住帳號</p>

              </div>
              <button type="button" onClick={handleLogin}>
                登入
              </button>

            </form>
          </div>
        </div>
      </div>
    </div>
  );
};
