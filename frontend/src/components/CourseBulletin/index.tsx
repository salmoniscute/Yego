import React from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import UserIcon from "../../assets/testUser.png"

import { MdPushPin , MdOutlinePushPin} from "react-icons/md";
type propsType = Readonly<{
    cbName : string,
    cbInfor: string,
    cbAuthorID : string,
    cbTime : string,
}>;

export default function CourseBulletin(props:propsType): React.ReactElement {

    const {
        cbName,
        cbInfor,
        cbAuthorID,
        cbTime,

    } = props;

    return (
        <div id="courseBulletin">
            <div className="cbPin">
                <MdOutlinePushPin/>
            </div>
            <div className="cb">
                <p className="cbTitle">{cbName}</p>
                <div className="cbContent">
                    <img src={UserIcon}/>
                    <div>
                        <p className="cbAuther">張老師</p>
                        <p className="cbTime">{cbTime}</p>
                        <p className="cbInfor">{cbInfor}</p>
                    </div>
                </div>
            </div>
            
        </div>
    );
}
