import { ReactElement, useState , useContext} from 'react';

import { login } from 'api/login';

import './index.scss';
import { useNavigate } from 'react-router-dom';

import userDataContext from "context/userData";

export default function LoginPage(): ReactElement {
  const [userName, setUserName] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  const userData = useContext(userDataContext);

  const handleLogin = async () => {
      const user = await login(userName, password);
      if (user) {
      } else {
          
      }
  };

  return (
    <div id="loginPage">
      <h2>登入YEGO</h2>
        <div className='rightBlock'>
          <p>帳號</p>
          <textarea
            placeholder="帳號與成功入口相同"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            rows={1}
          />
          <p>密碼</p>
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

          <div className='rightBlockButton' style={{backgroundColor: "#FFEA79",}} onClick={handleLogin}>
            登入
          </div>
          <p style={{textAlign: "center"}}>或</p>
          <div className='rightBlockButton' style={{backgroundColor: "#949494",color:"#F7F7F7"}}>
            訪客登入
          </div>
          <p style={{textAlign: "end" }}>登入說明</p>

        </div>
        

      </div>
      
    
  );
};
