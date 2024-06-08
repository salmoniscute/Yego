import {
    ReactElement,
    useContext
} from "react";
import { Link } from "react-router-dom";

import { AssignmentInfo } from "schemas/assignment";
import { Course } from "schemas/course";

import functionContext from "context/function";
import userDataContext from "context/userData";

import "./index.scss";

type propsType = Readonly<{
    dueAssignment: Array<AssignmentInfo>,
    currentCourse: Array<Course>,
}>;

export default function SideBar(props: propsType): ReactElement {
    const {
        dueAssignment,
        currentCourse,
    } = props;

    const {
        getText
    } = useContext(functionContext);
    const userData = useContext(userDataContext);

    return <label id="sideBar">
        <input type="checkbox" />
        <div className="body-bold">{getText("sidebar_menu")}</div>
        <div className="ms" />
        <div className="mask">
            <div className="content">
                <div className="personalHomepage">
                    <img alt="avatar" src={userData?.avatar} />
                    <Link to={`/personal/${userData?.uid}`} className="body-bold">{getText("personal_homepage")}</Link>
                </div>
                { userData?.role === "student" && <div className="caption-bold subTitle">{getText("due_soon")}</div>}
                { userData?.role === "student" &&
                    dueAssignment.map((data, i) => <div key={i} className="caption">
                        <Link to={`/course/${data.course_id}/${data.uid}`}>{data.assignment_name}</Link>
                    </div>)
                }
                <div className="caption-bold subTitle">{getText("calendar")}</div>
                <div className="caption-bold subTitle">{getText("this_semester_courses")}</div>
                {
                    currentCourse.map((data, i) => <div key={i} className="caption">
                        <Link to={`/course/${data.id}`}>{data.course_name}</Link>
                    </div>)
                }
                <div className="toolBox">
                    <Link to="/reportBug">{getText("report_bug")}</Link>
                    <div>{getText("dark_mode")}</div>
                    <Link to="/help">{getText("use_tutorial")}</Link>
                    <Link to="/setting">{getText("setting")}</Link>
                    <Link to="/logout">{getText("logout")}</Link>
                </div>
            </div>
        </div>
    </label>
};
