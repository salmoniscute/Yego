import { ReactElement, useContext, useEffect, useState } from "react";
import NotiContext from "../../views/NotificationPage/context";
import './index.scss';

type propsType = Readonly<{
  id: number
}>;

export default function NotificationDisplayer(props: propsType): ReactElement {
  const {
    id
  } = props;
  const ctx = useContext(NotiContext);
  const moment = require('moment-timezone');
  const [formattedDate, setformattedDate] = useState<String>("");

  useEffect(() => {
    if(ctx.currNoti.release_time != ""){
      const dateConvert = moment(ctx.currNoti.release_time);
      setformattedDate(dateConvert.format("YYYY-MM-DD hh:mm"));
    }
  }, [ctx.currNoti]);

  useEffect(() => {
    if (ctx.notifications.length) { 
      for(let i = 0; i < ctx.notifications.length; i++){
        if(ctx.notifications[i].id === props.id) ctx.set_curr_noti(ctx.notifications[i]);
      }
    }
  }, [props.id, ctx.notifications]); 

  return (
    <div id="notificationDisplayer">
      <div>
        <h2>{ctx.currNoti.course_name}</h2>
        <h1>{ctx.currNoti.title ? ctx.currNoti.title : "尚無通知"}</h1>
        <h2>{ctx.currNoti.publisher} {formattedDate ? "發佈於" : ""} {formattedDate ? formattedDate : ""}</h2>
        <div className="content"><p>{ctx.currNoti.content}</p></div>
      </div>
    </div>
  );
}
