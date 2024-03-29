

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
}>;

export const modules = {
  toolbar: {
    container: "#toolbar",
    handlers: {
      undo: undoChange,
      redo: redoChange
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
  "image",
  "color",
  "code-block"
]

export default function CourseBulletinEditor(props: propsType) : React.ReactElement {

  const {
      submitBulletin
  } = props;

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
        <button className="ql-image" />
      </span>
      <span className="submitButton" onClick={submitBulletin}>
        發布
      </span>

    </div>
  )
}