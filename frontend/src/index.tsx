import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./App";

import reportWebVitals from "./reportWebVitals";

import "./index.css";
import { setRequestConfig } from "./config/axios";
import ScrollToTop from "utils/scrollToTop";

// const testToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIwIiwibmFtZSI6InVzZXIiLCJyb2xlIjoic3R1ZGVudCIsImNvdW50cnkiOiJ0YWl3YW4iLCJkZXBhcnRtZW50IjoiQ1NJRSIsImVtYWlsIjoidXNlckB5ZWdvLmNvbSIsImludHJvZHVjdGlvbiI6ImludHJvZHVjdGlvbiJ9.8NZrmIVMsJC7IkWDLilOAU9Y-_Z_YUrTSIiK6nYF65s";
// const testLogin = true;
// if (testLogin) localStorage.setItem("access_token", testToken);
// else localStorage.removeItem("access_token");

// Setup axios
setRequestConfig();

const root = ReactDOM.createRoot(
    document.getElementById("root") as HTMLElement
);

root.render(
    <BrowserRouter>
        <ScrollToTop/>
        <App />
    </BrowserRouter>
);

reportWebVitals();
