
import React, { useState, useEffect } from 'react';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { Link } from 'react-router-dom';


export default function WebAnnouncementList() {
  const [announcementData, setAnnouncementData] = useState<any[]>([]);

  useEffect( () => {
    fetch("http://localhost:8080/api/website/bulletin/all")
    .then(res=>{
      return res.json();
    })
    .then(data =>{
      setAnnouncementData(data);
    })
    .catch(error => {
      console.error('Error fetching announcement data:', error);
    });

  }, []);
  if (!announcementData) {
    return <div>Loading...</div>;
  }

 return (
    <div className="web-announcement-container">
    <div className="breadcrumbs">
      <span><Link to="/" ><BsFillHouseFill /></Link> / <Link to="/webAnnouncementlist" >網站公告</Link> </span>
    </div>
    <div className="web-announcement-header">
      <h1>網站公告</h1>
    </div>
    <div className="announcement-list">
      <div className="list-header">
        <span style={{width:"50%"}}>標題</span>
        <span style={{width:"30%"}}>發布日期</span>
        <span style={{width:"20%"}}>發布者</span>
      </div>
      {announcementData.map((announcement, index) => (
        <div className="list-item" key={index}>
          <span style={{width:"50%"}}>{announcement.title}</span>
          <span style={{width:"30%"}}>{announcement.release_time}</span>
          <span style={{width:"20%"}}>{announcement.uid}</span>
        </div>
      ))}

    </div>
   
      </div>

    
     )
  }
  