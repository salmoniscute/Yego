import {
    ReactElement,
    useEffect,
    useState
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";

import {
    getCourseMemberList,
    getCourseMemberContent
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
                            {data.name}
                        </p>
                        <p>{data.uid}</p>
                        <p>{data.department}</p>
                        <p>{data.role}</p>
                    </div> 
                )}
                <div className="memberWindow" data-show={showMember}>
                    <div className="closeWindow" onClick={() => {setShowMember(false)}} >
                        <span className="material-symbols-outlined">
                            close
                        </span>
                    </div>
                    <br/><br/>
                    <div className="windowSet">
                        <div className="leftWindow">
                            <img alt="avatar" src="https://i.imgur.com/XdMhWxz.png"/>
                            <br/>
                            <div className="memberName">{selectedStudent?.name}</div>
                            <div className="memberMail">Email</div>
                            <br/>
                            <div className="memberIntro">自我介紹:</div>
                        </div>
                        <div className="rightWindow">
                            <br/>
                            <div>國家 &nbsp;&nbsp;&nbsp; {selectedStudent?.department}</div>
                            <br/>
                            <div>科系 &nbsp;&nbsp;&nbsp; {selectedStudent?.department}</div>
                            <br/>
                            <div>學號 &nbsp;&nbsp;&nbsp; {selectedStudent?.department}</div>
                        </div>
                    </div>
                </div>                                                       
            </div>

        </div>
    );
}
