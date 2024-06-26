import React, { useCallback } from "react";
import {
    ReactElement,
    useState,
    useEffect,
    useContext
} from "react";
import { Link } from "react-router-dom";
import userDataContext from "context/userData";
import PostEditor from "components/PostEditor";

import "./index.scss";
import { FaPen } from "react-icons/fa";
import { TbBellRinging } from "react-icons/tb";
import { BiBell } from "react-icons/bi";

import { Discussion } from "schemas/discussion";
import { getDiscussionList } from "api/discussion";

import { create_subscription, cancel_subscription } from "api/subscription";
import functionContext from "context/function";

type propsType = Readonly<{
    courseID: number,
}>;

export default function DiscussionPage(props: propsType): ReactElement {
    const {
        courseID,
    } = props;

    const [discussionList, setDiscussion] = useState<Array<Discussion>>([]);
    const [openEditor, setopenEditor] = useState(false);
    
    const userData = useContext(userDataContext);
    const {
        setLoading
    } = useContext(functionContext);

    const Open = useCallback(() => {
        setopenEditor(true);
    }, []);
    const Close = useCallback(() => {
        setopenEditor(false);
    }, []);

    const handleDiscussionList = useCallback(() => {
        setLoading(true);
        getDiscussionList(courseID, userData ? userData.uid : null).then(data => {
            setDiscussion(data);
            console.log(data);
        }).catch(error => {
            if (error.response && error.response.status === 404) {

            }
        }).finally(() => {
            setLoading(false);
        });
    }, [courseID, userData, setLoading]);

    const follow = useCallback(async (data: Discussion) => {
        if (userData && data && data.id) {
            if (data.subscription_status === false) await create_subscription(userData.uid, data.id);
            else await cancel_subscription(userData.uid, data.id);
            handleDiscussionList();
        }
    }, [handleDiscussionList, userData]);

    useEffect(() => {
        handleDiscussionList();
    }, [handleDiscussionList]);

    return (
        <div id="courseDiscussionPage">
            {userData?.role === "teacher" && <div className="addDiscussionButton">
                <button onClick={Open}><FaPen /><span>新增討論區</span></button>
            </div>}
            <div className="yegogo">
                <img alt="Yegoo" src="/assets/Yegogo2.png" />
                <div>看起來討論的很熱烈！</div>
            </div>
            <div className="discussion">
                <div className="discussionTab">
                    <p className="discussionTitle">標題</p>
                    <p className="discussionDiscription">說明</p>
                    <p>追蹤回覆</p>
                </div>
                {
                    discussionList.map((data, i) =>
                        <div className="discussionInfo" key={i}>
                            <p className="discussionTitle">
                                <Link to={`./${data.id}`} >{data.title}</Link>
                            </p>
                            <div
                                className="discussionDiscription"
                                dangerouslySetInnerHTML={{ __html: data.content }}
                            />
                            <div className="discussionPadding"></div>
                            <button onClick={() => follow(data)}>{data.subscription_status === true ? <TbBellRinging /> : <BiBell />}</button>
                        </div>
                    )
                }

            </div>
            <div className={openEditor === true ? '' : 'editor'}><PostEditor onClose={Close} type="discussion" updatePost={handleDiscussionList} parent_id={courseID} isEditing={false} /></div>

        </div>
    );
}
