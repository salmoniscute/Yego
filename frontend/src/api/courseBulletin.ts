
import {
    CourseBulletinInfo
} from "../schemas/courseBulletin";

export async function getCourseBulletinList() :Promise<Array<CourseBulletinInfo>>{
    const result = [
        {
            uid: "0",
            course_id : "0",
            title: "老師今天身體不適，所以今天不上課。",
            release_time: 1703390840,
            pin_to_top: false,
            content: "hello",
            publisher: "張老師",

        },
        {
            uid: "0",
            course_id : "0",
            title: "老師今天身體不適，所以今天不上課。",
            release_time: 1703390840,
            pin_to_top: false,
            content: "hello",
            publisher: "張老師",

        },
        {
            uid: "0",
            course_id : "0",
            title: "老師今天身體不適，所以今天不上課。",
            release_time: 1703390840,
            pin_to_top: false,
            content: "hello",
            publisher: "張老師",

        }
    ];
    const pinedResult = result.filter(data => data.pin_to_top);
    const notPinedResult = result.filter(data => !data.pin_to_top);
    pinedResult.sort((d1, d2) => d2.release_time - d1.release_time);
    notPinedResult.sort((d1, d2) => d2.release_time - d1.release_time);
    return pinedResult.concat(notPinedResult);
}