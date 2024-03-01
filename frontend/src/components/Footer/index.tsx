import React from "react";

import logo from "../../logo.svg"

import "./index.scss";

export default function Footer(): React.ReactElement {
    return (
        <div id="footer">
            <div className="leftFooter">
                <h6>YEGO 成功大學數位學習平台</h6>
                <p>國立成功大學 版權所有</p>
                <p>Copyright © National Cheng Kung University all rights reserved</p>
            </div>
            <div className="rightFooter">
                <p>聯絡資訊</p>
                <div>
                    <a href = 'http://cc.ncku.edu.tw/'>• http://cc.ncku.edu.tw/</a>
                    <p>• sfkuo@ncku.edu.tw</p>
                    <p>• (06)275-7575#61056</p>
                </div>
            </div>
        </div>
    );
}
