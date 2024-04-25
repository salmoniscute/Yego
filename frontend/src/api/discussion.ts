import { 
    Discussion,
    DiscussionTopicInfo,
    DiscussionTopicContent,
    DiscussionTopicReply
 } from "schemas/discussion";
import axios from "axios";

export async function getDiscussionList(course_id:string): Promise<Array<Discussion>>{
    let url = "http://localhost:8080/api/discussions";
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

export async function postDiscussion(uid:string , course_id:string , title:string , content:string): Promise<Discussion>{
    let url = "http://localhost:8080/api/discussion?uid="+uid+"&course_id="+course_id;
    let discussion ;
    try {
        const response = await axios.post(url,{
            "title": title,
            "release_time": "2021-09-01T00:00:00",
            "content": content,
          });
        discussion = response.data;
    }
    catch(error) {  
        
    }

    return discussion;
}


export async function getDiscussionTopicList() : Promise<Array<DiscussionTopicInfo>>{
    const result = [
        {
            uid:"F74106050",
            discussion_topic_id: "",
            discussion_id: "",
            release_time: 1703390840,
            title:"1-1第一題題意",
        },
        {
            uid:"F74106050",
            discussion_topic_id: "",
            discussion_id: "",
            release_time: 1703390840,
            title:"救我啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        },

    ]
    return result;
}

export async function getDiscussionTopicContent(data: DiscussionTopicInfo): Promise<DiscussionTopicContent | null> {
    return Object.assign(data, {
        uid: "F74106050",
        publisher:"林志芸",
        content:"新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財",
    });
};

export async function getDiscussionTopicReplyList() : Promise<Array<DiscussionTopicReply>>{
    const result = [
        {
            discussion_topic_reply_id:"",
            uid:"F74106050",
            publisher:"林志芸",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },
        {
            discussion_topic_reply_id:"",
            uid:"F74106050",
            publisher:"林志芸",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },

    ]
    return result;
}
