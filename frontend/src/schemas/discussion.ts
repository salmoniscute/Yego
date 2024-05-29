export interface Discussion {
    id?: number,
    uid:string,
    course_id: number,
    title:string,
    content: string,
    follow:boolean,
    release_time?:string
};

export interface DiscussionTopic {
    id?: number,
    uid : string,
    discussion_id: number,
    publisher_avatar : string ,
    release_time?: string,
    title:string,
    reply_number:number,
    follow:boolean,
    publisher:string,
    content:string,
    files?: Array<string>,
    replies?:Array<DiscussionTopicReply>,
};

export interface DiscussionTopicReply{
    id?:number,
    parent_id : number ,
    topic_id : number , 
    publisher_avatar : string ,
    uid:string,
    publisher:string,
    release_time?: string,
    content:string,
}