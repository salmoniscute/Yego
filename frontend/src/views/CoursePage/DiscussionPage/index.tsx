import React from "react";
import {
    ReactElement,
    useState
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import { FaPen } from "react-icons/fa";

type propsType = Readonly<{
    courseID: string,
}>;

export default function DiscussionPage(props: propsType): React.ReactElement {
    const {
        courseID

    } = props;


    return (
        <div id="discussionPage">
            <div className="addDiscussionButton">
                <div className="buttonInfo">
                    <FaPen className="icon"/>
                    <p>新增討論區</p>
                </div>

            </div>
            <div className="discussionTab">
                <p >討論區</p>
                <p style={{marginRight:"20em"}}>說明</p>
                <p >追蹤更新</p>
            </div>
            
        </div>
    );
}
