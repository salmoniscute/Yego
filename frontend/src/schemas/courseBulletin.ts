export interface CourseBulletin {
    id?:string,
    uid: string,
    course_id:number,
    title: string,
    release_time?: number,
    pin_to_top: boolean,
    content: string,
    publisher: string,
    files?: Array<string>,
}
