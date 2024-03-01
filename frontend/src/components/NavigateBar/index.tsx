import React ,{useState} from "react";
import { Link } from "react-router-dom";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCaretUp,faCaretDown,faGlobe } from "@fortawesome/free-solid-svg-icons";

import "./index.scss";

export default function NavigateBar(): React.ReactElement {
    const [openStatus, setOpenStatus] = useState<boolean>(false);
    const [language, setLanguage] = useState<string>("正體中文");
    return (
        <div id="navigateBar">
            <div className="leftLogo">
                <p>Yego</p>
            </div>
            <div className="rightButton">
                <div className="dropdownMenu" onClick={() => {setOpenStatus(!openStatus)}}>
                    <FontAwesomeIcon icon={faGlobe} className="icon"/>
                    <div>{language}</div>
                    {openStatus ? <FontAwesomeIcon icon={faCaretUp} className="icon"/> : <FontAwesomeIcon icon={faCaretDown} className="icon"/>}
                    {openStatus && (
                        <div className="dropdownContent">
                            {language === "正體中文" ? (
                                <div onClick={() => {
                                    setLanguage("English");
                                }}>English</div>
                            ) : (
                                <div onClick={() => {
                                    setLanguage("正體中文");
                                }}>正體中文</div>
                            )}
                        </div>
                    )}
                </div>
                
                <Link className="loginButton" to={"/"} >登入</Link>
            </div>
        </div>
    );
}
