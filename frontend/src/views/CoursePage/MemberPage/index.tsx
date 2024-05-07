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
                                <div className="OtherInfoContent">{selectedStudent?.department}</div>
                            </div>
                            <div className="OtherInfo">
                                <div className="OtherInfoTag">科系</div>
                                <div className="OtherInfoContent">{selectedStudent?.department}</div>
                            </div>
                            <div className="OtherInfo">
                                <div className="OtherInfoTag">學號</div>
                                <div className="OtherInfoContent">{selectedStudent?.department}</div>
                            </div>
                            <div className="memberMail">Email</div>
                            <br/>
                        </div>
                        <div className="rightWindow">
                            <br/>
                            <div className="memberName">{selectedStudent?.name}</div>
                            <div className="memberIntro">
                                <div className="memberIntroTag">自我介紹</div>
                                <div className="memberIntroContent">
                                    {selectedStudent?.department}
                                    我的名字叫吉良吉影，33歲。住在杜王町東北部的別墅區一帶，未婚。我在龜友連鎖店服務。每天都要加班到晚上8點才能回家。我不抽煙，酒僅止於淺嚐。晚上11點睡，每天要睡足8個小時。睡前，我一定喝一杯溫牛奶，然後做20分鐘的柔軟操，上了床，馬上熟睡。一覺到天亮，決不把疲勞和壓力留到第二天。醫生都說我很正常。」
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>                                                       
            </div>

        </div>
    );
}
