import { ReactElement, useState } from 'react';

import { login } from 'api/login';

import salmon from "./salmon.jpg";

import './index.scss';
import { useNavigate } from 'react-router-dom';

export default function LoginPage(): ReactElement {
  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  return (
    <div id="loginPage">
      <h2>成功大學數位學習平臺-登入</h2>
      <div className='block'>
        <div className='leftBlock'>
        </div>
        <div className='rightBlock'>
          <textarea
            placeholder="帳號"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            rows={1}
          />
          <textarea
            placeholder="密碼"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            rows={1}
          />

          <div className='rightBlockMiddle'>
            <div>
              <input type="checkbox"/>
              <label >記住帳號</label>
            </div>
            <div>
              <p>忘記帳號/密碼</p>
            </div>
          </div>

          <div className='rightBlockButton'>
            登入
          </div>
          <p style={{textAlign: "center"}}>或</p>
          <div className='rightBlockButton'>
            訪客登入
          </div>
          <p style={{textAlign: "end"}}>登入說明</p>

        </div>
        

      </div>
      
    </div>
  );
};
