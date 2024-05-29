import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import './index.scss';
import { BsFillHouseFill } from "react-icons/bs";
import { AiFillCaretLeft, AiFillCaretRight } from "react-icons/ai";

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
  const [announcementData, setAnnouncementData] = useState<Info | null>(null);
  const [allIds, setAllIds] = useState<number[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnnouncementData = async () => {
      try {
        const response = await fetch(`http://localhost:8080/api/website/bulletin/${id}`);
        const data = await response.json();
        console.log("Fetched announcement data:", data);
        setAnnouncementData(data);
      } catch (error) {
        console.error('Error fetching announcement data:', error);
      } finally {
        setLoading(false);
      }
    };

    const fetchAllIds = async () => {
      try {
        const response = await fetch('http://localhost:8080/api/website/bulletins');
        const data = await response.json();
        console.log("Fetched all IDs:", data);
        const ids = data.map((announcement: { id: number }) => announcement.id);
        setAllIds(ids);
      } catch (error) {
        console.error('Error fetching all IDs:', error);
      }
    };

    fetchAnnouncementData();
    fetchAllIds();
  }, [id]);

  if (loading || !announcementData) {
    return <div>Loading...</div>;
  }

  const currentId = parseInt(id || '', 10);
  const currentIndex = allIds.indexOf(currentId);
  const prevId = allIds[currentIndex - 1];
  const nextId = allIds[currentIndex + 1];
  const publisherAvatarUrl = `http://localhost:8080${announcementData.publisher_avatar}`;

  console.log('Current ID:', currentId);
  console.log('Current Index:', currentIndex);
  console.log('Previous ID:', prevId);
  console.log('Next ID:', nextId);

  return (
    <div className="web-announcement-container">
      <div className="breadcrumbs">
        <span>
          <Link to="/"><BsFillHouseFill /></Link> /
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
            <img src={publisherAvatarUrl} alt="announcement" />
            {announcementData.publisher}
            {announcementData.release_time}
          </p>
          <p className="announcement-content">{announcementData.content}</p>
          <div className="announcement-documents">
            {announcementData.files.map((doc, index) => (
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
