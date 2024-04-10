import { ReactElement, useState } from "react";

import './index.scss';

import NotificationColumn from "components/NotificationColumn";

export default function ReportPage(): ReactElement {

  return <div id="notificationPage">
    <NotificationColumn seeAllBtn={false} />
    <div className="detail-panel">
      <h2>課程名稱</h2>
      <h1>訊息標題</h1>
      <h2>發布者發佈於ＯＯＯ時間</h2>
      <p>內文</p>
    </div>
  </div>
}