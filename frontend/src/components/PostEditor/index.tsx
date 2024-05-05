import React, { Component, ReactElement, useState , useContext } from 'react';
import ReactQuill, { Quill } from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import userDataContext from "context/userData";
import "./index.scss";

import { Discussion , DiscussionTopic } from 'schemas/discussion';
import { Report } from 'schemas/report';

import { postDiscussion ,postDiscussionTopic} from 'api/discussion';
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
  parent_id : string
}>;

export default function PostEditor(props: propsType): ReactElement {
  const userData = useContext(userDataContext);
  // text editor
  const [content, setContent] = useState('');
  const [title , setTitle] = useState("");
  const [save , setSave] = useState(false);

  const {
    onClose,
    type,
    updatePost,
    parent_id
  } = props;

  const Close = () => {
    onClose();
    if (save === false){
      setContent("");
      setTitle("");
    }
  }

  const handleContentChange = (value:any, delta:any) => {
    setContent(value);
  };

  const onSubmit = async () =>{
    const nowTime = new Date().getTime();
    const uid = userData?.uid;
    const publisher = userData?.name;
    if (uid) {
      if (type === "discussion"){
        const discussion : Discussion ={
          release_time:nowTime,
          course_id: parent_id,
          title:title,
          content: content,
          follow:false,
          uid:uid
        };
        await postDiscussion(discussion);
        updatePost();
      }
      else if ( type === "report"){
        const report : Report = {
          uid : uid,
          release_time: nowTime,
          title:title,
          reply:0,
          content:content,
        }
        await postReport(report);
        updatePost();
      }
      else if ( type === "discussionTopic"){
        const discussionTopic : DiscussionTopic ={
          uid : uid,
          discussion_id: parent_id,
          release_time: nowTime,
          title:title,
          reply:0,
          follow:false,
          publisher : publisher || "",
          content:content,
        };
        await postDiscussionTopic(discussionTopic);
        updatePost();
      }
      
    }
    else {}
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
