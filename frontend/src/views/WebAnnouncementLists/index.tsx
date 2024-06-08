import { useState, useEffect } from 'react';
import './index.scss';
import { Link } from 'react-router-dom';
import axios from "axios";

interface Info {
  id: number;
  pin_to_top: boolean;
  title: string;
  publisher: string;
  release_time: string;
}

const formatDateTime = (dateTimeString: string) => {
  const date = new Date(dateTimeString);
  const year = date.getFullYear();
  const month = (date.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始，因此要加1
  const day = date.getDate().toString().padStart(2, '0');

  return `${year}年${month}月${day}日`;
};

export default function WebAnnouncementList() {
  const [announcementData, setAnnouncementData] = useState<Info[]>([]);


  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/website/bulletins");
        setAnnouncementData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="web-announcement-container">
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-list">
        <div className="list-header">
          <span style={{ width: "7%" }}></span>
          <span style={{ width: "45%" }}>標題</span>
          <span style={{ width: "30%" }}>發布日期</span>
          <span style={{ width: "20%" }}>發布者</span>
        </div>
        {announcementData.sort((a, b) => {
          if (a.pin_to_top && b.pin_to_top)
            return 0;
          return a.pin_to_top ? -1 : 1;
        }).map((announcement, index) => (
          <div className="list-item" key={index}>
            <div className="pin caption-bold" style={{ width: "5%" }} data-pin={announcement.pin_to_top} >{announcement.pin_to_top ? "置頂" : ""}</div>
            <span style={{ width: "45%" }}><Link to={`/webAnnouncement/${announcement.id}`} className="announcement-title">{announcement.title}</Link></span>
            <span style={{ width: "30%" }}>{formatDateTime(announcement.release_time)}</span>
            <span style={{ width: "20%" }}>{announcement.publisher}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
