import axios from "axios";
import {
    CourseBulletinInfo
} from "../schemas/courseBulletin";

export async function getCourseBulletinList(course_id:string) :Promise<Array<CourseBulletinInfo>>{
    let url = "http://localhost:8080/api/course/bulletin?course_id="+course_id;
    try {
        const response = await axios.get(url,{
          });
        const result = response.data;
        const pinedResult = result.filter((data: CourseBulletinInfo) => data.pin_to_top);
        const notPinedResult = result.filter((data: CourseBulletinInfo) => !data.pin_to_top);
        pinedResult.sort((d1: CourseBulletinInfo, d2: CourseBulletinInfo) => d2.release_time - d1.release_time);
        notPinedResult.sort((d1: CourseBulletinInfo, d2: CourseBulletinInfo) => d2.release_time - d1.release_time);
        return pinedResult.concat(notPinedResult);
    }
    catch(error) {  
        //return ;
        throw error;
    }
}

export async function postCourseBulletin(uid:string,course_id:string,title:string,release_time:number,content:string,pin_to_top:boolean) :Promise<CourseBulletinInfo>{
    let url = "http://localhost:8080/api/course/bulletin?uid="+uid+"&course_id="+course_id;
    let courseBulletin ;

    // 目前先自己設定id
    try {
        const response = await axios.post(url,{
            "title": title,
            "id":"3",
            "release_time": "2021-09-01T00:00:00",
            "content": content,
            "pin_to_top": pin_to_top
          });
        courseBulletin = response.data;
    }
    catch(error) {  
        
    }

    return courseBulletin;

}
