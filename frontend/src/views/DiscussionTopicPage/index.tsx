import { ReactElement, useState , useEffect} from "react";
import { Link } from "react-router-dom";
import PostEditor from "components/PostEditor";

import { DiscussionTopicInfo } from "schemas/discussion";
import { getDiscussionTopicList } from "api/discussion";

import { BiSolidBellRing } from "react-icons/bi";
import { TbBellRinging } from "react-icons/tb";
import { IoArrowUp } from "react-icons/io5";
import { IoArrowDown } from "react-icons/io5";
import { FaPen } from "react-icons/fa";

import './index.scss';

type propsType = Readonly<{
  discussionTitle:string,
  discussionContent:string
}>;

export default function DiscussionTopicPage(props: propsType): ReactElement {

  const {
    discussionTitle,
    discussionContent
  } = props;

  const [discussionTopicList, setDiscussionTopic] = useState<Array<DiscussionTopicInfo>>([]);
  const [openEditor, setopenEditor] = useState(false);
  const Open = () => {
    setopenEditor(true);
  }
  const Close = () => {
    setopenEditor(false);
  }

  useEffect(() => {
    handleDiscussionTopicList();
  }, [])

  const handleDiscussionTopicList = () =>{
    getDiscussionTopicList().then(data => {
      setDiscussionTopic(data);
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

  return <div id="discussionTopicPage">
    <div className="header">
      <h1>{discussionTitle}</h1>
      <button onClick={Open}><FaPen /><span>新增討論主題</span></button>
    </div>
    <div className="tutorial">
      <h4 dangerouslySetInnerHTML={{ __html: discussionContent }}/>
    </div>

    <div className="discussionTopic">
      <div className="discussionTopicTab">
        <p className="title">討論主題</p>
        <p className="launch">發布日期<button onClick={Resort}>{arrow === true ? <IoArrowUp /> : <IoArrowDown />}</button></p>
        <p className="reply">回覆</p>
        <p className="follow">追蹤更新</p>
      </div>
      {
        discussionTopicList.map((data,i) => 
          <div key={i} className="discussionTopicList">
            <p className="title">
                <Link to={`./${data.id}`}>{data.title}</Link>
            </p>
            <p className="launch">{data.release_time}</p>
            <p className="reply">{data.reply}</p>
            <button className="follow"><p>{data.follow === true ? <BiSolidBellRing /> : <TbBellRinging />}</p></button> 
          </div>
        )
      }

    </div>
    
    {/* <div className={openEditor === true ? '' : 'editor'}><PostEditor onClose={Close} type="discussionTopic"/></div> */}
  </div>
}