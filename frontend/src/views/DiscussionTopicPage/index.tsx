import { ReactElement, useState , useEffect} from "react";
import { Link ,useParams} from "react-router-dom";
import PostEditor from "components/PostEditor";

import { DiscussionTopic, Discussion } from "schemas/discussion";
import {  getDiscussionTopicList, getDiscussion } from "api/discussion";

import { BiSolidBellRing } from "react-icons/bi";
import { TbBellRinging } from "react-icons/tb";
import { IoArrowUp } from "react-icons/io5";
import { IoArrowDown } from "react-icons/io5";
import { FaPen } from "react-icons/fa";

import './index.scss';

type propsType = Readonly<{
}>;

export default function DiscussionTopicPage(props: propsType): ReactElement {

  const {
  } = props;

  const params = useParams();

  const [discussionTopicList, setDiscussionTopic] = useState<Array<DiscussionTopic>>([]);
  const [discussion , setDiscussion] = useState<Discussion>();
  const [openEditor, setopenEditor] = useState(false);
  const [arrow, setArrow] = useState(true); //up = true, down = false

  const Open = () => {
    setopenEditor(true);
  }
  const Close = () => {
    setopenEditor(false);
  }

  useEffect(() => {
    handleDiscussionTopicList();
    getDiscussion(params.discussionId || "").then( data=>{
      setDiscussion(data);
    })
  }, [])

  const handleDiscussionTopicList = () =>{
    getDiscussionTopicList(params.discussionId|| "").then(data => {
      resortList(data, arrow);
    });
  };

  const resortList = (data:DiscussionTopic[] , state :boolean) =>{
    const sortedList = [...data]; 
    if (state === true) {
        sortedList.sort((d1, d2) => {
          const date1 = new Date(d1.release_time||0);
          const date2 = new Date(d2.release_time||0);
          return date2.getTime() - date1.getTime();
      });
        
    } else {
        sortedList.sort((d1, d2) => {
          const date1 = new Date(d1.release_time||0);
          const date2 = new Date(d2.release_time||0);
          return date1.getTime() - date2.getTime();
      });
        
    }
    setDiscussionTopic(sortedList);
    console.log(discussionTopicList);
  }

  const Resort = () => {
    resortList(discussionTopicList,!arrow);
    setArrow(!arrow);
  }

  const setTimeString = (release_time:number):string => {
    const releaseDate = new Date(release_time);
    const formattedDate = `${releaseDate.getFullYear()}年${releaseDate.getMonth() + 1}月${releaseDate.getDate()}日`;
    return formattedDate;
  }

  return <div id="discussionTopicPage">
    <div className="header">
      <h1>{discussion?.title}</h1>
      <button onClick={Open}><FaPen /><span>新增討論主題</span></button>
    </div>
    <div className="tutorial">
      <h4 dangerouslySetInnerHTML={{ __html: discussion?.content || '' }}/>
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
                <Link to={`./discussionTopic/${data.id}`}>{data.title}</Link>
            </p>
            <p className="launch">{setTimeString(data.release_time||0)}</p>
            <p className="reply">{data.reply_number}</p>
            <button className="follow"><p>{data.follow === true ? <BiSolidBellRing /> : <TbBellRinging />}</p></button> 
          </div>
        )
      }

    </div>
    
    <div className={openEditor === true ? '' : 'editor'}><PostEditor onClose={Close} type="discussionTopic" updatePost={handleDiscussionTopicList} parent_id={Number(params.discussionId) || 0}/></div>
  </div>
}