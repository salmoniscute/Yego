import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { AiFillCaretLeft, AiFillCaretRight } from "react-icons/ai";

interface Document {
  path: string;
  name: string;
}

interface Info {
  id: number;
  pin_to_top: boolean;
  title: string;
  photo: string;
  publisher: string;
  release_time: string;
  content: string;
  files: Document[];
}
const MAX_ID = 10;

export default function WebAnnouncementPage() {
  const { id } = useParams<{ id: string }>();
  const [announcementData, setAnnouncementData] = useState<Info | null>(null);

  useEffect(() => {
    fetch(`http://localhost:8080/api/website/bulletin/${id}`)
      .then(res => res.json())
      .then(data => {
        setAnnouncementData(data);
      })
      .catch(error => {
        console.error('Error fetching announcement data:', error);
      });
  }, [id]);

  if (!announcementData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="web-announcement-container">
      <div className="breadcrumbs">
        <span>
          <Link to="/" ><BsFillHouseFill /></Link> / 
          <Link to="/webAnnouncementlist">網站公告</Link> / 
          {announcementData.title}
        </span>
      </div>
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-detail">
        <div key={announcementData.id} className="announcement-item">
          <div className="announcement-title">
            <p>{announcementData.pin_to_top ? '置頂' : null}</p>
            {announcementData.title}
          </div>
          <p className="announcement-timestamp">
            <img src={announcementData.photo} alt="announcement" />
            {announcementData.publisher}
            {announcementData.release_time}
          </p>
          <p className="announcement-content">{announcementData.content}</p>
          <div className="announcement-documents">
            {announcementData.files.map((doc, index) => (
              <a key={index} href={doc.path} className="document-link">
                {doc.name}
              </a>
            ))}
          </div>
        </div>
      </div>
      <div className="announcement-navigation">
      {parseInt(id || '') > 0 && (
        <Link to={`/webAnnouncement/${parseInt(id || '') - 1}`}>
          <AiFillCaretLeft /> 上一篇標題
        </Link>
      )}
      {parseInt(id || '') < MAX_ID && (
        <Link to={`/webAnnouncement/${parseInt(id || '') + 1}`}>
          下一篇標題 <AiFillCaretRight />
        </Link>
      )}
    </div>
    </div>
  );
}
