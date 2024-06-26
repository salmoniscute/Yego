import { jwtDecode } from "jwt-decode";
import {
    ReactElement,
    useCallback,
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

import { AssignmentInfo } from "schemas/assignment";
// import { Course } from "schemas/course";
import { User } from "./schemas/user";

import functionContext from "context/function";
import userDataContext from "./context/userData";

import { getDueAssignments } from "api/assignment";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";

import MainPage from "./views/MainPage";
import LoginPage from "views/LoginPage";
import WebAnnouncementPage from "views/WebAnnouncementPage";
import WebAnnouncementList from "views/WebAnnouncementLists";
import PersonalPage from "views/PersonalPage";

import CoursePage from "views/CoursePage";
import LandingPage from "views/LandingPage";
import ReportPage from "views/ReportPage";
import ReportReplyPage from "views/ReportReplyPage";

import TeamPage from "views/TeamPage";

import NotificationPage from "views/NotificationPage";

import getTextOrigin from "utils/getText";
import LoadingPage from "views/LoadingPage";

function Logout(): ReactElement {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    return <Navigate to="/" />
}


export default function App(): ReactElement {
    const [language, setLanguage] = useState<string>(localStorage.getItem("local") || "zh_Hant");
    // const [pastCourse, setPastCourse] = useState<Array<Course>>([]);
    const [dueAssignment, setDueAssignment] = useState<Array<AssignmentInfo>>([]);
    const [refreshToken , setRefreshToken] = useState<string>(localStorage.getItem("refresh_token")||"");
    const [showLoading, setShowLoading] = useState<boolean>(false);

    const location = useLocation();

    const userData = useMemo(() => {
        const token = localStorage.getItem("access_token");
        try {
            return token === null ? null : jwtDecode(token) as User; 
        }
        catch { }
        console.debug(refreshToken);
        console.debug(location.pathname);
        return null;
    }, [location.pathname, refreshToken]);

    const getText = useCallback((id: string) => {
        return getTextOrigin(id, language);
    }, [language]);

    const setLoading = useCallback((show: boolean) => {
        setShowLoading(show);
    }, []);

    useEffect(() => {
        getDueAssignments().then(data => {
            setDueAssignment(data);
        });
    }, []);

    return (
        <userDataContext.Provider value={userData}>
            <functionContext.Provider value={{
                getText: getText,
                setLoading: setLoading,
            }}>
                <div id="app">
                    <NavigateBar
                        setLanguage={setLanguage}
                        dueAssignment={dueAssignment}
                    />
                    <LoadingPage show={showLoading} />
                    <Routes>
                        <Route path="/landing" element={<LandingPage />} />
                        <Route path="/" element={userData === null ? <LandingPage /> : <MainPage
                            dueAssignment={dueAssignment}
                        />} />
                        <Route path="/login" element={userData === null ? <LoginPage setRefreshToken={setRefreshToken}/> : <Navigate to="/" />} />
                        <Route path="/logout" element={<Logout />} />
                        <Route path="/webAnnouncement/:id" element={<WebAnnouncementPage />} />
                        <Route path="/webAnnouncementlist" element={<WebAnnouncementList />} />
                        <Route path="/course/:courseID/*" element={<CoursePage />} />
                        <Route path="/personal/:uid/*" element={<PersonalPage PassSetRefreshToken={setRefreshToken}/>} />
                        <Route path="/reportBug" element={<ReportPage />} />  
                        <Route path="/reportBug/:reportId" element={<ReportReplyPage />} />
                        <Route path="/notification/:id" element={<NotificationPage />} />
                        <Route path="/group/:courseID" element={<TeamPage/>} />
                        <Route path="*" element={<Navigate to="/" />} />
                    </Routes>
                    <Footer />
                </div>
            </functionContext.Provider>
        </userDataContext.Provider>
    );
}
