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

export default function WebAnnouncement(props: propsType): ReactElement {
    const {
        webAnnouncementList,
    } = props;

    const { getText } = useContext(functionContext);

    return <div className="webAnnouncement">
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
            <Link to="/webAnnouncement" >{getText("see_more")}</Link>
        </div>
    </div>
}
