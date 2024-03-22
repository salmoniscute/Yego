import { ReactElement, useEffect, useState } from "react";
import announcements from "../../api/announcements.json";
import "./index.scss";
import { GoTriangleLeft } from "react-icons/go";
import { GoTriangleRight } from "react-icons/go";

interface Announcement {
    title: string;
    content: string;
    poster: string;
    date: string;
    photo: string;
}

export default function WebAnnouncementPage(): ReactElement {
    const [data, setData] = useState<Announcement[]>([]);

    useEffect(() => {
        setData(announcements);
    }, []);

    return (
        <div className="container">
            <div className="title">
                <h1>網站公告</h1>
            </div>
            <div className="announcementtitle">
                {data.map((announcement, index) => (
                    <div key={index} className="announcement">
                        <h2>{announcement.title}</h2>
                    </div>
                ))}
            </div>
            <div className="posterinformation">
                {data.map((announcement, index) => (
                    <div key={index} className="announcement">
                        <img src={announcement.photo} />
                        <p>{announcement.poster}</p>
                    </div>
                ))}
            <div className="date">
                {data.map((announcement, index) => (
                    <div key={index} className="announcement">
                        <p>{announcement.date}</p>
                    </div>
                ))}
            </div>

            </div>
            <div className="announcement-list">
                {data.map((announcement, index) => (
                    <div key={index} className="announcement">
                        <p>{announcement.content}</p>
                    </div>
                ))}
            </div>
            <div className="switchpages">
                <div className="previouspage">
                <GoTriangleLeft />
                <a href="">上一篇標題</a> 
                </div>
                <div className="nextpage">
                <a href="">下一篇標題</a> 
                <GoTriangleRight />
                </div>
            </div>
        </div>
    );
}
