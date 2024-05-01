import { ReactElement, useState, useEffect } from "react";
import { Link } from "react-router-dom";

import { get_all_notification } from "api/notification";

import './index.scss';

import Notification from "components/Notification";
import { NotificationRead } from "schemas/notification";

type propsType = Readonly<{

  seeAllBtn: boolean;

}>;

export default function NotificationColumn(props: propsType): ReactElement {
  const {
    seeAllBtn
  } = props;

  const [notifications, setnotifications] = useState<Array<NotificationRead>>([]);

  useEffect(() => {
    get_all_notification("C14096277").then(data => {
      setnotifications(data);
    });
  }, [])
  const listRender = notifications.map((item) =>
    <Notification notification={item} />
  );

  return <div id="notificationColumn">
    <div className="header">
      <p>新通知</p>
      <button>全部標示為已讀</button>
      {props.seeAllBtn === true ? <Link to="/notification" className="seeall">查看全部</Link> : <></>}
    </div>
    <div>
      {listRender}
    </div>
    <p className="header">過去的通知</p>
    <div>
      {listRender}
    </div>
  </div>
}