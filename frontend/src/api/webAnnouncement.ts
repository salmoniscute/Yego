// import axios from "axios";
import {
    WebAnnouncementContent,
    WebAnnouncementInfo
} from "../schemas/webAnnouncement";

export async function getWebAnnouncementList(): Promise<Array<WebAnnouncementInfo>> {
    const result = [
        {
            uid: "0",
            title: "公告標題-News 113/1/1(一)9:00~17:00 Moodle平臺暫停服務ddddddddddddddddddddddddddddddddd",
            release_time: 1703390840,
            pin_to_top: false,
        },
        {
            uid: "1",
            title: "公告標題-News 113/1/30(二)9:00~17:00 Moodle平臺暫停服務",
            release_time: 1706410840,
            pin_to_top: false,
        },
        {
            uid: "2",
            title: "公告標題-News 113/2/10(六)9:00~17:00 Moodle平臺暫停服務",
            release_time: 1707480840,
            pin_to_top: false,
        },
        {
            uid: "3",
            title: "公告標題-News 113/3/7(四)9:00~17:00 Moodle平臺暫停服務",
            release_time: 1709510840,
            pin_to_top: true,
        },
    ];
    // try {
    //     const response = await axios.get(...);
    //     ...
    // }
    // catch { return []; }

    const pinedResult = result.filter(data => data.pin_to_top);
    const notPinedResult = result.filter(data => !data.pin_to_top);

    pinedResult.sort((d1, d2) => d2.release_time - d1.release_time);
    notPinedResult.sort((d1, d2) => d2.release_time - d1.release_time);

    return pinedResult.concat(notPinedResult);
};

export async function getWebAnnouncementContent(data: WebAnnouncementInfo): Promise<WebAnnouncementContent | null> {
    return Object.assign(data, {
        content: "新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財",
        publisher: "admin"
    });

    // try {
    //     const response = await axios.get(...);
    //     ...
    // }
    // catch { return []; }
};
