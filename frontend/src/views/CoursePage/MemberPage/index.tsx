import {
    ReactElement,
    useEffect,
    useState
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";

import {
    getCourseMemberList
} from "api/courseMember";

import { OtherUser } from "schemas/otherUser";

export default function MemberPage(): ReactElement {
    const tab = ["成員名稱", "學號", "系所", "身份", "組別"]

    const [courseMemberList, setCourseMember] = useState<Array<OtherUser>>([]);
    const [selectedStudent, setSelectedStudent] = useState<OtherUser | undefined>();
    const [showMember, setShowMember] = useState<boolean>(false);

    useEffect(() => {
        getCourseMemberList().then(data => {
            setCourseMember(data);
        });
    }, [])

    return (
        <div id="courseMemberPage">
            <div className="courseMember">
                <div className="dropdownkey">
                    關鍵字搜尋或篩選
                    <span className="material-symbols-outlined">
                        stat_minus_1
                    </span>
                </div>
                <div className="courseMemberTab">
                    {tab.map((tab, index) => (
                        <p key={index} >
                            {tab}
                        </p>
                    ))}
                </div>
                {courseMemberList.map((data) =>
                    <div className="courseMemberContent">
                        <p key={data.uid} onClick={() => {
                            setShowMember(true);
                            setSelectedStudent(data)
                        }}>
                            <img src="https://i.imgur.com/XdMhWxz.png"/>
                            {data.name}
                        </p>
                        <p>{data.uid}</p>
                        <p>{data.department}</p>
                        <p>{data.role}</p>
                        <p>{data.group_name}</p>
                    </div> 
                )}
                <div className="memberWindow" data-show={showMember}>
                    <div className="closeWindow" onClick={() => {setShowMember(false)}} >
                        <span className="material-symbols-outlined">
                            close
                        </span>
                    </div>
                    <br/>
    
                    <div className="windowSet">
                        <div className="leftWindow">
                            <img alt="avatar" src="https://i.imgur.com/XdMhWxz.png"/>
                            <div className="OtherInfo">
                                <div className="OtherInfoTag">國家</div>
                                <div className="OtherInfoContent">{selectedStudent?.country}</div>
                            </div>
                            <div className="OtherInfo">
                                <div className="OtherInfoTag">科系</div>
                                <div className="OtherInfoContent">{selectedStudent?.department}</div>
                            </div>
                            <div className="OtherInfo">
                                <div className="OtherInfoTag">學號</div>
                                <div className="OtherInfoContent">{selectedStudent?.uid}</div>
                            </div>
                            <div className="memberMail">{selectedStudent?.email}</div>
                            <br/>
                        </div>
                        <div className="rightWindow">
                            <br/>
                            <div className="memberName">{selectedStudent?.name}</div>
                            <div className="memberIntro">
                                <div className="memberIntroTag">自我介紹</div>
                                <div className="memberIntroContent">
                                    {selectedStudent?.introduction}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>                                                       
            </div>

        </div>
    );
}
