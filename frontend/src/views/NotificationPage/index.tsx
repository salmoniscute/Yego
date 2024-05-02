import { ReactElement, useEffect, useState } from "react";
import './index.scss';
import { NotiContextProvider } from "./context";
import NotificationColumn from "components/NotificationColumn";
import NotificationDisplayer from "components/NotificationDisplayer";
import { useParams } from "react-router-dom";
export default function NotificationPage(): ReactElement {
  const { id } = useParams<{ id?: string }>();
  const [idNumber, setidNumber] = useState<number>(0);

  useEffect(() => {
    if (id) {
      const numberId = parseInt(id);
      if (!isNaN(numberId)) {
        setidNumber(numberId);
      }
    }
  }, [id]);
  return <div id="notificationPage">
    <NotiContextProvider>
      <NotificationColumn seeAllBtn={false}/>
      <NotificationDisplayer id={idNumber}/>
    </NotiContextProvider>
  </div>
}