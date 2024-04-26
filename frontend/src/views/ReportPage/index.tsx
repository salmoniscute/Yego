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
      setReportList(data);
    })
  };

  const [arrow, setArrow] = useState(true); //up = true, down = false
  const Resort = () => {
    if (arrow === true) {
      setArrow(false);
      // early->last api
    }
    else {
      setArrow(true);
      // last->early api
    }
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
            <p className="launch">{data.release_time}</p>
            <p className="reply">{data.reply}</p>
          </div>
        )
      }

    </div>
    <div className={openEditor === true ? '' : 'editor'}><PostEditor onClose={Close} type="report" updatePost={handleReportList}/></div>
  </div>
}