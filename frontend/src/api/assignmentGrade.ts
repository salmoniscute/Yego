import {AssignmentGrade } from "schemas/assignmentGrade";


export async function getAssignmentGrade(): Promise<Array<AssignmentGrade>> {
    return [
        {
            assignment_name: "第一周作業討論",
            teacher_comment: "討論HW1-1、1-2",
            score_status: "已評分",
            score: 99,
            grade: "A+",
        },
        {
            assignment_name: "第二周作業討論",
            teacher_comment: "",
            score_status: "未評分",
            score: NaN,
            grade: "",
        },
        {
            assignment_name: "第一次小考討論",
            teacher_comment: "",
            score_status: "未繳交",
            score: NaN,
            grade: "",
        },
    ];
}