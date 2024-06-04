import { jwtDecode } from "jwt-decode";

import axios from "axios";
import { User } from "schemas/user";

let access_token = "";

export async function login(username: string, password: string): Promise<User> {
    let url = "/auth/login?";
    try {
        const response = await axios.post(url,"username="+username+"&password="+password);
        console.log(response.data);
        access_token = response.data.access_token;
        localStorage.setItem("access_token", access_token);
        
    }
    catch {  
        console.log("hi");
        //return ;
    }

    return jwtDecode(access_token) as User;
}
