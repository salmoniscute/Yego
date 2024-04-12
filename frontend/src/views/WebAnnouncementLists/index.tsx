
import React, { useState, useEffect } from 'react';
import { listData } from '../../api/announcelistData';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { ListItem } from  "../../schemas/weblist";



export default function WebAnnouncementList() {
    const [announcements, setAnnouncements] = useState<ListItem[]>([]);
   
  useEffect(() => {
    const fetchListData = async () => {
      try {
        const data = await listData(); 
        setAnnouncements(data); 
      } catch (error) {
        console.error("Fetching list data failed", error);
      }
    };
    fetchListData(); 
  }, []); 


 return (
    <div className="web-announcement-container">
    <div className="breadcrumbs">
      <span><BsFillHouseFill /> 網站公告</span>
    </div>
    <div className="web-announcement-header">
      <h1>網站公告</h1>
    </div>
    <div className="announcement-list">
      <div className="list-header">
        <span>標題</span>
        <span>發布日期</span>
        <span>發布者</span>
      </div>
      {announcements.map((announcement, index) => (
        <div className="list-item" key={index}>
          <span>{announcement.title}</span>
          <span>{announcement.creationDate}</span>
          <span>{announcement.poster}</span>
        </div>
      ))}
    </div>
   
      </div>

    
     )
  }
  