import { ReactElement } from "react";

import './index.scss';
import { FaCircle } from "react-icons/fa";

export default function Notification(): ReactElement{
  return <div id="notification">
    <div className="left">
      <img></img>
      <div className="detail">
        <h2>課程名稱</h2>
        <h1>通知標題</h1>
        <p>幾分鐘前</p>
      </div>
    </div>
    <FaCircle className="circle-sign"/>
  </div>
}