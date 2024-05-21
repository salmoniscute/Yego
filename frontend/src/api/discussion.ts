import { 
    Discussion,
    DiscussionTopic,
    DiscussionTopicReply
 } from "schemas/discussion";
import axios from "axios";

export async function getDiscussionList(course_id:string): Promise<Array<Discussion>>{
    let url = "http://localhost:8080/api/discussions/"+course_id;
    try {
        const response = await axios.get(url,{
          });
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}

export async function getDiscussion(id:string) : Promise <Discussion>{
    let url = "http://localhost:8080/api/discussion/"+id;
    let discussion;
    try {
        const response = await axios.delete(url,{
          });
        discussion = response.data;
    }
    catch(error){
    }
    return discussion;
}
export async function postDiscussion(discussion:Discussion):Promise<Discussion | null>{
    let url = "http://localhost:8080/api/discussion?uid="+discussion.uid+"&course_id="+discussion.course_id;
    try {
        const response = await axios.post(url,discussion);
    }
    catch(error) {  
        
    }
    return discussion;
}


export async function getDiscussionTopicList(discussion_id:string) : Promise<Array<DiscussionTopic>>{
    let url = "http://localhost:8080/api/discussion_topics/"+discussion_id;
    try {
        const response = await axios.get(url,{
          });
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}

export async function getDiscussionTopic(id:string) : Promise <DiscussionTopic>{
    let url = "http://localhost:8080/api/discussion_topic/"+id;
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
    let url = "http://localhost:8080/api/discussion_topic?uid="+discussionTopic.uid+"&discussion_id="+discussionTopic.discussion_id;
    try {
        const response = await axios.post(url,discussionTopic);
    }
    catch(error) {  
        
    }
    return discussionTopic;
}

export async function getDiscussionTopicReplyList() : Promise<Array<DiscussionTopicReply>>{
    const result = [
        {
            id:"",
            uid:"F74106050",
            publisher:"林志芸",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },
        {
            id:"",
            uid:"F74106050",
            publisher:"林志芸",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },

    ]
    return result;
}
