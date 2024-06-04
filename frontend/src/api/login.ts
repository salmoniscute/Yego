import { jwtDecode } from "jwt-decode";

import axios from "axios";
import { User } from "schemas/user";

let access_token = "";
let refresh_token = "";

export async function login(username: string, password: string): Promise<User> {
    let url = "/api/auth/login";
    try {
        const response = await axios.post(url,"username="+username+"&password="+password);
        access_token = response.data.access_token;
        refresh_token = response.data.refresh_token;
        localStorage.setItem("access_token", access_token);
        localStorage.setItem("refresh_token", refresh_token);
        
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

export async function updateUser(user:User): Promise<User| null>{
    let url = "http://localhost:8080/api/user/" + user.uid;
    
    try {
        const response = await axios.put(url,user);
        return response.data;
    }
    catch {  
        
        //return ;
    }
    return null ; 
}

export async function refreshToken(){
    let url = "http://localhost:8080/api/auth/refresh";
    try {
        const response = await axios.post(url,{
            "refresh_token":localStorage.getItem("refresh_token")
        });
        access_token = response.data.access_token;
        refresh_token = response.data.refresh_token;
        localStorage.setItem("access_token", access_token);
        localStorage.setItem("refresh_token", refresh_token);
        
    }
    catch {  
        //return ;
    }

}


