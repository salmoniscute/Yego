import { jwtDecode } from "jwt-decode";

import axios from "axios";
import { User } from "schemas/user";

let access_token = "";

export async function login(username: string, password: string): Promise<User> {
    let url = "http://localhost:8080/api/auth/login?";
    try {
        const response = await axios.post(url,"username="+username+"&password="+password);
        access_token = response.data.access_token;
        localStorage.setItem("access_token", access_token);
        
    }
    catch {  
        //return ;
    }

    return jwtDecode(access_token) as User;
}

export async function updateUserRole(uid:string , role :string ){
    let url = "http://localhost:8080/api/user/"+ uid+"/default_avatar?avatar="+role;
    try {
        await axios.put(url,);
        
    }
    catch {  
        
        //return ;
    }

}

export async function getUser(uid:string): Promise<User| null>{
    let url = "http://localhost:8080/api/user/" + uid;
    
    try {
        const response = await axios.get(url,);
        return response.data;
    }
    catch {  
        
        //return ;
    }
    return null ; 
}
