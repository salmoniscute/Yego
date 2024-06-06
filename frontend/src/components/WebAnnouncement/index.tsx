import React, { ReactElement, useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import functionContext from "context/function";

import "./index.scss";

type propsType = Readonly<{
    webAnnouncementList?: Array<WebAnnouncementInfo>,
}>;

function timestampToString(timestamp: string): string {
    let date = new Date(timestamp);
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`;
}

export default function WebAnnouncement(props: propsType): ReactElement {
    const { getText } = useContext(functionContext);
    const [announcementList, setAnnouncementList] = useState<Array<WebAnnouncementInfo>>([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const response = await axios.get("/website/bulletins");
                setAnnouncementList(response.data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        }

        fetchData();
    }, []);

    return (
        <div className="webAnnouncement">
            <h2>{getText("website_announcement")}</h2>
            <div className="content">
                {announcementList.sort((a, b) => {
                    if (a.pin_to_top && b.pin_to_top)
                        return 0;
                    return a.pin_to_top ? -1 : 1;
                }).map((data) => (
                    <div key={data.id} className="block" title={data.title}>
                        <div className="caption timestamp">{timestampToString(data.release_time)}</div>
                        <div className="pin caption-bold" data-pin={data.pin_to_top} >{data.pin_to_top ? "置頂" : ""}</div>
                        <Link className="body" style={{ fontWeight: "bold" }} to={`/webAnnouncement/${data.id}`}>{data.title}</Link>

                    </div>
                ))}
                <div className="seeMore">
                    <Link to="/webAnnouncementlist">查看更多</Link>
                </div>
            </div>
        </div>
    );
}
