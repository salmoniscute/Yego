import {
    Dispatch,
    ReactElement,
    SetStateAction,
    useContext,
    useEffect,
    useState
} from "react";
import {
    Link,
    Navigate,
} from "react-router-dom";

import { AssignmentInfo } from "schemas/assignment";
import { Course } from "schemas/course";
import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import userDataContext from "context/userData";

import { getWebAnnouncementList } from "api/webAnnouncement";
import { getCurrentCourseList, getPastCourseList } from "api/course";

import getText from "utils/getText";

import "./index.scss";
import { getDueAssignments } from "api/assignment";

interface HelpInfo {
    id: string,
    title: string,
    description: string
};

const HelpList: Array<HelpInfo> = [
    {
        id: "0",
        title: "母課程申請",
        description: "操作教學說明"
    },
    {
        id: "1",
        title: "常見問題",
        description: "操作教學說明"
    },
    {
        id: "2",
        title: "問題說明",
        description: "操作教學說明"
    },
];

type propsType = Readonly<{
    webAnnouncementList: Array<WebAnnouncementInfo>,
    setWebAnnouncementList: Dispatch<SetStateAction<Array<WebAnnouncementInfo>>>,
}>;

export default function MainPage(props: propsType): ReactElement {
    const {
        webAnnouncementList,
        setWebAnnouncementList,
    } = props;
    const [webAnnouncementLoaded, setWebAnnouncementLoaded] = useState<boolean>(false);
    const [currentCourse, setCurrentCourse] = useState<Array<Course>>([]);
    const [pastCourse, setPastCourse] = useState<Array<Course>>([]);
    const [dueAssignment, setDueAssignment] = useState<Array<AssignmentInfo>>([]);

    const userData = useContext(userDataContext);

    useEffect(() => {
        if (userData === null) {
            return;
        }

        getWebAnnouncementList().then(data => {
            setWebAnnouncementList(data);
        }).finally(() => {
            setWebAnnouncementLoaded(true);
        });

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

    return userData === null ? <Navigate to="/" /> : <div id="mainPage">
        <div className="main">
            <div className="webAnnouncement">
                <h2>{getText("website_announcement")}</h2>
                <div className="content body-bold">
                    {
                        webAnnouncementList.map(data => <div
                            className="block"
                            title={data.title}
                        >
                            {
                                data.pin_to_top ? <svg width="12" height="20" viewBox="0 0 12 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M10 10V2H11V0H1V2H2V10L0 12V14H5.2V20H6.8V14H12V12L10 10Z" fill="black" />
                                </svg> : undefined
                            }
                            <Link to={`/webAnnouncement/${data.uid}`}>{data.title}</Link>
                        </div>)
                    }
                </div>
                <div className="seeMore">
                    <Link to="" >{getText("see_more")}</Link>
                </div>
            </div>
            <div className="currentCourse">
                <h2>{getText("this_semester_courses")}</h2>
                <div className="content body">
                    {
                        currentCourse.map(data => <div
                            className="block"
                            title={data.name}
                        >
                            <Link to={`/course/${data.uid}`}>{data.name}</Link>
                        </div>)
                    }
                </div>
            </div>
            <div className="pastCourse">
                <h2>{getText("past_courses")}</h2>
                <div className="content body">
                    {
                        pastCourse.map(data => <div
                            className="block"
                            title={data.name}
                        >
                            <Link to={`/course/${data.uid}`}>{data.name}</Link>
                        </div>)
                    }
                </div>
            </div>
        </div>
        {
            userData.role === "student" ? <div className="side">
                <h2>{getText("assignments_due_soon")}</h2>
                <div className="content">
                    {
                        dueAssignment.map(data => <Link
                            to={`/course/${data.course_id}/${data.uid}`}
                            className="block"
                        >
                            <div className="caption" title={data.course_name}>{data.course_name}</div>
                            <div className="body" title={data.assignment_name}>{data.assignment_name}</div>
                        </Link>)
                    }
                </div>
                <h2>{getText("platform_friendly_area")}</h2>
                <div className="content">
                    {
                        HelpList.map(data => <Link
                            to={`/help/${data.id}`}
                            className="block"
                        >
                            <div className="body-bold">{data.title}</div>
                            <div className="body">{data.description}</div>
                        </Link>)
                    }
                </div>
            </div> : <div className="side">
                <h2>{getText("teacher_ta_friendly_area")}</h2>
                <div className="content">
                    {
                        HelpList.map(data => <Link
                            to={`/help/${data.id}`}
                            className="block"
                        >
                            <div className="body-bold">{data.title}</div>
                            <div className="body">{data.description}</div>
                        </Link>)
                    }
                </div>
            </div>
        }
    </div>;
};
