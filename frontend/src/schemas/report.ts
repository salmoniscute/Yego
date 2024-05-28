export interface Report {
    id?: number,
    uid : string,
    publisher_avatar : string ,
    release_time?: string,
    title:string,
    reply_number:number,
    publisher:string,
    content:string,
    files?: Array<string>,
    replies?:Array<ReportReply>,
};

export interface ReportReply{
    id?:number,
    parent_id : number ,
    report_id : number , 
    publisher_avatar : string ,
    uid:string,
    publisher:string,
    release_time?: string,
    content:string,
}