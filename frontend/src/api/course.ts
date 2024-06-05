import { Course } from "../schemas/course";
import axios from "axios";

export async function getUserCourseList(uid : string):Promise<Array<Course>>{
    let url = "http://localhost:8080/api/selected_course/user/" + uid;
    try {
        const response = await axios.get(url,);
        return response.data;
    }
    catch {  
        
        //return ;
    }
    return [] ; 
}

export async function getCourse(id:number):Promise<Course|null>{
    let url = "http://localhost:8080/api/course/" + id;
    try {
        const response = await axios.get(url,);
        return response.data;
    }
    catch {  
        
        //return ;
    }
    return null ; 

}