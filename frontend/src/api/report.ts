import { Report , ReportReply } from "schemas/report";
import axios from "axios";

export async function getReportList() : Promise<Array<Report>>{
    let url = "http://localhost:8080/api/reports";
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
    let url = "http://localhost:8080/api/report/"+id;
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
    let url = "http://localhost:8080/api/report?uid="+report.uid;
    try {
        const response = await axios.post(url,report);
    }
    catch(error) {  
        
    }
    return report;
}

export async function postReportReply(reply:ReportReply){

}