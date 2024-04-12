import React from 'react';
import { announcementData } from '../../api/announcementData';
import './index.scss';
import { GoTriangleLeft } from "react-icons/go";
import { GoTriangleRight } from "react-icons/go";
import { BsFillHouseFill } from "react-icons/bs";

export default function WebAnnouncementPage() {
  const { title, timestamp, photo,poster,content, documents ,previousTitle, nextTitle} = announcementData;

  return (
    <div className="web-announcement-container">
      <div className="breadcrumbs">
        <span><BsFillHouseFill /> / 網站公告 / 公告標題</span>
      </div>
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-detail">
        <div className="announcement-title"> 
            <p>置頂</p>
            {title}
        </div>
        <p className="announcement-timestamp">
        <img src={photo}/>
            {poster}
            {timestamp}
        </p>
        <p className="announcement-content">{content}</p>
        <div className="announcement-documents">
          {documents.map((doc, index) => (
            <a key={index} href={doc.link} className="document-link">
              {doc.name}
            </a>
          ))}
        </div>
        <div className="announcement-navigation">
          <p className="previous-title">
          <GoTriangleLeft />
          {previousTitle}
          </p>
          <p className="next-title">
            {nextTitle}
            <GoTriangleRight />
            </p>
        </div>
      </div>
    </div>
  );
}
