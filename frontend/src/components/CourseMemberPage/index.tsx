import {
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

export default function CourseMemberPage(): React.ReactElement {
    const tab = ["成員名稱","學號","系所","身份","組別"]

    const [courseMemberList,setCourseMember] = useState<Array<OtherUser>>([]);

    useEffect(()=>{
        getCourseMemberList().then(data=>{
            setCourseMember(data);
        });
    },[])
    return (
        <div id="courseMemberPage">
            <div className="courseMember">
                <div className="courseMemberTab">
                    {tab.map((tab,index)=>(
                        <p key={index} >
                            {tab}
                        </p>
                    ))}
                </div>
                {courseMemberList.map(data => 
                    <div className="courseMemberContent">
                        <p>{data.name}</p>
                        <p>{data.uid}</p>
                        <p>{data.department}</p>
                        <p>{data.role}</p>
                    </div>
                )}
            </div>
            
        </div>
    );
}
