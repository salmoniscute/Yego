import React from "react";
import {
    ReactElement,
    useState,
    useEffect
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import { FaPen } from "react-icons/fa";
import { BiSolidBellRing } from "react-icons/bi";
import { TbBellRinging } from "react-icons/tb";

import { Discussion } from "schemas/discussion";
import { getDiscussionList } from "api/discussion";

type propsType = Readonly<{
    courseID: string,
}>;

export default function DiscussionPage(props: propsType): ReactElement {
    const [discussionList, setDiscussion] = useState<Array<Discussion>>([]);
    const {
        courseID

    } = props;

    useEffect(() => {
        getDiscussionList().then(data => {
            setDiscussion(data);
        })
    }, [])

    return (
        <div id="courseDiscussionPage">
            <div className="addDiscussionButton">
                <div className="buttonInfo">
                    <FaPen />
                    <p>新增討論區</p>
                </div>

            </div>
            <div className="discussion">
                <div className="discussionTab">
                    <p className="discussionTitle">標題</p>
                    <p className="discussionDiscription">說明</p>
                    <p >追蹤回覆</p>
                </div>
                {
                    discussionList.map(data =>
                        <div className="discussionInfo">
                            <p className="discussionTitle">
                                <Link to={`/discussionTopic/${data.discussion_id}`}>{data.title}</Link>
                            </p>
                            <p className="discussionDiscription">{data.discription}</p>
                            <BiSolidBellRing />
                        </div>
                    )
                }
            </div>

        </div>
    );
}
