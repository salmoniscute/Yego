import { ReactElement } from "react";

import WebAnnouncement from "components/WebAnnouncement";
import PlatformFriendlyArea from "components/PlatformFriendlyArea";

import "./index.scss";

export default function landing(): ReactElement {
    return (
        <div id="landPage">
            <div className="Content">
                <div className="KeyImage">
                    <img alt="landing" src="/assets/landing_image.png" />
                </div>
                <div className="slogan">
                    <img alt="landing" src="/assets/landing_slogan.png" />
                </div>
                <div className="identity">
                    <div className="IDoption">
                        <div className="Iam">
                            我是本校學生
                        </div>
                        <div className="operate">
                            登入說明
                        </div>
                    </div>
                    <div className="IDoption">
                        <div className="Iam">
                            我是教師
                        </div>
                        <div className="operate">
                            登入說明
                        </div>
                    </div>
                    <div className="IDoption">
                        <div className="Iam">
                            我是外校學生
                        </div>
                        <div className="operate">
                            登入說明
                        </div>
                    </div>
                </div>
                <div className="YegogoGreeting">
                    <img alt="greeting" src="/assets/landing_yegogo_greeting.png" />
                </div>
                <div className="WebAnnoList">
                    <WebAnnouncement />
                </div>

                <div className="platformFriendlyArea">
                    <PlatformFriendlyArea titleId="platform_friendly_area" />
                </div>
            </div>

        </div>
    )
}