import { Course } from "../schemas/course";

export async function getCurrentCourseList(): Promise<Array<Course>> {
    return [
        {
            uid: "3",
            teacher: "teacher1",
            course_code: "A2-001",
            academic_year: 112,
            semester: 2,
            name: "Course 0",
            outline: "Outline",
        },
        {
            uid: "4",
            teacher: "teacher1",
            course_code: "A2-002",
            academic_year: 112,
            semester: 2,
            name: "Course 1",
            outline: "Outline",
        },
        {
            uid: "5",
            teacher: "teacher1",
            course_code: "A2-003",
            academic_year: 112,
            semester: 2,
            name: "Course 2",
            outline: "Outline",
        },
    ];
};

export async function getPastCourseList(): Promise<Array<Course>> {
    return [
        {
            uid: "0",
            teacher: "teacher1",
            course_code: "A1-001",
            academic_year: 112,
            semester: 1,
            name: "Course 0",
            outline: "Outline",
        },
        {
            uid: "1",
            teacher: "teacher1",
            course_code: "A1-002",
            academic_year: 112,
            semester: 1,
            name: "Course 1",
            outline: "Outline",
        },
        {
            uid: "2",
            teacher: "teacher1",
            course_code: "A1-003",
            academic_year: 112,
            semester: 1,
            name: "Course 2",
            outline: "Outline",
        },
    ];
};
