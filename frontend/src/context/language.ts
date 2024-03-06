import {
    createContext
} from "react";

const languageContext = createContext<string>(localStorage.getItem("local") || "zh_Hant");
export default languageContext;
