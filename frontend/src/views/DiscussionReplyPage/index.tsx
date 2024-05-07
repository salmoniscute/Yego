import {
    useEffect,
    useState,
    CSSProperties,
    useContext,
} from "react";
import { Link ,useParams} from "react-router-dom";
import "./index.scss";
import { FaPen } from "react-icons/fa";
import { IoSend } from "react-icons/io5";
import { SlOptions } from "react-icons/sl";
import { TiArrowBack } from "react-icons/ti";

import userDataContext from "context/userData";
import DiscussionReplyArea from "components/DiscussionReplyArea";
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
    const [showReplyArea, setShowReplyArea] = useState<boolean>(false);

    useEffect(()=>{
        getDiscussionTopic(params.discussionTopicId || "").then( data =>{
            setDiscussionTopic(data);
        })
        getDiscussionTopicReplyList().then(data=>{
            setDiscussionTopicReply(data);
        });
        
    },[])

    const handleToggleReplyArea = () => {
        setShowReplyArea(!showReplyArea);
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
                <h3>{discussionTopic?.title}</h3>
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
