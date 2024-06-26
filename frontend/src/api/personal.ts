import axios from "axios";
import {
    User
} from "../schemas/user";

export async function getPersonal(uid:string) : Promise <User>{
    let url = "/user/"+uid;
    let personal;
    try {
        const response = await axios.get(url,{
          });
        personal = response.data;
        return personal;
    }
    catch(error){
    }
    return personal;
}

export async function updatePersonal(user:User){
    let url = "/user/"+user.uid;
    try {
        await axios.put(url,user);
    }
    catch(error) {  
        
    }
}

export async function updateAvatar(avatar:string){
    let url = "/user/avatar";
    try {
        await axios.put(url,avatar);
    }
    catch(error) {  
        
    }
}