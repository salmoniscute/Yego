import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { AiFillCaretLeft, AiFillCaretRight } from "react-icons/ai";
import axios from 'axios';

interface Document {
  id: number;
  path: string;
  name?: string;
}

interface Info {
  id: number;
  pin_to_top: boolean;
  title: string;
  publisher_avatar: string;
  publisher: string;
  release_time: string;
  content: string;
  files: Document[];
}

export default function WebAnnouncementPage() {
  const { id } = useParams<{ id: string }>();
  const [announcementData, setAnnouncementData] = useState<Info>();
  const [allIds, setAllIds] = useState<number[]>([]);

  useEffect(() => {
    const fetchAnnouncementData = async () => {
      try {
        const response = await axios.get(`/website/bulletin/${id}`);
        console.log("Fetched announcement data:", response.data);
        setAnnouncementData(response.data);
      } catch (error) {
        console.error('Error fetching announcement data:', error);
      } finally {
      }
    };

    const fetchAllIds = async () => {
      try {
        const response = await axios.get('/website/bulletins');
        const ids = response.data.map((announcement: { id: number }) => announcement.id);
        setAllIds(ids);
      } catch (error) {
        console.error('Error fetching all IDs:', error);
      }
    };

    fetchAnnouncementData();
    fetchAllIds();
  }, [id]);

  const formatDateTime = (dateTimeString: string) => {
    const date = new Date(dateTimeString);
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0'); 
    const day = date.getDate().toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');

    return `${year}年${month}月${day}日 ${hours}:${minutes}`;
  };


  const currentId = parseInt(id || '', 10);
  const currentIndex = allIds.indexOf(currentId);
  const prevId = allIds[currentIndex - 1];
  const nextId = allIds[currentIndex + 1];
  const publisherAvatarUrl = announcementData?.publisher_avatar || "";

  console.log('Current ID:', currentId);
  console.log('Current Index:', currentIndex);
  console.log('Previous ID:', prevId);
  console.log('Next ID:', nextId);

  return (
    <div className="web-announcement-container">
      <div className="web-announcement-header">
        <h1>網站公告</h1>
      </div>
      <div className="announcement-detail">
        <div key={announcementData?.id} className="announcement-item">
          <div className="announcement-title">
            {announcementData?.pin_to_top && <p>置頂</p>}
            {announcementData?.title}
          </div>
          <div className="announcement-timestamp">
            <img src={publisherAvatarUrl} alt="announcement" />
            <p className='title'>{announcementData?.publisher}</p>
            <p className='time'>{formatDateTime(announcementData?.release_time || "")}</p>
          </div>
          <div
              className="announcement-content"
              dangerouslySetInnerHTML={{ __html: announcementData?.content || "" }}
          />     
          <div className="announcement-documents">
            {announcementData?.files.map((doc, index) => (
              <a key={index} href={`http://localhost:8080${doc.path}`} className="document-link">
                {doc.name || `Document ${index + 1}`}
              </a>
            ))}
          </div>
        </div>
      </div>
      <div className="announcement-navigation">
        {prevId && (
          <Link to={`/webAnnouncement/${prevId}`}>
            <AiFillCaretLeft /> 上一篇標題
          </Link>
        )}
        {nextId && (
          <Link to={`/webAnnouncement/${nextId}`}>
            下一篇標題 <AiFillCaretRight />
          </Link>
        )}
      </div>
    </div>
  );
}
