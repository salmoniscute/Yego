import {
    ReactElement,
    useContext,
} from "react";
import {
    Link,
    Navigate,
} from "react-router-dom";

import { AssignmentInfo } from "schemas/assignment";
import { Course } from "schemas/course";
import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import functionContext from "context/function";
import userDataContext from "context/userData";

import WebAnnouncement from "components/WebAnnouncement";
import PlatformFriendlyArea from "components/PlatformFriendlyArea";

import "./index.scss";

type propsType = Readonly<{
    webAnnouncementList: Array<WebAnnouncementInfo>,
    dueAssignment: Array<AssignmentInfo>,
    currentCourse: Array<Course>,
    pastCourse: Array<Course>,
}>;

export default function MainPage(props: propsType): ReactElement {
    const {
        webAnnouncementList,
        dueAssignment,
        currentCourse,
        pastCourse,
    } = props;

    const { getText } = useContext(functionContext)
    const userData = useContext(userDataContext);

    return userData === null ? <Navigate to="/" /> : <div id="mainPage">
        <div className="main">
            <WebAnnouncement webAnnouncementList={webAnnouncementList} />
            <div className="currentCourse">
                <h2>{getText("this_semester_courses")}</h2>
                <div className="content body">
                    {
                        currentCourse.map((data, i) => <div
                            key={i}
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
                        pastCourse.map((data, i) => <div
                            key={i}
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
                <div className="assignmentsDueSoon">
                    <h2>{getText("assignments_due_soon")}</h2>
                    <div className="content">
                        {
                            dueAssignment.map((data, i) => <Link
                                key={i}
                                to={`/course/${data.course_id}/${data.uid}`}
                                className="block"
                            >
                                <div className="caption" title={data.course_name}>{data.course_name}</div>
                                <div className="body" title={data.assignment_name}>{data.assignment_name}</div>
                            </Link>)
                        }
                    </div>
                </div>
                <PlatformFriendlyArea titleId="platform_friendly_area" />
            </div> : <div className="side">
                <PlatformFriendlyArea titleId="teacher_ta_friendly_area" />
            </div>
        }
    </div>;
};
