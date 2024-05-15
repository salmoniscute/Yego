import { 
    OtherUser,
 } from "schemas/otherUser";

export async function getCourseMemberList() : Promise<Array<OtherUser>>{
    const result = [
        {
            uid: "F74106050",
            name: "張老師",
            role: "教授",
            department: "歷史系",
            avatar: "",
            country: "台灣",
            email: "Y1111@gmail.com",
            introduction: "hi",
            group_name: "A"

        },
        {
            uid: "F74106050",
            name: "張學生",
            role: "高階助教",
            department: "歷史系",
            avatar: "",
            country: "台灣",
            email: "T12222@gmail.com",
            introduction: "hi妳好",
            group_name: "B"
        },
        {
            uid: "F74106050",
            name: "Franziska",
            role: "學生",
            department: "不分系學位學程",
            avatar: "",
            country: "印度",
            email: "J12345@gmail.com",
            introduction: "我的名字叫吉良吉影，33歲。住在杜王町東北部的別墅區一帶，未婚。我在龜友連鎖店服務。每天都要加班到晚上8點才能回家。我不抽煙，酒僅止於淺嚐。晚上11點睡，每天要睡足8個小時。睡前，我一定喝一杯溫牛奶，然後做20分鐘的柔軟操，上了床，馬上熟睡。一覺到天亮，決不把疲勞和壓力留到第二天。醫生都說我很正常。",
            group_name: "C"
        }
    ]
    return result;
}