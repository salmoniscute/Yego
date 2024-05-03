import React from 'react';
import {useState,useEffect} from "react";
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { AiFillCaretLeft } from "react-icons/ai";
import { AiFillCaretRight } from "react-icons/ai";
import { Link } from 'react-router-dom';

interface Document {
  path: string;
  name: string;
}

export default function WebAnnouncementPage() {
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
        <span> <Link to="/" ><BsFillHouseFill /></Link> / <Link to="/webAnnouncementlist" >網站公告</Link> / 公告標題</span>
      </div>
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-detail">
        {announcementData.map(announcement => (
          <div key={announcement.id} className="announcement-item">
            <div className="announcement-title"> 
              <p>{announcement.pin_to_top ? '置頂' : null}</p>
              {announcement.title}
            </div>
            <p className="announcement-timestamp">
              <img src={announcement.photo} alt="announcement"/>
              {announcement.uid}
              {announcement.release_time}
            </p>
            <p className="announcement-content">{announcement.content}</p>
            <div className="announcement-documents">
                <p>檔案一.pdf</p>
                <p>檔案二.pdf</p>
            </div>
          </div>
        ))}
      </div>
      <div className="announcement-navigation">
              <AiFillCaretLeft />
               上一篇標題                         
               下一篇標題
               <AiFillCaretRight />
            </div>
    </div>
  );


  /* {announcement.files.map((doc: Document, index: number) => (
    <a key={index} href={doc.path} className="document-link">
      {doc.name}
    </a> 
     ))} */
}