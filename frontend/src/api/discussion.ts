import { 
    Discussion,
    DiscussionTopic,
    DiscussionTopicReply
 } from "schemas/discussion";
import axios from "axios";

export async function getDiscussionList(course_id:number, uid:string | null): Promise<Array<Discussion>>{
    let url = `/discussion/course/${course_id}?`;
    try {
        const response = await axios.get(url+"uid="+uid);
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}

export async function getDiscussion(id:number) : Promise <Discussion>{
    let url = "/discussion/"+id;
    let discussion;
    try {
        const response = await axios.get(url,{
          });
        discussion = response.data;
    }
    catch(error){
    }
    return discussion;
}
export async function postDiscussion(discussion:Discussion):Promise<Discussion | null>{
    let url = "/discussion?uid="+discussion.uid+"&course_id="+discussion.course_id;
    try {
        const response = await axios.post(url,discussion);
    }
    catch(error) {  
        
    }
    return discussion;
}


export async function getDiscussionTopicList(discussion_id:number, uid: string | null) : Promise<Array<DiscussionTopic>>{
    let url = `/discussion_topics/${discussion_id}?`;
    try {
        const response = await axios.get(url+"uid="+uid);
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}

export async function getDiscussionTopic(id:number) : Promise <DiscussionTopic>{
    let url = "/discussion_topic/"+id;
    let discussionTopic;
    try {
        const response = await axios.get(url,{
          });
        discussionTopic = response.data;
    }
    catch(error){
    }
    return discussionTopic;
}

export async function postDiscussionTopic(discussionTopic : DiscussionTopic):Promise<DiscussionTopic | null>{
    let url = "/discussion_topic?uid="+discussionTopic.uid+"&discussion_id="+discussionTopic.discussion_id;
    try {
        const response = await axios.post(url,discussionTopic);
    }
    catch(error) {  
        
    }
    return discussionTopic;
}

export async function postDTReply(reply:DiscussionTopicReply):Promise<DiscussionTopicReply | null>{
    let url = "/discussion_topic_reply?uid="+reply.uid+"&topic_id="+reply.topic_id + "&parent_id="+reply.parent_id;
    try {
        const response = await axios.post(url,reply);
        return response.data;
    }
    catch(error) {  
        
    }
    return reply;

}

export async function updateDiscussionTopic(discussionTopic : DiscussionTopic){
    let url = "/discussion_topic/"+discussionTopic.id;
    try {
        await axios.put(url,discussionTopic);
    }
    catch(error) {  
        
    }
}
