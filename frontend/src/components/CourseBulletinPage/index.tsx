import React from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import CourseBulletin from "../CourseBulletin";

type propsType = Readonly<{
    courseID:string
}>;

export default function CourseBulletinPage(props:propsType): React.ReactElement {
    const {
        courseID

    } = props;

    return (
        <div id="courseBulletinPage">
            <p>課程公告</p>
            <CourseBulletin cbName="老師今天身體不適，所以今天不上課。" cbAuthorID="pinky" cbInfor="hello" cbTime="2024/1/1"/>
            <CourseBulletin cbName="老師今天身體不適，所以今天不上課。" cbAuthorID="pinky" cbInfor="hello" cbTime="2024/1/1"/>
        </div>
    );
}
