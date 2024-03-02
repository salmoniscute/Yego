import React from "react";
import {
    ReactElement,
    useState
} from "react";
import { Link } from "react-router-dom";

import { LuClipboardCheck } from "react-icons/lu";
import CourseBulletinPage from "../CourseBulletinPage";
import CourseMemberPage from "../CourseMemberPage";

import "./index.scss";

type propsType = Readonly<{
    crouseID: string,
}>;

export default function CourseForum(props: propsType): React.ReactElement {
    const {
        crouseID
    } = props;

    const [signIn, setSignIn] = useState<string>("已簽到");

    const [activeTab, setActiveTab] = useState<string>('公告');

    const tab = [
        {label:'公告' , component : <CourseBulletinPage courseID= {crouseID}/>},
        {label:'討論區'},
        {label:'課程教材'},
        {label:'成績'},
        {label:'成員' , component : <CourseMemberPage/>}
    ];

    return (
        <div id="courseForum">
            <div className="titleInfor">
                <h6>課程名稱</h6>
                <div className="signIn" onClick={()=>{}}>
                    簽到
                    <LuClipboardCheck className="cfIcon"/>
                </div>
                <a href="">課程大綱</a>
                
            </div>
            <div className="forumCategory">
                {tab.map((tab,index)=>(
                    <div 
                        key={index} 
                        onClick={()=> setActiveTab(tab.label)} 
                        style={{color : activeTab == tab.label ? "black" : "#949494"}}
                    >
                        {tab.label}
                    </div>
                ))}
            </div>
            <div>
                {tab.find(tab => tab.label == activeTab)?.component}
            </div>
        </div>
    );
}
