import { AssignmentInfo } from "schemas/assignment";


export async function getDueAssignments(): Promise<Array<AssignmentInfo>> {
    return [
        {
            uid: "0",
            course_id: 0,
            course_name: "Course 0",
            assignment_name: "HW 1",
        },
        {
            uid: "1",
            course_id: 0,
            course_name: "Course 0",
            assignment_name: "HW 2",
        },
        {
            uid: "2",
            course_id: 0,
            course_name: "Course 0",
            assignment_name: "HW 3",
        },
    ];
}