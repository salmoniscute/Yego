import {
    useEffect,
    useState
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import { MdPushPin , MdOutlinePushPin} from "react-icons/md";

import { CourseBulletinInfo } from "schemas/courseBulletin";

import { getCourseBulletinList } from "api/courseBulletin";

const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{
    courseID:string
}>;

export default function CourseBulletinPage(props:propsType): React.ReactElement {
    const {
        courseID

    } = props;

    const [courseBulletinList,setCourseBulletin] =  useState<Array<CourseBulletinInfo>>([]);

    useEffect(()=>{
        getCourseBulletinList().then(data =>{
            setCourseBulletin(data);
        });
    },[]);

    return (
        <div id="courseBulletinPage">
            <p>課程公告</p>

            <div className="courseBulletin">
                {
                    courseBulletinList.map(data =>
                    <div className = "courseBulletinContent">
                        <div className="cbPin">
                            <MdOutlinePushPin/>
                        </div>
                        <div className="cb">
                            <p className="cbTitle">{data.title}</p>
                            <div className="cbContent">
                                <img src={UserIcon}/>
                                <div>
                                    <p className="cbAuther">{data.publisher}</p>
                                    <p className="cbTime">{data.release_time}</p>
                                    <p className="cbInfor">{data.content}</p>
                                </div>
                            </div>
                        </div>
                    </div>)
                }
            </div>
        </div>
    );
}