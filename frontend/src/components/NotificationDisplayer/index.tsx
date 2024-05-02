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
    const dateConvert = moment(ctx.currNoti.release_time);
    setformattedDate(dateConvert.format("YYYY-MM-DD hh:mm"));
  }, [ctx.currNoti]);
  useEffect(() => {
    if (ctx.notifications?.length > 0) { 
      console.log(ctx.notifications[props.id - 1]);
      ctx.set_curr_noti(ctx.notifications[props.id - 1
      ]);
    }
  }, []); 
  useEffect(() => {
    if (ctx.notifications?.length > 0) { 
      console.log(ctx.notifications[props.id - 1]);
      ctx.set_curr_noti(ctx.notifications[props.id - 1]);
    }
  }, [props.id]); 

  return (
    <div id="notificationDisplayer">
      <div>
        <h2>{ctx.currNoti.course_name}</h2>
        <h1>{ctx.currNoti.title}</h1>
        <h2>{ctx.currNoti.publisher} 發佈於 {formattedDate}</h2>
        <p>{ctx.currNoti.content}</p>
      </div>
    </div>
  );
}
