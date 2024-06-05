import { Report , ReportReply } from "schemas/report";
import axios from "axios";

export async function getReportList() : Promise<Array<Report>>{
    let url = "/reports";
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

export async function getReport(id : number ){
    let url = "/report/"+id;
    try {
        const response = await axios.get(url,{});
        const result = response.data;
        return result;
    }
    catch(error){
        return[];
    }
}

export async function postReport(report:Report) :Promise<Report | null>{
    let url = "/report?uid="+report.uid;
    try {
        const response = await axios.post(url,report);
    }
    catch(error) {  
        
    }
    return report;
}

export async function postReportReply(reply:ReportReply):Promise<ReportReply | null>{
    let url = "/report_reply?uid="+reply.uid+"&report_id="+reply.report_id + "&reply_id="+reply.parent_id;
    try {
        const response = await axios.post(url,reply);
        return response.data;
    }
    catch(error) {  
        
    }
    return reply;

}