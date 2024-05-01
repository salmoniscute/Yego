import {
    useEffect,
    useState,
    CSSProperties,
} from "react";

import "./index.scss";
import { FaPen } from "react-icons/fa";
import { IoSend } from "react-icons/io5";
import { TiArrowBack } from "react-icons/ti";

import DiscussionReplyArea from "components/DiscussionReplyArea";
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
                <h3>1-1第一題題意</h3>
                <div className="discussionTopicTop">
                    <img src={UserIcon}/>
                    <h3>發布者</h3>
                    <p>2024年02月14日(三) 17:48</p>
                </div>
                <p>新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財新年快樂恭喜發財</p>
                <div className="discussionTopicBottom">
                    <p>回覆</p>
                </div>
            </div>
            <div >
                {
                    discussionTopicReplyList.map(data=>
                        <div className="discussionTopicReply">
                            <div className="discussionTopicReplyTop">
                                <img src={UserIcon}/>
                                <h3>發布者</h3>
                            </div>
                            <p>{data.content}</p>
                            <div className="discussionTopicReplyBottom">
                                <p>{data.release_time}</p>
                                <div className="replyButton" onClick={handleToggleReplyArea}> 
                                    <p>回覆</p>
                                    <TiArrowBack/>
                                </div>
                            </div>
                            { showReplyArea === true &&  <DiscussionReplyArea parentID={data.id}/>}
                        </div> 
                    )
                }
            </div>

            <DiscussionReplyArea parentID=""/>
                
        </div>
    );
}
