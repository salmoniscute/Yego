

import {
    ReactElement,
    useContext
} from "react";

import userDataContext from "context/userData";

import "./index.scss";

export default function Personal(): ReactElement {
    const userData = useContext(userDataContext);

    return (
        <div id="PersonalPage">
            <div className="twoSide">
                <div className="leftSide">
                    <img alt="avatar" src="https://i.imgur.com/XdMhWxz.png"/>
                    <div className="Name">
                        {userData?.name}
                    </div>
                    <div className="eMail">
                        {userData?.email}
                    </div>
                    <div className="EditPerson">
                        <span className="material-symbols-outlined">edit</span>
                        <div>編輯個人資料</div>
                    </div>
                </div>
                <div className="rightSide">
                    <div className="OtherInfo">
                        <div className="OtherInfoTag">國家</div>
                        <div className="OtherInfoContent">{userData?.country}</div>
                    </div>
                    <div className="OtherInfo">
                        <div className="OtherInfoTag">科系</div>
                        <div className="OtherInfoContent">{userData?.department}</div>
                    </div>
                    <div className="OtherInfo">
                        <div className="OtherInfoTag">學號</div>
                        <div className="OtherInfoContent">{userData?.uid}</div>
                    </div>
                    <div className="IntroTag">自我介紹</div>
                    <div className="IntroContent">{userData?.introduction}</div>
                </div>
            </div>

        </div>
    )
}