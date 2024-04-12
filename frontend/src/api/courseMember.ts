import { 
    OtherUser,
    OtherUserContent
 } from "schemas/otherUser";

export async function getCourseMemberList() : Promise<Array<OtherUser>>{
    const result = [
        {
            uid: "F74106050",
            name: "張老師",
            role: "教授",
            department: "歷史系",

        },
        {
            uid: "F74106050",
            name: "張學生",
            role: "高階助教",
            department: "歷史系",

        },
        {
            uid: "F74106050",
            name: "Franziska",
            role: "學生",
            department: "不分系學位學程",

        }
    ]
    return result;
}

export async function getCourseMemberContent(data: OtherUser): Promise<OtherUserContent | null> {
    return Object.assign(data, {
        country: "台灣",
        email: "Y1111@gmail.com",
        introduction: "hi",
    });
};