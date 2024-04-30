export interface Discussion {
    id: string,
    uid:string,
    course_id: string,
    title:string,
    content: string
    follow:boolean
};

export interface DiscussionTopicInfo {
    id: string,
    uid : string,
    discussion_id: string,
    release_time: number,
    title:string,
    reply:number,
    follow:boolean,
};

export interface DiscussionTopicContent extends DiscussionTopicInfo {
    uid: string,
    publisher:string,
    content:string,
    files?: Array<string>,
};

export interface DiscussionTopicReply{
    id:string,
    uid:string,
    publisher:string,
    release_time: number,
    content:string,
}