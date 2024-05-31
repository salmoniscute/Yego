import {
    ReactElement,
    useContext
} from "react";
import {
    Link,
} from "react-router-dom";
import userDataContext from "context/userData";
import "./index.scss";

export default function Personal(): ReactElement {
    const userData = useContext(userDataContext);

    return (
        <div id="PersonalEditPage">
            <div className="twoSide">
                <div className="leftSide">
                    <img alt="avatar" src={userData?.avatar}/>
                    <div className="Name">
                        {userData?.name}
                    </div>
                    <Link className="EditPerson" to={`/personal/${userData?.uid}`}>
                        <div>&nbsp;結束編輯</div>
                    </Link>

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
                        <div className="OtherInfoTag">信箱</div>
                        <div className="OtherInfoContent">{userData?.email}</div>
                    </div>
                    <div className="IntroTag">自我介紹</div>
                    <div className="IntroContent">{userData?.introduction}</div>
                </div>
            </div>
        </div>
    )
}