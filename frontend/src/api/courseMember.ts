import { 
    OtherUser,
 } from "schemas/otherUser";
 import axios from "axios";

export async function getCourseMemberList(course_id: number) : Promise<Array<OtherUser>>{
    let url = "http://localhost:8080/api/selected_course/course/"+course_id;
    try {
        const response = await axios.get(url,{
          });
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}