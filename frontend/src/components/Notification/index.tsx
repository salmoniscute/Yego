import { ReactElement, useState, useEffect } from "react";

import { NotificationRead } from "schemas/notification";

import './index.scss';
import { FaCircle } from "react-icons/fa";

type propsType = Readonly<{
  notification: NotificationRead
}>;

export default function Notification(props: propsType): ReactElement{
  const {
    notification
  } = props;

  const [timeDifference, settimeDifference] = useState<number>(0);
  const [seconds, setseconds] = useState<number>(0);
  const [minutes, setminutes] = useState<number>(0);
  const [hours, sethours] = useState<number>(0);
  const [days, setdays] = useState<number>(0);
  const getTimeDifference = (time: string) => {
    let offlineTime = new Date(time).getTime();
    let currentTime = new Date().getTime();
    settimeDifference(currentTime - offlineTime);
    setseconds(Math.floor((timeDifference / 1000) % 60));
    setminutes(Math.floor((timeDifference / (1000 * 60)) % 60));
    sethours(Math.floor((timeDifference / (1000 * 60 * 60)) % 24));
    setdays(Math.floor(timeDifference / (1000 * 60 * 60 * 24)));
  }

  useEffect(() => {
    getTimeDifference(props.notification.release_time);
  }); 

  return <div id="notification">
    <div className="left">
      {props.notification.icon_type === ""}<img></img>
      <div className="detail">
        <h2>{props.notification.course_name}</h2>
        <h1>{props.notification.title}</h1>
        <p>{days}天{hours}小時{minutes}分鐘{seconds}秒前</p> 
      </div>
    </div>
    <FaCircle className="circle-sign"/>
  </div>
}