import { jwtDecode } from "jwt-decode";
import {
    ReactElement,
    useEffect,
    useMemo,
    useState
} from "react";
import {
    Navigate,
    Route,
    Routes,
    useLocation
} from "react-router-dom";

import { User } from "./schemas/user";
import { WebAnnouncementInfo } from "./schemas/webAnnouncement";

import userDataContext from "./context/userData";
import languageContext from "context/language";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";
import MainPage from "./views/MainPage";


export default function App(): ReactElement {
    const [webAnnouncementList, setWebAnnouncementList] = useState<Array<WebAnnouncementInfo>>([]);
    const [language, setLanguage] = useState<string>(localStorage.getItem("local") || "zh_Hant");

    const location = useLocation();

    const token = localStorage.getItem("access_token");
    const userData = useMemo(() => {
        try {
            return token === null ? null : jwtDecode(token) as User;
        }
        catch { }
        return null;
    }, [token]);

    return (
        <userDataContext.Provider value={userData}>
            <languageContext.Provider value={language}>
                <div id="app">
                    <NavigateBar setLanguage={setLanguage} />
                    <Routes>
                        <Route path="/" element={<MainPage
                            webAnnouncementList={webAnnouncementList}
                            setWebAnnouncementList={setWebAnnouncementList}
                        />} />
                        <Route path="*" element={<Navigate to="/" />} />
                    </Routes>
                    <Footer />
                </div>
            </languageContext.Provider>
        </userDataContext.Provider>
    );
}
