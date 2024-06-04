import {
    ReactElement,
    useContext,
} from "react";
import {
    Link,
    Navigate,
} from "react-router-dom";
import React, { useEffect, useState} from "react";

import { AssignmentInfo } from "schemas/assignment";
import { Course } from "schemas/course";
import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import { getUserCourseList } from "api/course";
import functionContext from "context/function";
import userDataContext from "context/userData";

import WebAnnouncement from "components/WebAnnouncement";
import PlatformFriendlyArea from "components/PlatformFriendlyArea";

import "./index.scss";

type propsType = Readonly<{
    webAnnouncementList: Array<WebAnnouncementInfo>,
    dueAssignment: Array<AssignmentInfo>,
}>;

export default function MainPage(props: propsType): ReactElement {
    const [currentCourse, setCurrentCourse] = useState<Array<Course>>([]);
    const [bulletins, setBulletins] = useState<Array<WebAnnouncementInfo>>([]);
    const { getText } = useContext(functionContext);
    const userData = useContext(userDataContext);
    const {
        dueAssignment,
    } = props;

    useEffect(() => {
        fetch("http://localhost:8080/api/website/bulletins")
            .then(response => response.json())
            .then(data => {
                const parsedBulletins = data.map((bulletin: WebAnnouncementInfo) => ({
                    ...bulletin,
                    release_time: new Date(bulletin.release_time)
                }));
                setBulletins(parsedBulletins);
            })
            .catch(error => console.error("Error fetching bulletins", error));
        
        getUserCourseList(userData?.uid || "").then(data => {
            setCurrentCourse(data);
        });
    
    }, []);

    return userData === null ? <Navigate to="/" /> : <div><div id="mainPage">
        <div className="main">
             <WebAnnouncement webAnnouncementList={bulletins} />
            <div className="currentCourse">
                <h2>{getText("this_semester_courses")}</h2>
                <div className="content body">
                    {
                        currentCourse.map((data, i) => <div
                            key={i}
                            className="block"
                            title={data.course_name}
                        >
                            <div className="teacherName caption">{data.instructor_name}</div>
                            <Link to={`/course/${data.id}`}>{data.id}</Link>
                            <div className="infoBar">
                                <div className="assignments">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M3 3C1.89 3 1 3.89 1 5V19C1 20.11 1.9 21 3 21H17C18.11 21 19 20.11 19 19V9L13 3H3ZM12 10V4.5L17.5 10H12ZM23 7V13H21V7H23ZM21 15H23V17H21V15Z" fill="#F25C1C" />
                                    </svg>
                                    <span className="caption">0項作業即將過期</span>
                                </div>
                                <div className="announcement">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M13 11H11V5H13M13 15H11V13H13M20 2H4C2.9 2 2 2.9 2 4V22L6 18H20C21.1 18 22 17.1 22 16V4C22 2.9 21.1 2 20 2Z" fill="#4B67C9" />
                                    </svg>
                                    <span className="caption">新公告</span>
                                </div>
                            </div>
                        </div>)
                    }
                </div>
            </div>
            <PlatformFriendlyArea titleId="platform_friendly_area" />
        </div>
        {/* {
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
            </div> : <div className="side">
                <PlatformFriendlyArea titleId="teacher_ta_friendly_area" />
            </div>
        } */}
    </div>
    </div>
    
        ;
};
