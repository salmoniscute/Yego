import { ReactElement, useState } from "react";
import { Link } from "react-router-dom";

import "./index.scss";

import { BiSolidBellRing } from "react-icons/bi";
import { TbBellRinging } from "react-icons/tb";
import { IoArrowUp } from "react-icons/io5";
import { IoArrowDown } from "react-icons/io5";

export default function DiscussionList(): ReactElement {
  let list = [ //get list api
    {
      id: 0,
      topic: "畫面上的yegogo會跑來跑去",
      launch: "2024年3月9日",
      reply: 1,
      isFollow: false
    },
    {
      id: 1,
      topic: "yegogo太吵了",
      launch: "2024年3月10日",
      reply: 0,
      isFollow: true
    },
    {
      id: 2,
      topic: "yego閃退問題",
      launch: "2024年3月11日",
      reply: 2,
      isFollow: false
    }
  ];

  const [arrow, setArrow] = useState(true); //up = true, down = false
  const Resort = () => {
    if(arrow === true) {
      setArrow(false);
      // early->last api
    }
    else {
      setArrow(true);
      // last->early api
    }
  }

  const listRender = list.map((item) =>
    <div key={item.id} className="list">
      <Link to="/" className="topic"><p>{item.topic}</p></Link>
      <p className="launch">{item.launch}</p>
      <p className="reply">{item.reply}</p>
      <button className="follow"><p>{item.isFollow === true ? <BiSolidBellRing /> : <TbBellRinging />}</p></button> 
    </div>
  );

  return <>
  <div className="list">
      <h3 className="topic">討論主題</h3>
      <h3 className="launch">發布日期<button onClick={Resort}>{arrow === true ? <IoArrowUp /> : <IoArrowDown />}</button></h3>
      <h3 className="reply">回覆</h3>
      <h3 className="follow">追蹤更新</h3>
  </div>
  {listRender}
  </>
}
