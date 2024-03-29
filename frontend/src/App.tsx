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
import { Course } from "schemas/course";
import { User } from "./schemas/user";
import { WebAnnouncementInfo } from "./schemas/webAnnouncement";

import functionContext from "context/function";
import userDataContext from "./context/userData";

import { getDueAssignments } from "api/assignment";
import { getCurrentCourseList, getPastCourseList } from "api/course";
import { getWebAnnouncementList } from "api/webAnnouncement";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";

import MainPage from "./views/MainPage";
import LoginPage from "views/LoginPage";
import WebAnnouncementPage from "views/WebAnnouncementPage";


import CoursePage from "views/CoursePage";
import LandingPage from "views/LandingPage";
import ReportPage from "views/ReportPage";

import getTextOrigin from "utils/getText";
import DiscussionReplyPage from "views/DiscussionReplyPage";
import DiscussionTopicList from "components/DiscussionTopicList";

function Logout(): ReactElement {
    localStorage.removeItem("access_token")
    return <Navigate to="/" />
}


export default function App(): ReactElement {
    const [language, setLanguage] = useState<string>(localStorage.getItem("local") || "zh_Hant");
    const [webAnnouncementList, setWebAnnouncementList] = useState<Array<WebAnnouncementInfo>>([]);
    const [currentCourse, setCurrentCourse] = useState<Array<Course>>([]);
    const [pastCourse, setPastCourse] = useState<Array<Course>>([]);
    const [dueAssignment, setDueAssignment] = useState<Array<AssignmentInfo>>([]);

    const location = useLocation();

    const userData = useMemo(() => {
        const token = localStorage.getItem("access_token");
        try {
            return token === null ? null : jwtDecode(token) as User;
        }
        catch { }
        return null;
    }, [location.pathname]);

    const getText = useCallback((id: string) => {
        return getTextOrigin(id, language);
    }, [language]);

    useEffect(() => {
        getWebAnnouncementList().then(data => {
            setWebAnnouncementList(data);
        })

        getCurrentCourseList().then(data => {
            setCurrentCourse(data);
        });

        getPastCourseList().then(data => {
            setPastCourse(data);
        });

        getDueAssignments().then(data => {
            setDueAssignment(data);
        });
    }, []);

    return (
        <userDataContext.Provider value={userData}>
            <functionContext.Provider value={{
                getText: getText
            }}>
                <div id="app">
                    <NavigateBar
                        setLanguage={setLanguage}
                        dueAssignment={dueAssignment}
                        currentCourse={currentCourse}
                    />
                    <Routes>
                        <Route path="/landing" element={<LandingPage webAnnouncementList={webAnnouncementList} />} />
                        <Route path="/" element={userData === null ? <LandingPage
                            webAnnouncementList={webAnnouncementList}
                        /> : <MainPage
                            webAnnouncementList={webAnnouncementList}
                            dueAssignment={dueAssignment}
                            currentCourse={currentCourse}
                            pastCourse={pastCourse}
                        />} />
                        <Route path="/login" element={userData === null ? <LoginPage /> : <Navigate to="/" />} />
                        <Route path="/logout" element={<Logout />} />
                        <Route path="/webAnnouncement" element={<WebAnnouncementPage />} />
                        <Route path="/course/:courseID/*" element={<CoursePage />} />
                        <Route path="/reportBug" element={<ReportPage />} />
                        <Route path="/salmontest" element={<DiscussionReplyPage />} />
                        <Route path="*" element={<Navigate to="/" />} />
                    </Routes>
                    <Footer />
                </div>
            </functionContext.Provider>
        </userDataContext.Provider>
    );
}
