import {
    useEffect,
    useState
} from "react";

import { AssignmentGrade } from "schemas/assignmentGrade";

import {getAssignmentGrade} from "api/assignmentGrade";

import "./index.scss";

export default function CourseGradePage(): React.ReactElement {   
    const tab = ["項目","教師評語","狀態","分數","等第"]

    const [courseAssignmentList,setCourseAssignment] = useState<Array<AssignmentGrade>>([]);

    useEffect(()=>{
        getAssignmentGrade().then(data=>{
            setCourseAssignment(data);
        });
    },[])

    return (
        <div id="courseGradePage">
            <div className="courseGradeTab">
                {tab.map((tab,index)=>(
                    <p key={index} >
                        {tab}
                    </p>
                ))}
            </div>
            
            {courseAssignmentList.map(data => 
                <div className="courseGradeContent">
                    <p className="assignmentName">{data.assignment_name}</p>
                    <p>{data.teacher_comment}</p>
                    <p>{data.score_status}</p>
                    <p>{data.score}</p>
                    <p>{data.grade}</p>
                </div>
            )}
            
        </div>
    )
}