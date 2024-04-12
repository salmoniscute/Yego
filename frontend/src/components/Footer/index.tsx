import React from "react";

import logo from "../../logo.svg"

import "./index.scss";

export default function Footer(): React.ReactElement {
    return (
        <div id="footer">
            <div className="leftFooter">
                <h2>YEGO 成功大學數位學習平台</h2>
                <p>國立成功大學 版權所有</p>
                <p>Copyright © National Cheng Kung University all rights reserved</p>
            </div>
            <div className="rightFooter">
                <p>網站連結</p>
                <div><a href=''>課程資訊與選課系統</a></div>
                <div><a href=''>學籍＆成績查詢</a></div>
            </div>
            <div className="rightFooter">
                <p>幫助</p>
                <div><a href=''>教學手冊</a></div>
                <div><a href=''>常見問題</a></div>
                <div><a href=''>問題回報</a></div>
            </div>
            <div className="rightFooter">
                <p>國立成功大學計算機與網路中心</p>
                <div>
                    <a href = 'http://cc.ncku.edu.tw/'>• http://cc.ncku.edu.tw/</a>
                    <p>• sfkuo@ncku.edu.tw</p>
                    <p>• (06)275-7575#61056</p>
                </div>
            </div>
        </div>
    );
}
