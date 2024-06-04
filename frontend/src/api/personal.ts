import axios from "axios";
import {
    User
} from "../schemas/user";

export async function getPersonal(uid:string) : Promise <User>{
    let url = "http://localhost:8080/api/user/"+uid;
    let personal;
    try {
        const response = await axios.get(url,{
          });
        personal = response.data;
    }
    catch(error){
    }
    return personal;
}

export async function updatePersonal(user:User){
    let url = "http://localhost:8080/api/user/"+user.uid;
    try {
        await axios.put(url,user);
    }
    catch(error) {  
        
    }
}