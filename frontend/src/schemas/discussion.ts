export interface Discussion {
    id?: string,
    uid:string,
    course_id: number,
    title:string,
    content: string,
    follow:boolean,
    release_time?:number
};

export interface DiscussionTopic {
    id?: string,
    uid : string,
    discussion_id: string,
    discussion_id: number,
    release_time?: number,
    title:string,
    reply_number:number,
    follow:boolean,
    publisher:string,
    content:string,
    files?: Array<string>,
    replies?:Array<DiscussionTopicReply>,
};

export interface DiscussionTopicReply{
    id?:string,
    parent_id : string ,
    topic_id : string , 
    publisher_avatar : string ,
    uid:string,
    publisher:string,
    release_time?: number,
    content:string,
}