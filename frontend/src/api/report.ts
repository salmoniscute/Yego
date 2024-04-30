import { Report } from "schemas/report";
import axios from "axios";

export async function getReportList() : Promise<Array<Report>>{
    const result = [
        {
            uid:"F74106050",
            release_time: 1703390840,
            title:"1-1第一題題意",
            content:"",
            id:"",
            reply:1,
        },
        {
            uid:"F74106050",
            release_time: 1703390840,
            title:"救我啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
            id:"",
            reply:1,
            content:"",
        },

    ]
    return result;
}