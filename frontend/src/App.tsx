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

import userDataContext from "./context/userData";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";
import MainPage from "./views/MainPage";
import { WebAnnouncementInfo } from "./schemas/webAnnouncement";
import { User } from "./schemas/user";


export default function App(): ReactElement {
    // 網站公告清單
    const [webAnnouncementList, setWebAnnouncementList] = useState<Array<WebAnnouncementInfo>>([]);

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
            <div id="app">
                <NavigateBar />
                <Routes>
                    <Route path="/" element={<MainPage
                        webAnnouncementList={webAnnouncementList}
                        setWebAnnouncementList={setWebAnnouncementList}
                    />} />
                    <Route path="*" element={<Navigate to="/" />} />
                </Routes>
                <Footer />
            </div>
        </userDataContext.Provider>
    );
}
