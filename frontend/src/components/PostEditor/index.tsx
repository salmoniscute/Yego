import React, { Component, ReactElement, useState , useContext , useEffect } from 'react';
import ReactQuill, { Quill } from 'react-quill';
import { Link ,useParams} from "react-router-dom";
import 'react-quill/dist/quill.snow.css';
import userDataContext from "context/userData";
import "./index.scss";

import { Discussion , DiscussionTopic } from 'schemas/discussion';
import { Report } from 'schemas/report';

import { postDiscussion ,postDiscussionTopic , getDiscussionTopic , updateDiscussionTopic} from 'api/discussion';
import { postReport } from 'api/report';

import { RxCross2 } from "react-icons/rx";
import { CgExpand } from "react-icons/cg";

//自定義按鈕可參考以下：
// 定义自定义按钮组件，使用 Octicon
const CustomButton: React.FC = () => <span className="octicon octicon-star" />;

// // 插入星星的事件处理函数
// function insertStar(this: any) {
//   const cursorPosition = this.quill.getSelection().index;
//   this.quill.insertText(cursorPosition, "★");
//   this.quill.setSelection(cursorPosition + 1);
// }

const CustomToolbar: React.FC = () => (
  <div id="toolbar">
    <span className="ql-formats">
      <select className="ql-color">
        <option value="red" />
        <option value="green" />
        <option value="blue" />
        <option value="orange" />
        <option value="violet" />
        <option value="#d0d1d2" />
        <option selected />
      </select>
      <button className="ql-bold" />
      <button className="ql-italic" />
      <button className="ql-list" value="ordered" />
      <button className="ql-list" value="bullet" />
    </span>
    <span className="ql-formats">
      <button className="ql-link" />
      <button className="ql-image" />
    </span>
    <CustomButton />
  </div>
);
class Editor extends Component<{ placeholder?: string }, { editorHtml: string }> {
  // constructor(props: { placeholder?: string }) {
  //   super(props);
  //   this.state = { editorHtml: "" };
  //   this.handleChange = this.handleChange.bind(this);
  // }

  // handleChange(html: string) {
  //   this.setState({ editorHtml: html });
  // }

  static modules = {
    toolbar: {
      container: "#toolbar",
      handlers: {
        //insertStar: insertStar
      }
    },
    clipboard: {
      matchVisual: false,
    }
  };

  static formats = [
    "header",
    "font",
    "size",
    "bold",
    "italic",
    "underline",
    "strike",
    "blockquote",
    "list",
    "bullet",
    "indent",
    "link",
    "image",
    "color"
  ];

}

type propsType = Readonly<{
  onClose : () => void,
  type : string
  updatePost:() => void,
  parent_id : number,
  isEditing : boolean,
}>;

export default function PostEditor(props: propsType): ReactElement {
  const params = useParams();
  const userData = useContext(userDataContext);
  const [discussionTopic , setDiscussionTopic] = useState<DiscussionTopic>();
  // text editor
  const [content, setContent] = useState('');
  const [title , setTitle] = useState("");
  const [save , setSave] = useState(false);

  const {
    onClose,
    type,
    updatePost,
    parent_id,
    isEditing
  } = props;

  const Close = () => {
    onClose();
    if (save === false){
      setContent("");
      setTitle("");
    }
  }

  useEffect(() => {
      if (isEditing){
        if (type == "discussionTopic"){
          getDiscussionTopic(Number(params.discussionTopicId) || 0).then( data =>{
            setDiscussionTopic(data);
            if (discussionTopic){
              setTitle(discussionTopic.title);
              setContent(discussionTopic.content);
            }
          });
        }
      }
  }, [])

  const handleContentChange = (value:any, delta:any) => {
    setContent(value);
  };

  const onSubmit = async () =>{
    const uid = userData?.uid;
    const publisher = userData?.name;

    if (!isEditing){
      if (uid) {
        if (type === "discussion"){
          const discussion : Discussion ={
            course_id: parent_id,
            title:title,
            content: content,
            subscription_status:false,
            uid:uid
          };
          await postDiscussion(discussion);
          updatePost();
        }
        else if ( type === "report"){
          const report : Report = {
            uid : uid,
            title:title,
            reply_number:0,
            content:content,
            publisher : publisher || "",
            publisher_avatar : ""
          }
          await postReport(report);
          updatePost();
        }
        else if ( type === "discussionTopic"){
          const discussionTopic : DiscussionTopic ={
            uid : uid,
            discussion_id: parent_id,
            title:title,
            reply_number:0,
            subscription_status:false,
            publisher : publisher || "",
            content:content,
            publisher_avatar : ""
          };
          await postDiscussionTopic(discussionTopic);
          updatePost();
        }
      }
      else {}
    }
    else{
      if (uid){
        if (type == "discussionTopic" && discussionTopic){
          discussionTopic.title = title;
          discussionTopic.content = content;
          await updateDiscussionTopic(discussionTopic);
          updatePost();
        }
      }
    }    
    Close();
    setContent("");
    setTitle("");
  } 

  const Save = async () => {
    setSave(true);
  }
 
  
  return <>
    <div className='window'>
      <div id="postEditor">
        <button className='btn expand-btn'><CgExpand /></button>
        <button className='btn close-btn' onClick={Close}><RxCross2 /></button>
        <div className="text-editor">
          <input type="text" placeholder='標題｜少於20字' className='title' value={title}
                onChange={(e) => setTitle(e.target.value)} />
          <ReactQuill
            placeholder='內文｜'
            modules={Editor.modules}
            formats={Editor.formats}
            value={content}
            onChange={handleContentChange}
            theme={"snow"} // 设置为 "snow" 使用默认主题
          />
          <CustomToolbar />
          <div className='bottom'>
            <button className='save' onClick={Save}>存檔</button>
            <button className='post' onClick={onSubmit}>發布</button>
          </div>
        </div>
      </div>
    </div>
  </>
}
