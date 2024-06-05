import axios from "axios";
import {
    CourseBulletin
} from "../schemas/courseBulletin";

export async function getCourseBulletinList(course_id:number) :Promise<Array<CourseBulletin>>{
    let url = "/course/bulletin/particular_course/"+course_id;
    try {
        const response = await axios.get(url,{
          });
        const result = response.data;
        const pinedResult = result.filter((data: CourseBulletin) => data.pin_to_top);
        const notPinedResult = result.filter((data: CourseBulletin) => !data.pin_to_top);
        return pinedResult.concat(notPinedResult);
    }
    catch(error){
        return[];
    }
}

export async function postCourseBulletin(courseBulletin:CourseBulletin) :Promise<CourseBulletin>{
    let url = "/course/bulletin?uid="+courseBulletin.uid+"&course_id="+courseBulletin.course_id;
    try {
        const response = await axios.post(url,courseBulletin);
    }
    catch(error) {  
        
    }
    return courseBulletin;
    

}

export async function deleteCourseBulletin(id:number){
    let url = "/course/bulletin/"+id;
    try {
        const response = await axios.delete(url,{});
    }
    catch(error) {  
        
    }
}

export async function updateCourseBulletin(courseBulletin:CourseBulletin){
    let url = "/course/bulletin/"+courseBulletin.id;
    try {
        const response = await axios.put(url,courseBulletin);
    }
    catch(error) {  
        
    }
}

