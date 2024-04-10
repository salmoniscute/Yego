import React, { Component, ReactElement, useState , useContext } from 'react';
import ReactQuill, { Quill } from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import userDataContext from "context/userData";
import "./index.scss";

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
  constructor(props: { placeholder?: string }) {
    super(props);
    this.state = { editorHtml: "" };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(html: string) {
    this.setState({ editorHtml: html });
  }

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
  onClose : Function,
  type : string
}>;

export default function PostEditor(props: propsType): ReactElement {
  const userData = useContext(userDataContext);
  const {
    onClose,
    type
  } = props;
  const Close = () => {
    onClose();
  }
  // text editor
  const [content, setContent] = useState('');
  const [title , setTitle] = useState("");

  const handleContentChange = (value:any, delta:any) => {
    setContent(value);
  };

  const onSubmit = async () =>{
    const nowTime = new Date().getTime();
    const uid = userData?.uid;
    if (uid) {
      if (type === "discussion"){

      }
      else if ( type === "report"){
  
      }
      else if ( type === "discussionTopic"){
        
      }
      
    }
    else {}
    setContent("");
    setTitle("");
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
            <button className='save'>存檔</button>
            <button className='post'>發布</button>
          </div>
        </div>
      </div>
    </div>
  </>
}
