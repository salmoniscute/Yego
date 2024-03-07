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

import getTextOrigin from "utils/getText";

export default function App(): ReactElement {
    const [language, setLanguage] = useState<string>(localStorage.getItem("local") || "zh_Hant");
    const [webAnnouncementList, setWebAnnouncementList] = useState<Array<WebAnnouncementInfo>>([]);
    const [currentCourse, setCurrentCourse] = useState<Array<Course>>([]);
    const [pastCourse, setPastCourse] = useState<Array<Course>>([]);
    const [dueAssignment, setDueAssignment] = useState<Array<AssignmentInfo>>([]);

    const location = useLocation();

    const token = localStorage.getItem("access_token");
    const userData = useMemo(() => {
        try {
            return token === null ? null : jwtDecode(token) as User;
        }
        catch { }
        return null;
    }, [token]);

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
                        <Route path="/" element={<MainPage
                            webAnnouncementList={webAnnouncementList}
                            dueAssignment={dueAssignment}
                            currentCourse={currentCourse}
                            pastCourse={pastCourse}
                        />} />
                        <Route path="*" element={<Navigate to="/" />} />
                    </Routes>
                    <Footer />
                </div>
            </functionContext.Provider>
        </userDataContext.Provider>
    );
}
