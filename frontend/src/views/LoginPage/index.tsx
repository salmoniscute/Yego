import {
  ReactElement,
  useState,
  SetStateAction,
  Dispatch
} from "react";

import {
  login,
  updateUserRole,
  refreshToken,
  updateUser
} from "api/login";

import "./index.scss";
import { useNavigate } from "react-router-dom";
import { RxCross2 } from "react-icons/rx";
import { User } from "schemas/user";

const YegoIcon = `${process.env.PUBLIC_URL}/assets/Yego.png`;
const YegogoIcon = `${process.env.PUBLIC_URL}/assets/Yegogo.png`;
const DagoIcon = `${process.env.PUBLIC_URL}/assets/Dago.png`;

type propsType = Readonly<{
  setRefreshToken: Dispatch<SetStateAction<string>>,
}>;

export default function LoginPage(props: propsType): ReactElement {
  // const {
  //   setRefreshToken,
  // } = props;
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [selectedCharacter, setSelectedCharacter] = useState("");
  // const [rememberMe, setRememberMe] = useState(false);
  const [showWork, setShowWork] = useState<boolean>(false);
  const [nowPage, setNowPage] = useState(1);
  const [selfIntro, setSelfIntro] = useState("");

  const [user, setUser] = useState<User>();

  const navigate = useNavigate();

  const handleLogin = async () => {
    const user = await login(userName, password);
    if (localStorage.getItem("access_token") && user) {
      setUser(user);
      if (user.introduction === "" || user.introduction === null || user.introduction === "<p><br></p>") {
        setShowWork(true);
      }
      else {
        navigate("/");
      }
    } else {

    }
  };

  const updateRole = async (role: string) => {
    if (user?.uid) {
      await updateUserRole(user?.uid, role);
      await refreshToken();
      navigate("/");
    }
  }

  const updateUserIntro = async () => {
    if (user?.uid) {
      const updatedUser = { ...user, introduction: selfIntro };
      await updateUser(updatedUser);
      await refreshToken();
      setNowPage(3);
    }
  }

  const characters = [
    { name: "Dago", icon: DagoIcon, intro: "每天在作業死線反覆橫跳，好幾次差點遲交，但意外的成績都不錯。" },
    { name: "Yegogo", icon: YegogoIcon, intro: "愛吃椰果，會對沒交作業的同學發射芒果。脖子上的領巾是老師送的。" },
    { name: "Yego", icon: YegoIcon, intro: "成績很好，小組報告裡面最閃亮的星，最近的煩惱是每天都想睡。" }
  ];
  const handleCharacterClick = (name: string) => {
    setSelectedCharacter(name);
  };

  return (
    <div id="loginPage">
      <h2>登入YEGO</h2>
      <div className="rightBlock">
        <p>帳號</p>
        <input
          type="text"
          className="loginInput"
          placeholder="帳號與成功入口相同"
          value={userName}
          onChange={(e) => setUserName(e.target.value)}
        />
        <p>密碼</p>
        <input
          type="password"
          className="loginInput"
          placeholder="密碼"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <div className="rightBlockMiddle">
          <div>
            <input type="checkbox" />
            <label >記住帳號</label>
          </div>
          <div>
            <p>忘記帳號/密碼</p>
          </div>
        </div>

        <div className="rightBlockButton" style={{ backgroundColor: "#FFEA79", }} onClick={handleLogin}>
          登入
        </div>
        <p style={{ textAlign: "center" }}>或</p>
        <div className="rightBlockButton" style={{ backgroundColor: "#949494", color: "#F7F7F7" }}>
          訪客登入
        </div>
        <p style={{ textAlign: "end" }}>登入說明</p>

      </div>
      <div className="selectedWork" data-show={showWork} >
        {nowPage === 1 && <div className="page1">
          <h2>初次登入 - 歡迎光臨！</h2>
          <img alt="yego icon" src={YegogoIcon} />
          <div className="intro">
            <p className="title">Hi! {user?.name} 我是 Yegogo!</p>
            <p>歡迎你加入 YEGO 成大數位學習平台！</p>
            <p>接下來的四年、五年、六年，你的學習生活都和我們很～有關係汪！</p>
            <p>忘了說，我叫Yegogo，最喜歡椰果奶茶。很高興見到你！</p>
            <p>不過⋯⋯我只知道你的名字，我還想更認識你！</p>
          </div>
          <button onClick={() => setNowPage(2)}><p>好啊！</p></button>

        </div>}
        {nowPage === 2 && <div className="page2">
          <h2>我想更認識你！</h2>
          <div className="intro">
            <img alt="yego icon" src={YegogoIcon} />
            <p>和我介紹一下你自己吧汪！</p>
          </div>
          <textarea
            placeholder="你從哪裡來？你的興趣是什麼？未來的夢想是？"
            value={selfIntro}
            onChange={(e) => setSelfIntro(e.target.value)}
            rows={1}
          >
          </textarea>
          <button onClick={() => updateUserIntro()}><p>我填好了！</p></button>
        </div>}
        {nowPage === 3 && <div className="page3">

          <h2>選擇角色</h2>
          <div>
            {characters.map(character => (
              <div
                key={character.name}
                className={`character ${selectedCharacter === character.name ? "selected" : ""}`}
                onClick={() => handleCharacterClick(character.name)}
              >
                <img src={character.icon} alt={character.name} />
                <div className="hoverEffect">
                  <p className="name">{character.name}</p>
                  <p className="intro">{character.intro}</p>
                </div>
              </div>
            ))}
          </div>
          <div className="button">
            {/* <button onClick={()=>{}}><p>從電腦裡選擇</p></button> */}
            <button onClick={() => { updateRole(selectedCharacter) }}><p>大功告成！</p></button>
          </div>
        </div>}
        <RxCross2 className="closeCross" onClick={() => setShowWork(false)} />
      </div>

    </div>


  );
};
