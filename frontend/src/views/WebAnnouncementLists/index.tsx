import React, { useState, useEffect } from 'react';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { Link } from 'react-router-dom';

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
  const weekDay = date.toLocaleDateString('zh-CN', { weekday: 'short' });
  const hours = date.getHours().toString().padStart(2, '0');
  const minutes = date.getMinutes().toString().padStart(2, '0');

  return `${year}年${month}月${day}日(${weekDay}) ${hours}:${minutes}`;
};

export default function WebAnnouncementList() {
  const [announcementData, setAnnouncementData] = useState<Info[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8080/api/website/bulletins", {
      method: 'GET',
      headers: {
        'accept': 'application/json'
      }
    })
      .then(res => {
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then(data => {
        if (Array.isArray(data)) {
          setAnnouncementData(data);
        } else {
          console.error('Fetched data is not an array:', data);
        }
      })
      .catch(error => {
        console.error('Error fetching announcement data:', error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="web-announcement-container">
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-list">
        <div className="list-header">
          <span style={{ width: "50%" }}>標題</span>
          <span style={{ width: "30%" }}>發布日期</span>
          <span style={{ width: "20%" }}>發布者</span>
        </div>
        {announcementData.map((announcement, index) => (
          <div className="list-item" key={index}>
            <span style={{ width: "50%" }}><Link to={`/webAnnouncement/${announcement.id}`} className="announcement-title">{announcement.title}</Link></span>
            <span style={{ width: "30%" }}>{formatDateTime(announcement.release_time)}</span>
            <span style={{ width: "20%" }}>{announcement.publisher}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
