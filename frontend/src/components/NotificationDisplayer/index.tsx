import { ReactElement, useContext, useEffect, useState } from "react";
import NotiContext from "../../views/NotificationPage/context";
import './index.scss';

export default function NotificationDisplayer(): ReactElement {
  const ctx = useContext(NotiContext);
  const moment = require('moment-timezone');
  const [formattedDate, setformattedDate] = useState<String>("");

  useEffect(() => {
    const dateConvert = moment(ctx.currNoti.release_time);
    setformattedDate(dateConvert.format("YYYY-MM-DD hh:mm"));
  }, [ctx.currNoti]);

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
