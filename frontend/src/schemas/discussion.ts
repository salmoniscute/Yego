export interface DiscussionTopicInfo {
    discussion_topic_id: string,
    discussion_id: string,
    release_time: number,
    title:string,
};

export interface DiscussionTopicContent extends DiscussionTopicInfo {
    publisher_id: string,
    content:string,
    files?: Array<string>,
};

export interface DiscussionTopicReply{
    discussion_topic_reply_id:string,
    publisher_id:string,
    release_time: number,
    content:string,
}