import { jwtDecode } from "jwt-decode";

import { User } from "schemas/user";

const testToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIwIiwibmFtZSI6InVzZXIiLCJyb2xlIjoic3R1ZGVudCIsImNvdW50cnkiOiJ0YWl3YW4iLCJkZXBhcnRtZW50IjoiQ1NJRSIsImVtYWlsIjoidXNlckB5ZWdvLmNvbSIsImludHJvZHVjdGlvbiI6ImludHJvZHVjdGlvbiJ9.8NZrmIVMsJC7IkWDLilOAU9Y-_Z_YUrTSIiK6nYF65s";

export async function login(username: string, password: string): Promise<User> {
    let result = "";
    if (username === "user" && password === "password") {
        result = testToken;
    }
    else {
        throw Error;
    }

    localStorage.setItem("access_token", result);
    return jwtDecode(result) as User;
}
