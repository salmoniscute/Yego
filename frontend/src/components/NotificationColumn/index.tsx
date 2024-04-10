import { ReactElement } from "react";
import { Link } from "react-router-dom";

import './index.scss';

import Notification from "components/Notification";

type propsType = Readonly<{

  seeAllBtn: boolean;

}>;

export default function NotificationColumn(props: propsType): ReactElement {
  const {
    seeAllBtn
  } = props;
  return <div id="notificationColumn">
    <div className="header">
      <p>新通知</p>
      <button>全部標示為已讀</button>
      {props.seeAllBtn === true ? <Link to="/notification" className="seeall">查看全部</Link> : <></>}
    </div>
    <div>
      <Notification />
      <Notification />
      <Notification />
    </div>
    <p className="header">過去的通知</p>
    <div>
      <Notification />
    </div>
  </div>
}