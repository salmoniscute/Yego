import {
    ReactElement,
    useContext,
    SetStateAction,
    Dispatch
} from "react";

import {
    Link,
    Route,
    Routes,
} from "react-router-dom";

import userDataContext from "context/userData";
import PersonalEditPage from "views/PersonalEdit";
import "./index.scss";

type propsType = Readonly<{
    PassSetRefreshToken: Dispatch<SetStateAction<string>>,
  }>;

export default function Personal(props: propsType): ReactElement {
    const {
        PassSetRefreshToken
    } = props;
    const userData = useContext(userDataContext);

    const personalInfo = (
        <div id="PersonalPage">
            <div className="twoSide">
                <div className="leftSide">
                    <img alt="avatar" src={userData?.avatar}/>
                    <div className="Name">
                        {userData?.name}
                    </div>
                    <div className="eMail">
                        {userData?.email}
                    </div>
                    <Link className="EditPerson" to="./editPerson">
                        <span className="material-symbols-outlined">edit</span>
                        <div>&nbsp;編輯個人資料</div>
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
                        <div className="OtherInfoTag">學號</div>
                        <div className="OtherInfoContent">{userData?.uid}</div>
                    </div>
                    <div className="IntroTag">自我介紹</div>
                    <div className="IntroContent">
                        <p dangerouslySetInnerHTML={{ __html: userData?.introduction || '' }}/>
                    </div>
                </div>
            </div>
        </div>
    )

    return (
        <Routes>
            <Route path="*" element={personalInfo}/>
            <Route path="/editPerson" element={<PersonalEditPage setRefreshToken={PassSetRefreshToken}/>}/>
        </Routes>
    )
}