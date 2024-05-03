import { ReactElement } from "react";

import "./index.scss";

export default function personal(): ReactElement {
    return (
        <div id="PersonalPage">
            <div className="avatar">
                <img alt="avatar" src="https://i.imgur.com/XdMhWxz.png"/>
                <div className="EditPerson">
                    <span className="material-symbols-outlined">edit</span>
                    <div>編輯個人資料</div>
                </div>
            </div>
            <div className="twoSide">
                <div className="leftSide">
                    <div className="Name">
                        學生姓名
                    </div>
                    <div className="eMail">
                        Y1111@gmail.com
                    </div>
                    <div className="Nation">
                        台灣
                    </div>
                    <div className="Department">
                        醫工系
                    </div>
                    <div className="ID">
                        xxxxxxxxx
                    </div>
                </div>
                <div className="rightSide">
                    自我介紹欄位
                </div>
            </div>

        </div>
    )
}