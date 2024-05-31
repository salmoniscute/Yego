export interface CourseBulletin {
    id?:number,
    uid: string,
    course_id:number,
    title: string,
    release_time?: string,
    pin_to_top: boolean,
    content: string,
    publisher: string,
    files?: Array<string>,
}
