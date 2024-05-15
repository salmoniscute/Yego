import {
    ReactElement,
    useContext
} from "react";
import { Link } from "react-router-dom";

import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import functionContext from "context/function";

import "./index.scss";

type propsType = Readonly<{
    webAnnouncementList: Array<WebAnnouncementInfo>,
}>;

function timestampToString(timestamp: number): string {
    let date = new Date(timestamp);
    return `${date.getFullYear()}-${date.getMonth().toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`;
}

export default function WebAnnouncement(props: propsType): ReactElement {
    const {
        webAnnouncementList,
    } = props;

    const { getText } = useContext(functionContext);

    return <div className="webAnnouncement">
        <h2>{getText("website_announcement")}</h2>
        <div className="content">
            {
                webAnnouncementList.map((data, i) => <div
                    key={i}
                    className="block"
                    title={data.title}
                >
                    <div className="caption timestamp">{timestampToString(data.release_time * 1000)}</div>
                    <div className="pin caption-bold" data-pin={data.pin_to_top}>置頂</div>
                    <Link className="body" to={`/webAnnouncement/${data.uid}`}>{data.title}</Link>
                </div>)
            }
            <div className="seeMore">
                <Link to="/webAnnouncement" >{getText("see_more")}</Link>
            </div>
        </div>
        
    </div>
}
