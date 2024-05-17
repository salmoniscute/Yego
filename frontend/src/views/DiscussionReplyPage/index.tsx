import {
    useEffect,
    useState,
    CSSProperties,
    useContext,
} from "react";
import { Link ,useParams} from "react-router-dom";
import "./index.scss";
import { IoSend } from "react-icons/io5";
import { SlOptions } from "react-icons/sl";
import { TiArrowBack } from "react-icons/ti";

import userDataContext from "context/userData";
import { DiscussionTopic,DiscussionTopicReply } from "schemas/discussion";
import {  getDiscussionTopicReplyList } from "api/discussion";
import { getDiscussionTopic } from "api/discussion";

const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{
    
}>;

export default function DiscussionReplyPage(props: propsType): React.ReactElement {

    const params = useParams();
    const userData = useContext(userDataContext);
    const [discussionTopicReplyList,setDiscussionTopicReply] = useState<Array<DiscussionTopicReply>>([]);
    const [discussionTopic , setDiscussionTopic] = useState<DiscussionTopic>();
    const [replyContentList, setReplyContentList] = useState(Array(discussionTopicReplyList.length).fill(''));
    const [showReplyAreaList, setShowReplyAreaList] = useState(Array(discussionTopicReplyList.length).fill(false));
    const [mainReply , setMainReply] = useState("");

    useEffect(()=>{
        getDiscussionTopic(params.discussionTopicId || "").then( data =>{
            setDiscussionTopic(data);
        })
        getDiscussionTopicReplyList().then(data=>{
            setDiscussionTopicReply(data);
        });
        
    },[])

    const handleToggleReplyArea = (index:number) => {
        const newShowReplyAreaList = [...showReplyAreaList];
        newShowReplyAreaList[index] = !newShowReplyAreaList[index];
        setShowReplyAreaList(newShowReplyAreaList);
    };
    const handleReplyContentChange = (index:number, value:string) => {
        const newReplyContentList = [...replyContentList];
        newReplyContentList[index] = value;
        setReplyContentList(newReplyContentList);
    };


    type Option = {
        label: string;
        action: (() => void) | undefined;
    };
    
    const editOptions = (): Option[] => [
        { label: "編輯" ,action:undefined },
    ];

    const setTimeString = (release_time:number):string => {
        const releaseDate = new Date(release_time);
        const weekdays = ["日", "一", "二", "三", "四", "五", "六"];
        const formattedDate = `${releaseDate.getFullYear()}年${("0" + (releaseDate.getMonth() + 1)).slice(-2)}月${("0" + releaseDate.getDate()).slice(-2)}日(${weekdays[releaseDate.getDay()]}) ${("0" + releaseDate.getHours()).slice(-2)}:${("0" + releaseDate.getMinutes()).slice(-2)}`;
        return formattedDate;
    }

    return (
        <div id="discussionReplyPage">
            <div className="mainDiscussionTopic">
                <div className="mainDtTop">
                    <h3>{discussionTopic?.title}</h3>
                    { discussionTopic?.uid === userData?.uid && <label className="dropdownMenu">
                        <SlOptions/>
                        <input type="checkbox" />
                        <div className="mask" style={{ "--length": 1 } as CSSProperties}>
                            <div className="content body-bold">
                                {
                                    editOptions().map((option, i) => <div
                                    key={i}
                                    onClick={option.action}
                                ><p>{option.label}</p></div>)
                                }
                            </div>
                        </div>
                    </label>}
                </div>
                
                <div className="discussionTopicTop">
                    <img src={UserIcon}/>
                    <h3>{discussionTopic?.publisher}</h3>
                    <p>{setTimeString(discussionTopic?.release_time||0)}</p>
                </div>
                <div className="dtContent">
                    <p dangerouslySetInnerHTML={{ __html: discussionTopic?.content || '' }}/>
                </div>
                <div className="dtBottom">
                    <p>回覆</p>
                </div>
                
            </div>
            <div >
                {
                    discussionTopicReplyList.map((data,index)=>
                        <div key={index} className="discussionTopicReply">
                            <div className="discussionTopicReplyTop">
                                <img src={UserIcon}/>
                                <h3>發布者</h3>
                            </div>
                            <p>{data.content}</p>
                            <div className="discussionTopicReplyBottom">
                                <p>{data.release_time}</p>
                                <div className="replyButton" onClick={()=>handleToggleReplyArea(index)}> 
                                    <p>回覆</p>
                                    <TiArrowBack/>
                                </div>
                            </div>
                            { showReplyAreaList[index] === true &&  <div className="discussionReplyArea">
                                <img src={UserIcon}/>
                                <textarea
                                    placeholder="回覆留言"
                                    value={replyContentList[index]}
                                    onChange={(e) => handleReplyContentChange(index,e.target.value)}
                                    rows={1}
                                />
                                <IoSend className="sendIcon"/>
                            </div>}
                        </div> 
                    )
                }
            </div>

            <div className="discussionReplyArea">
                <img src={UserIcon}/>
                <textarea
                    placeholder="回覆貼文"
                    value={mainReply}
                    onChange={(e) => setMainReply(e.target.value)}
                    rows={1}
                />
                <IoSend className="sendIcon"/>
            </div>
                
        </div>
    );
}
