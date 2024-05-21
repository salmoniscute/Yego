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
      <div className="breadcrumbs">
        <span><Link to="/"><BsFillHouseFill /></Link> / <Link to="/webAnnouncementlist">網站公告</Link></span>
      </div>
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
            <span style={{ width: "30%" }}>{announcement.release_time}</span>
            <span style={{ width: "20%" }}>{announcement.publisher}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
