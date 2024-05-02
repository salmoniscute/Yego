import axios from "axios";
import { Notification } from "schemas/notification";

export async function get_all_notifications(uid: String) {
    let notifications = [];
    let url = `http://localhost:8080/api/notification/user/${uid}?`;
    try {
        const response = await axios.get(url);
        notifications = response.data;
        console.log(notifications);
    }
    catch {  
        console.log("hi");
    }

    return notifications;
}

export async function read_all_notifications(uid: String) {
    let notifications = [];
    let url = `http://localhost:8080/api/notification/user/${uid}/read`;
    try {
        const response = await axios.put(url);
        notifications = response.data;
        console.log(notifications);
    }
    catch {  
        console.log("hi");
    }

    return notifications;
}

export async function read_notification(uid: String, component_id: number) {
    let url = `http://localhost:8080/api/notification/particular/${uid}/${component_id}`;
    try {
        await axios.put(url, { have_read: true });
        return true;
    }
    catch {  
        console.log("have read fail");
        return false;
    }
}