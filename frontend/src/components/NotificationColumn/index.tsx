import { ReactElement, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import './index.scss';
import NotiContext from "../../views/NotificationPage/context";
import Notification from "components/Notification";


type propsType = Readonly<{

  seeAllBtn: boolean;

}>;

export default function NotificationColumn(props: propsType): ReactElement {
  const {
    seeAllBtn
  } = props;
  const ctx = useContext(NotiContext);

  useEffect(() => {
    ctx.get_list();
  }, [])
  const listRender = ctx.notifications.map((item) =>
      {if(item.have_read === false) return <Notification notification={item} key={item.id} />;
      return null;}
  );
  const haveReadListRender = ctx.notifications.map((item) =>
      {if(item.have_read === true) return <Notification notification={item} key={item.id} />;
      return null;}
  );

  return <div id="notificationColumn">
    <div className="header">
      <p>新通知</p>
      <button onClick={ctx.read_all}>全部標示為已讀</button>
      {props.seeAllBtn === true ? <Link to="/notification/1" className="seeall">查看全部</Link> : <></>}
    </div>
    <div>
      {listRender}
    </div>
    <p className="header">已讀的訊息</p>
    <div>
      {haveReadListRender}
    </div>
  </div>
}