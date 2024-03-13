import { ReactElement } from "react";

import DiscussionList from "components/DiscussionList";

import './index.scss';

import { FaPen } from "react-icons/fa";

export default function ReportPage(): ReactElement {
  return <div id="reportPage">
    <div className="header">
      <h1>問題回報區</h1>
      <button><FaPen /><span>回報問題</span></button>
    </div>
    <div className="tutorial">
      <h4>操作教學說明</h4>
    </div>
    <DiscussionList />
  </div>
}