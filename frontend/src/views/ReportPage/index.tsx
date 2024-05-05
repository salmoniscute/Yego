import { ReactElement, useState , useEffect} from "react";
import { Link } from "react-router-dom";
import PostEditor from "components/PostEditor";

import { getReportList } from "api/report";
import { Report } from "schemas/report";

import { IoArrowUp } from "react-icons/io5";
import { IoArrowDown } from "react-icons/io5";
import { FaPen } from "react-icons/fa";

import './index.scss';

export default function ReportPage(): ReactElement {
  const [openEditor, setopenEditor] = useState(false);
  const [reportList, setReportList] = useState<Array<Report>>([]);
  const [arrow, setArrow] = useState(true); //up = true, down = false
  const Open = () => {
    setopenEditor(true);
  }
  const Close = () => {
    setopenEditor(false);
  }

  useEffect(() => {
    handleReportList();
  }, [])

  const handleReportList = () =>{
    getReportList().then(data => {
      resortList(data, arrow);
    })
  };

  
  const resortList = (data:Report[] , state :boolean) =>{
    const sortedList = [...data]; 
    if (state === true) {
        sortedList.sort((d1, d2) => {
          const date1 = new Date(d1.release_time);
          const date2 = new Date(d2.release_time);
          return date2.getTime() - date1.getTime();
      });
        
    } else {
        sortedList.sort((d1, d2) => {
          const date1 = new Date(d1.release_time);
          const date2 = new Date(d2.release_time);
          return date1.getTime() - date2.getTime();
      });
        
    }
    setReportList(sortedList);

  }

  const Resort = () => {
    resortList(reportList,!arrow);
    setArrow(!arrow);
  }

  const setTimeString = (release_time:number):string => {
    const releaseDate = new Date(release_time);
    const formattedDate = `${releaseDate.getFullYear()}年${releaseDate.getMonth() + 1}月${releaseDate.getDate()}日`;
    return formattedDate
  }

  return <div id="reportPage">
    <div className="header">
      <h1>問題回報區</h1>
      <div className="reportButton" onClick={Open}><FaPen /><span>回報問題</span></div>
    </div>
    <div className="tutorial">
      <h4>操作教學說明</h4>
    </div>

    <div className="discussionTopic">
      <div className="discussionTopicTab">
        <p className="title">討論主題</p>
        <p className="launch">發布日期<button onClick={Resort}>{arrow === true ? <IoArrowUp /> : <IoArrowDown />}</button></p>
        <p className="reply">回覆</p>
      </div>
      {
        reportList.map((data,i) => 
          <div key={i} className="discussionTopicList">
            <p className="title">
                <Link to={`./${data.id}`}>{data.title}</Link>
            </p>
            <p className="launch">{setTimeString(data.release_time)}</p>
            <p className="reply">{data.reply}</p>
          </div>
        )
      }

    </div>
    <div className={openEditor === true ? '' : 'editor'}><PostEditor onClose={Close} type="report" updatePost={handleReportList} parent_id=""/></div>
  </div>
}