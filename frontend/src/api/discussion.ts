import { 
    Discussion,
    DiscussionTopicInfo,
    DiscussionTopicContent,
    DiscussionTopicReply
 } from "schemas/discussion";

export async function getDiscussionList(): Promise<Array<Discussion>>{
    const result = [
        {
            discussion_id: "",
            course_id: "",
            title:"第一周作業討論",
            discription: "討論HW1-1、1-2"
        },
        {
            discussion_id: "",
            course_id: "",
            title:"第二周作業討論",
            discription: "討論HW2"
        },
        {
            discussion_id: "",
            course_id: "",
            title:"第一次小考討論",
            discription: "討論2/29課堂小考"
        },
    ]
    return result;
}


export async function getDiscussionTopicList() : Promise<Array<DiscussionTopicInfo>>{
    const result = [
        {
            discussion_topic_id: "",
            discussion_id: "",
            release_time: 1703390840,
            title:"1-1第一題題意",
        },
        {
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
        publisher_id: "F74106050",
        content:"新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財",
    });
};

export async function getDiscussionTopicReplyList() : Promise<Array<DiscussionTopicReply>>{
    const result = [
        {
            discussion_topic_reply_id:"",
            publisher_id:"F74106050",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },
        {
            discussion_topic_reply_id:"",
            publisher_id:"F74106050",
            release_time: 1703390840,
            content:"新年快樂恭喜發財",
        },

    ]
    return result;
}
