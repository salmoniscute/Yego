import {
    ReactElement,
    useMemo,
    useState
} from "react";
import {
    Link,
    Navigate,
    Route,
    Routes,
    useParams
} from "react-router-dom";

import { LuClipboardCheck } from "react-icons/lu";
import BulletinPage from "./BulletinPage";
import MemberPage from "./MemberPage";
import DiscussionPage from "./DiscussionPage";

import "./index.scss";
import MaterialPage from "./MaterialPage";
import GradePage from "./GradePage";

export default function CoursePage(): ReactElement {
    const [signIn, setSignIn] = useState<string>("已簽到");

    const params = useParams();
    const { courseID } = params;
    const tab = params["*"]?.split("/")[0];

    const tabs = useMemo(() => courseID ? [
        { label: "公告", path: "announcement", component: <BulletinPage courseID={courseID} /> },
        { label: "討論區", path: "discussion", component: <DiscussionPage courseID={courseID} /> },
        { label: "課程教材", path: "material", component: <MaterialPage courseID={courseID} /> },
        { label: "成績", path: "grade", component: <GradePage /> },
        { label: "成員", path: "member", component: <MemberPage /> }
    ] : [], [courseID]);

    return courseID ? (
        <div id="courseForum">
            <div className="titleInfor">
                <h2>課程名稱</h2>
                <div className="signIn" onClick={() => { }}>
                    簽到
                    <LuClipboardCheck className="cfIcon" />
                </div>
                <a href="">課程大綱</a>
            </div>
            <div className="forumCategory">
                {
                    tabs.map((data, i) => (
                        <Link
                            className="tabLink body-bold"
                            key={i}
                            to={`./${data.path}`}
                            data-active={tab === data.path}
                        >{data.label}</Link>
                    ))}
            </div>
            <Routes>
                {
                    tabs.map((data, i) => <Route
                        key={i}
                        path={`/${data.path}`}
                        element={data.component}
                    />)
                }
                <Route path="*" element={<Navigate to={`./${tabs[0].path}`} />} />
            </Routes>
        </div>
    ) : <Navigate to="/" />;
}
