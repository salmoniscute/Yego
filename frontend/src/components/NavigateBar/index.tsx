import {
    CSSProperties,
    Dispatch,
    ReactElement,
    SetStateAction,
    useContext,
    useMemo,
    useState
} from "react";
import { Link } from "react-router-dom";

import { AssignmentInfo } from "schemas/assignment";
import { Course } from "schemas/course";

import functionContext from "context/function";
import userDataContext from "context/userData";

import SideBar from "components/SideBar";

import getTextOrigin, { localMap } from "utils/getText";

import "./index.scss";
import NotificationColumn from "components/NotificationColumn";
import { NotiContextProvider } from "../../views/NotificationPage/context";

type propsType = Readonly<{
    setLanguage: Dispatch<SetStateAction<string>>,
    dueAssignment: Array<AssignmentInfo>,
    currentCourse: Array<Course>,
}>;

export default function NavigateBar(props: propsType): ReactElement {
    const {
        setLanguage,
        dueAssignment,
        currentCourse,
    } = props;

    const {
        getText
    } = useContext(functionContext);
    const userData = useContext(userDataContext);

    const languageList: Array<string> = useMemo(
        () => Object.keys(localMap).map(
            key => getTextOrigin("current_language", key)
        ), []
    );
    const changeLanguage: Array<() => void> = useMemo(
        () => Object.keys(localMap).map(
            key => () => setLanguage(key)
        ), [setLanguage]
    );
    
    const [display, setDisplay] = useState(false);
    const DisplayNotification = () => {
        setDisplay(!display);
    }
    return (
        <div id="navigateBar">
            <Link to="/" className="logo">
                <h1>YEGO</h1>
            </Link>
            <label className="dropdownMenu">
                <input type="checkbox" />
                <div className="ms">language</div>
                <div className="body-bold">{getText("current_language")}</div>
                <div className="ms dropDown">arrow_drop_down</div>
                <div className="mask" style={{ "--length": languageList.length } as CSSProperties}>
                    <div className="content body-bold">
                        {
                            languageList.map((name, i) => <div
                                key={i}
                                onClick={changeLanguage[i]}
                            ><p>{name}</p></div>)
                        }
                    </div>
                </div>
            </label>
            {
                userData === null ? <Link
                    className="loginButton body-bold"
                    to={"/login"} >
                    {getText("login")}
                </Link> : <div className="notification">
                    <p className="ms" onClick={DisplayNotification}>notifications</p>
                    <div className="notificationBlock">{display === true ? 
                    <NotiContextProvider><NotificationColumn seeAllBtn={true}/></NotiContextProvider> : <></>}</div>
                </div>
            }
            {
                userData === null ? undefined : <SideBar
                    dueAssignment={dueAssignment}
                    currentCourse={currentCourse}
                />
            }
        </div>
    );
}
