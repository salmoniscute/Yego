import { ReactElement } from "react";
import './index.scss';
import { NotiContextProvider } from "./context";
import NotificationColumn from "components/NotificationColumn";
import NotificationDisplayer from "components/NotificationDisplayer";
export default function NotificationPage(): ReactElement {
  return <div id="notificationPage">
    <NotiContextProvider>
      <NotificationColumn seeAllBtn={false}/>
      <NotificationDisplayer />
    </NotiContextProvider>
  </div>
}