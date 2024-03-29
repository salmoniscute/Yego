import { ReactElement, useState } from "react";

import DiscussionList from "components/DiscussionTopicList";
import PostEditor from "components/PostEditor";

import './index.scss';

import { FaPen } from "react-icons/fa";


export default function DiscussionTopicPage(): ReactElement {


  const [openEditor, setopenEditor] = useState(false);
  const Open = () => {
    setopenEditor(true);
  }

  return <div id="reportPage">
    <div className="header">
      <h1></h1>
      <button onClick={Open}><FaPen /><span>新增討論主題</span></button>
    </div>
    <div className="tutorial">
      <h4>操作教學說明</h4>
    </div>
    <DiscussionList />
    <div className={openEditor === true ? '' : 'editor'}><PostEditor /></div>
  </div>
}