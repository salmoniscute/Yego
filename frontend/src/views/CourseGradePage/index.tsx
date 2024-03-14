import {
    useEffect,
    useState
} from "react";

import "./index.scss";

export default function CourseGradePage(): React.ReactElement {   
    const tab = ["項目","教師評語","狀態","分數","等第"]
    return (
        <div id="courseGradePage">
            <div className="courseGradeTab">
                {tab.map((tab,index)=>(
                    <p key={index} >
                        {tab}
                    </p>
                ))}
            </div>
        </div>
    )
}