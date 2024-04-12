export interface Discussion {
    discussion_id: string,
    uid:string,
    course_id: string,
    title:string,
    discription: string
};

export interface DiscussionTopicInfo {
    discussion_topic_id: string,
    uid : string,
    discussion_id: string,
    release_time: number,
    title:string,
};

export interface DiscussionTopicContent extends DiscussionTopicInfo {
    uid: string,
    publisher:string,
    content:string,
    files?: Array<string>,
};

export interface DiscussionTopicReply{
    discussion_topic_reply_id:string,
    uid:string,
    publisher:string,
    release_time: number,
    content:string,
}