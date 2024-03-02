import React from "react";
import { Link } from "react-router-dom";

import "./index.scss";

export default function CourseMemberPage(): React.ReactElement {
    const tab = ["成員名稱","學號","系所","身份","組別"]
    return (
        <div id="courseMemberPage">
            {tab.map((tab,index)=>(
                <p key={index} >
                    {tab}
                </p>
            ))}
            
        </div>
    );
}
