import {
    useEffect,
    useState,
    CSSProperties,
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import { FaPen } from "react-icons/fa";
import { TiArrowBack } from "react-icons/ti";

import { DiscussionTopicContent,DiscussionTopicReply } from "schemas/discussion";

import { getDiscussionTopicContent , getDiscussionTopicReplyList } from "api/discussion";


const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{
    
}>;

export default function DiscussionReplyPage(props: propsType): React.ReactElement {
    const {
        

    } = props;

    const [discussionTopicReplyList,setDiscussionTopicReply] = useState<Array<DiscussionTopicReply>>([]);
    const [discussionTopicContent , setDiscussionTopicContent] = useState<DiscussionTopicContent>();
    const [showReplyArea, setShowReplyArea] = useState<boolean>(false);
    const [replyText, setReplyText] = useState<string>(""); 

    useEffect(()=>{
        getDiscussionTopicReplyList().then(data=>{
            setDiscussionTopicReply(data);
        });
        
    },[])

    const handleToggleReplyArea = () => {
        setShowReplyArea(!showReplyArea);
    };


    return (
        <div id="discussionReplyPage">
            <div className="mainDiscussionTopic">
                <div className="discussionTopicTop">
                    <img src={UserIcon}/>
                    <h3>發布者</h3>
                    <p>2024年02月14日(三) 17:48</p>
                </div>
                <h3>1-1第一題題意</h3>
                <p>新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財</p>
                <div className="discussionTopicBottom">
                    <p>回覆</p>
                </div>

                {
                    discussionTopicReplyList.map(data=>
                        <div className="discussionTopicReply">
                            <div className="discussionTopicTop">
                                <img src={UserIcon}/>
                                <h3>發布者</h3>
                                <p>{data.release_time}</p>
                            </div>
                            <p>{data.content}</p>
                            <div className="replyButton" onClick={handleToggleReplyArea}> 
                                <p>回覆</p>
                                <TiArrowBack/>
                            </div>
                        </div> 
                    )
                }
            </div>
                <div className={`replyArea ${showReplyArea ? 'visible' : 'hidden'}`}>
                    <img src={UserIcon}/>
                    <textarea
                        placeholder="回覆內容"
                        value={replyText}
                        onChange={(e) => setReplyText(e.target.value)}
                        rows={1}
                    />
                </div>
            
            
        </div>
    );
}
