import React from "react";
import "./index.scss";

import { WebAnnouncementInfo } from "schemas/webAnnouncement";

import WebAnnouncement from "components/WebAnnouncement";
import PlatformFriendlyArea from "components/PlatformFriendlyArea";

type propsType = Readonly<{
    webAnnouncementList: Array<WebAnnouncementInfo>}>;

export default function landing(props: propsType): React.ReactElement {
    const {webAnnouncementList} = props;
    return (
        <div id="landPage">
            <div className="news">
                <div className='newsContent'>
                    News 113/2/6(二)9:00~17:00 Moodle平臺暫停服務
                </div>
            </div>

            <div className="description">
                <p>Short description <br/>pppppppp</p>
            </div>
            <div className="twoSide">
                <div className="leftSide">
                    <div className="identity">
                        <div className="IDoption">
                            <div className="Iam">
                                我是本校學生
                            </div>
                            <div className="operate">
                                操作教學說明
                            </div>
                        </div>
                        <div className="IDoption">
                            <div className="Iam">
                                我是教師
                            </div>
                            <div className="operate">
                                操作教學說明
                            </div>
                        </div>
                        <div className="IDoption">
                            <div className="Iam">
                                我是外校學生
                            </div>
                            <div className="operate">
                                操作教學說明
                            </div>
                        </div>
                    </div>
                    <div className="WebAnnoList">
                        <WebAnnouncement webAnnouncementList={webAnnouncementList} />
                    </div>
                </div>
                <div className="rightSide">
                    <PlatformFriendlyArea titleId="platform_friendly_area" />
                </div>
            </div>
            
        </div>
    )
}