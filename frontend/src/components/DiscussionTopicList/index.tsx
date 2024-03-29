import { ReactElement, useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "./index.scss";

import { BiSolidBellRing } from "react-icons/bi";
import { TbBellRinging } from "react-icons/tb";
import { IoArrowUp } from "react-icons/io5";
import { IoArrowDown } from "react-icons/io5";

import { DiscussionTopicInfo } from "schemas/discussion";
import { getDiscussionTopicList } from "api/discussion";

export default function DiscussionTopicList(): ReactElement {
  const [discussionTopicList, setdiscussionTopic] = useState<Array<DiscussionTopicInfo>>([]);

  useEffect(() => {
    getDiscussionTopicList().then(data => {
      setdiscussionTopic(data);
    });
  }, [])


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

  const listRender = discussionTopicList.map((item) =>
    <div key={item.discussion_topic_id} className="list">
      <Link to="/" className="topic"><p>{item.title}</p></Link>
      <p className="launch">{item.release_time}</p>
      {/* <p className="reply">{item.reply}</p>
      <button className="follow"><p>{item.isFollow === true ? <BiSolidBellRing /> : <TbBellRinging />}</p></button>  */}
      <p className="reply">1</p>
      <button className="follow"><p>{<BiSolidBellRing />}</p></button>
    </div>
  );

  return <div id="DiscussionTopicList">
    <div className="list">
      <h3 className="topic">討論主題</h3>
      <h3 className="launch">發布日期<button onClick={Resort}>{arrow === true ? <IoArrowUp /> : <IoArrowDown />}</button></h3>
      <h3 className="reply">回覆</h3>
      <h3 className="follow">追蹤更新</h3>
    </div>
    {listRender}
  </div>
}
