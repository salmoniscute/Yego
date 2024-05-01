import React, { useState, useEffect, ReactNode } from "react";
import { get_all_notifications, read_all_notifications } from "api/notification";
import { NotificationRead } from "schemas/notification";

type propsType = Readonly<{
  children: ReactNode
}>;

type ContextType = {
  notifications: NotificationRead[];
  currNoti: NotificationRead;
  get_list: () => void;
  set_curr_noti: (curr: NotificationRead) => void;
  read_all: () => void;
};

const NotiContext = React.createContext<ContextType>({
  notifications: [],
  currNoti: {
    id: 0,
    publisher: "",
    course_name: "",
    release_time: "",
    title: "",
    content: "",
    have_read: false,
    icon_type: ""
  },
  get_list: () => {},
  set_curr_noti: (curr) => {},
  read_all: () => {}

});

export const NotiContextProvider = (props: propsType) => {
  const [notifications, setnotifications] = useState<Array<NotificationRead>>([]);
  const [currNoti, setcurrNoti] = useState<NotificationRead>({
    id: 0,
    publisher: "",
    course_name: "",
    release_time: "",
    title: "",
    content: "",
    have_read: false,
    icon_type: ""
  });

  const get_list = () => {
    get_all_notifications("C14096277").then(data => {
      setnotifications(data);
      setcurrNoti(data[0])
    });
  }

  const set_curr_noti = (curr: NotificationRead) => {
    setcurrNoti(curr);
  }

  const read_all = () => {
    read_all_notifications("C14096277").then(data => {
      setnotifications(data);
    });
  }

  return (
    <NotiContext.Provider
      value={{
        notifications: notifications,
        currNoti: currNoti,
        get_list: get_list,
        set_curr_noti: set_curr_noti,
        read_all: read_all
      }}
    >
      {props.children}
    </NotiContext.Provider>
  );
};

export default NotiContext;