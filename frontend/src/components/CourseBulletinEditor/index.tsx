
import {
  useEffect,
  useState,
} from "react";
import axios from 'axios';
import "./index.scss";

const CustomUndo = () => (
  <svg viewBox="0 0 18 18">
    <polygon className="ql-fill ql-stroke" points="6 10 4 12 2 10 6 10" />
    <path
      className="ql-stroke"
      d="M8.09,13.91A4.6,4.6,0,0,0,9,14,5,5,0,1,0,4,9"
    />
  </svg>
)

const CustomRedo = () => (
  <svg viewBox="0 0 18 18">
    <polygon className="ql-fill ql-stroke" points="12 10 14 12 16 10 12 10" />
    <path
      className="ql-stroke"
      d="M9.91,13.91A4.6,4.6,0,0,1,9,14a5,5,0,1,1,5-5"
    />
  </svg>
)

function undoChange() {
  //this.quill.history.undo()
}

function redoChange() {
  //this.quill.history.undo()
}

type propsType = Readonly<{
  submitBulletin:()=>void;
  imageUpload : () => void;
}>;





export const modules = {
  toolbar: {
    container: "#toolbar",
    handlers: {
      undo: undoChange,
      redo: redoChange,
    }
  },
  history: {
    delay: 500,
    maxStack: 100,
    userOnly: true
  }
}

// 每新增或移除 Quill Editor 內建的工具，記得要在 formats 做相應的調整
export const formats = [
  "header",
  "bold",
  "italic",
  "underline",
  "align",
  "strike",
  "background",
  "list",
  "bullet",
  "link",
  "color",
  "code-block"
]

export default function CourseBulletinEditor(props: propsType) : React.ReactElement {

  const {
      submitBulletin,
      imageUpload
  } = props;
  const [image, setImage] = useState<File | null>(null);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const selectedImage = event.target.files?.[0];
    if (selectedImage) {
      setImage(selectedImage);
      console.log(selectedImage);
    }
  };

  const handleUpload = async() => {
    if (!image) {
      alert("Please select an image.");
      return;
    }
    const formData = new FormData();
    formData.append("files", image);
    try {
      const response = await axios.post('http://localhost:8080/api/file?component_id=1', formData, {
      });

      console.log('Image uploaded successfully:', response.data);
    } catch (error) {
        console.error('Error uploading the image:', error);
    }
    
  };

  return (
    <div id="toolbar">
      <span className="ql-formats">
        <button className="ql-undo">
          <CustomUndo />
        </button>
        <button className="ql-redo">
          <CustomRedo />
        </button>
      </span>
      <span className="ql-formats">
        <button className="ql-bold" />
        <button className="ql-italic" />
        <button className="ql-underline" />
      </span>
      <span className="ql-formats">
        <select className="ql-align" />
        <select className="ql-color"></select>
        <select className="ql-background" />
      </span>
      <span className="ql-formats">
        <button className="ql-list" value="ordered" />
        <button className="ql-list" value="bullet" />
      </span>
      <span className="ql-formats">
        <button className="ql-link" />
      </span>
      <span className="submitButton" onClick={submitBulletin}>
        發布
      </span>
      <label htmlFor="file-input">
        <input
          type="file"
          id="file-input"
          accept="image/*"
          onChange={handleImageUpload}
        />
        <span className="submitButton">
          上傳圖片
        </span>
      </label>
      

    </div>
  )
}