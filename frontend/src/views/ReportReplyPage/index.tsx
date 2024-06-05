
import "./index.scss";
import { ReportReply, Report } from "schemas/report";
import { getReport , postReportReply } from "api/report";
import {
    useEffect,
    useState,
    CSSProperties,
    useContext,
    useRef,
    useCallback
} from "react";
import { Link ,useParams} from "react-router-dom";
import "./index.scss";
import { IoSend } from "react-icons/io5";
import { SlOptions } from "react-icons/sl";
import { TiArrowBack } from "react-icons/ti";
import PostEditor from "components/PostEditor";
import userDataContext from "context/userData";
type propsType = Readonly<{
    
}>;

export default function DiscussionReplyPage(props: propsType): React.ReactElement {

    const params = useParams();
    const userData = useContext(userDataContext);
    
    const [report , setReport] = useState<Report>();
    const [openEditor, setOpenEditor] = useState(false);
    const [replyContentList, setReplyContentList] = useState(Array());
    const [showReplyAreaList, setShowReplyAreaList] = useState(Array());
    const [mainReply , setMainReply] = useState("");
    const [showMainReplyArea, setShowMainReplyArea] = useState(false);
    const mainReplyAreaRef = useRef<HTMLDivElement>(null);
    const [categorizedReplies, setCategorizedReplies] = useState<{ [key: number]: ReportReply[] }>({});
    
    const handleDiscussionTopic = useCallback(() => {
        getReport(Number(params.reportId) || 0).then(data => {
            setReport(data);
            const newCategorizedReplies: { [key: number]: ReportReply[] } = { 0: [] };
            data.replies?.forEach(reply => {
                if (reply.parent_id === 0) {
                    newCategorizedReplies[reply.id || 0] = [];
                }
                if (!newCategorizedReplies[reply.parent_id]) {
                    newCategorizedReplies[reply.parent_id] = [];
                }
                newCategorizedReplies[reply.parent_id].push(reply);
            });
            setCategorizedReplies(newCategorizedReplies);
            setReplyContentList(new Array(newCategorizedReplies[0]?.length || 0).fill(''));
            setShowReplyAreaList(new Array(newCategorizedReplies[0]?.length || 0).fill(false));
        });
    }, [params.discussionTopicId]);

    useEffect(() => {
        handleDiscussionTopic();
    }, [handleDiscussionTopic]);

    const handleMainReplyClick = () => {
        setShowMainReplyArea(true);
        setTimeout(() => {
            if (mainReplyAreaRef.current) {
                mainReplyAreaRef.current.scrollIntoView({ behavior: 'smooth' });
            }
        }, 100);
    };

    const handleToggleReplyArea = (index: number) => {
        const newShowReplyAreaList = [...showReplyAreaList];
        newShowReplyAreaList[index] = !newShowReplyAreaList[index];
        setShowReplyAreaList(newShowReplyAreaList);
    };

    const handleReplyContentChange = (index: number, value: string) => {
        const newReplyContentList = [...replyContentList];
        newReplyContentList[index] = value;
        setReplyContentList(newReplyContentList);
    };

    type Option = {
        label: string;
        action: (() => void) | undefined;
    };

    const editOptions = (): Option[] => [
        { label: "編輯", action: Open },
    ];

    const Open = () => {
        setOpenEditor(true);
    };

    const Close = () => {
        setOpenEditor(false);
    };

    const setTimeString = (release_time: string): string => {
        const releaseDate = new Date(release_time);
        const weekdays = ["日", "一", "二", "三", "四", "五", "六"];
        return `${releaseDate.getFullYear()}年${("0" + (releaseDate.getMonth() + 1)).slice(-2)}月${("0" + releaseDate.getDate()).slice(-2)}日(${weekdays[releaseDate.getDay()]}) ${("0" + releaseDate.getHours()).slice(-2)}:${("0" + releaseDate.getMinutes()).slice(-2)}`;
    };

    const postReply = async (parent_id: number, index: number) => {
        if (userData) {
            const reply: ReportReply = {
                parent_id: parent_id,
                report_id : Number(params.reportId)|| 0,
                publisher_avatar: userData.avatar,
                uid: userData.uid,
                publisher: userData.name,
                content: "",
            };
            if (parent_id === 0) {
                reply.content = mainReply;
                const response = await postReportReply(reply);
                if (response) {
                    setCategorizedReplies(prevState => {
                        const updatedReplies = { ...prevState };
                        updatedReplies[0].push(response);
                        updatedReplies[response.id || 0] = [];
                        return updatedReplies;
                    });
                }
                setMainReply("");
                setShowMainReplyArea(false);
            } else {
                reply.content = replyContentList[index];
                const response = await postReportReply(reply);
                if (response) {
                    setCategorizedReplies(prevState => {
                        const updatedReplies = { ...prevState };
                        updatedReplies[parent_id].push(response);
                        return updatedReplies;
                    });
                }
            }
            setReplyContentList(new Array(categorizedReplies[0]?.length || 0).fill(''));
            setShowReplyAreaList(new Array(categorizedReplies[0]?.length || 0).fill(false));
        }
    };
    return (
        <div id="discussionReplyPage">
            <div className="mainDiscussionTopic">
                <div className="mainDtTop">
                    <h3>{report?.title}</h3>
                    { report?.uid === userData?.uid && <label className="dropdownMenu">
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
                    <img src={report?.publisher_avatar}/>
                    <h3>{report?.publisher}</h3>
                    <p>{setTimeString(report?.release_time||"")}</p>
                </div>
                <div className="dtContent">
                    <p dangerouslySetInnerHTML={{ __html: report?.content || '' }}/>
                </div>
                <div className="dtBottom" onClick={handleMainReplyClick}>
                    <p>回覆</p>
                </div>
            </div>
            <div >
                {
                    report && report.replies && categorizedReplies[0] && (
                        categorizedReplies[0].map((data,index)=>(
                            <div key={index} className="discussionTopicReply">
                                <div className="discussionTopicReplyTop">
                                    <img src={data.publisher_avatar}/>
                                    <h3>{data.publisher}</h3>
                                </div>
                                <p>{data.content}</p>
                                <div className="discussionTopicReplyBottom">
                                    <p>{setTimeString(data?.release_time||"")}</p>
                                    <div className="replyButton" onClick={()=>handleToggleReplyArea(index)}> 
                                        <p>回覆</p>
                                        <TiArrowBack/>
                                    </div>
                                </div>
                                { showReplyAreaList[index] === true &&  <div className="discussionReplyArea">
                                    <img src={userData?.avatar}/>
                                    <textarea
                                        placeholder="回覆留言"
                                        value={replyContentList[index]}
                                        onChange={(e) => handleReplyContentChange(index,e.target.value)}
                                        rows={1}
                                    />
                                    <IoSend className="sendIcon" onClick={() => postReply(data.id||0 , index)}/>
                                </div>}

                                { data.id && categorizedReplies[Number(data.id)] && (categorizedReplies[Number(data.id)].map((data2,index2)=>(
                                    <div key={index2} className="replyTheReply">
                                        <div className="replyTheReplyTop">
                                            <img src={data2.publisher_avatar}/>
                                            <h3>{data2.publisher}</h3>
                                        </div>
                                        <p>{data2.content}</p>
                                        <p>{setTimeString(data2?.release_time||"")}</p>
                                    </div>
                                )))}
                            </div> 
                        )
                            
                    ))
                }
            </div>

            { showMainReplyArea && <div className="discussionReplyArea" ref={mainReplyAreaRef}>
                <img src={userData?.avatar}/>
                <textarea
                    placeholder="回覆貼文"
                    value={mainReply}
                    onChange={(e) => setMainReply(e.target.value)}
                    rows={1}
                />
                <IoSend className="sendIcon" onClick={() => postReply(0 , 0)}/>
            </div>}
            
        </div> 
    );
}
