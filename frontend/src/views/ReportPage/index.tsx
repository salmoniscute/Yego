import { ReactElement, useState } from "react";

import DiscussionList from "components/DiscussionTopicList";
import PostEditor from "components/PostEditor";

import './index.scss';

import { FaPen } from "react-icons/fa";

export default function ReportPage(): ReactElement {
  const [openEditor, setopenEditor] = useState(false);
  const Open = () => {
    setopenEditor(true);
  }

  return <div id="reportPage">
    <div className="header">
      <h1>問題回報區</h1>
      <div className="reportButton" onClick={Open}><FaPen /><span>回報問題</span></div>
    </div>
    <div className="tutorial">
      <h4>操作教學說明</h4>
    </div>
    <DiscussionList />
    <div className={openEditor === true ? '' : 'editor'}><PostEditor /></div>
  </div>
}