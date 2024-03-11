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
    useLocation,
    useParams
} from "react-router-dom";

import { LuClipboardCheck } from "react-icons/lu";
import BulletinPage from "./BulletinPage";
import MemberPage from "./MemberPage";
import DiscussionPage from "./DiscussionPage";

import "./index.scss";

export default function CoursePage(): ReactElement {
    const [signIn, setSignIn] = useState<string>("已簽到");

    const params = useParams();
    const { courseId } = params;
    const tab = params["*"]?.split("/")[0];
    console.log(tab)

    const tabs = useMemo(() => courseId ? [
        { label: "公告", path: "announcement", component: <BulletinPage courseID={courseId} /> },
        { label: "討論區", path: "discussion", component: <DiscussionPage courseID={courseId} /> },
        { label: "課程教材", path: "material" },
        { label: "成績", path: "score" },
        { label: "成員", path: "member", component: <MemberPage /> }
    ] : [], [courseId]);

    return courseId ? (
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
            <div>
                <Routes>
                    {
                        tabs.map((data, i) => <Route
                            key={i}
                            path={`${data.path}`}
                            element={data.component}
                        />)
                    }
                    <Route path="*" element={<Navigate to={`./${tabs[0].path}`} />} />
                </Routes>
            </div>
        </div>
    ) : <Navigate to="/" />;
}
