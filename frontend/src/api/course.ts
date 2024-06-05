import { Course } from "../schemas/course";
import axios from "axios";

export async function getUserCourseList(uid : string):Promise<Array<Course>>{
    let url = "/selected_course/user/" + uid;
    try {
        const response = await axios.get(url);
        return response.data;
    }
    catch {  
        
        //return ;
    }
    return [] ; 
}

export async function getCourse(id:number):Promise<Course>{
    let url = "/course/" + id;
    let course;
    try {
        const response = await axios.get(url,);
        course = response.data;
        return course;
    }
    catch {  
        
        //return ;
    }
    return course ; 

}