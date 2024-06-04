import {
    ReactElement,
    useContext,
    useState,
    useEffect
} from "react";

import {
    Link,
    Route,
    Routes,
} from "react-router-dom";

import userDataContext from "context/userData";
import { User } from "schemas/user";
import {getPersonal} from "api/personal";
import PersonalEditPage from "views/PersonalEdit";
import "./index.scss";

export default function Personal(): ReactElement {
    const userData = useContext(userDataContext);
    const [personalData, setPersonalData] = useState<User>();

    useEffect(() => {
        console.log("update");
        getPersonal(userData?.uid?? "").then(data => {
            setPersonalData(data);
        });
    }, [])

    const personalInfo = (
        <div id="PersonalPage">
            <div className="twoSide">
                <div className="leftSide">
                    <img alt="avatar" src={personalData?.avatar}/>
                    <div className="Name">
                        {personalData?.name}
                    </div>
                    <div className="eMail">
                        {personalData?.email}
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
                        <p dangerouslySetInnerHTML={{ __html: personalData?.introduction || '' }}/>
                    </div>
                </div>
            </div>
        </div>
    )

    return (
        <Routes>
            <Route path="*" element={personalInfo}/>
            <Route path="/editPerson" element={<PersonalEditPage/>}/>
        </Routes>
    )
}