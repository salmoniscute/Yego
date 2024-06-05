import {
    ReactElement,
    useContext,
    useState,
    useEffect
} from "react";
import { useNavigate } from 'react-router-dom';
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import userDataContext from "context/userData";
import {getPersonal, updatePersonal} from "api/personal";
import {refreshToken} from 'api/login';
import { User } from "schemas/user";
import "./index.scss";
import { get } from "http";

// Undo & Redo icon
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

let quillEditor: any;
function undoChange() {
    quillEditor?.history.undo()
}
  
function redoChange() {
    quillEditor?.history.redo();
}

// Modules for Quill Editor
const modules = {
    toolbar: {
      container: "#toolbar",
      handlers: {
        undo: undoChange,
        redo: redoChange
      }
    },
    history: {
      delay: 1000,
      maxStack: 100,
      userOnly: true
    }
  }
  
// 每新增或移除 Quill Editor 內建的工具，記得要在 formats 做相應的調整
const formats = [
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
]

function PersonalIntroEditor() : React.ReactElement {

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
      </div>
    )
  }

  
export default function PersonalEdit(): ReactElement {
    const userData = useContext(userDataContext);
    const [personalData, setPersonalData] = useState<User>();
    const navigate = useNavigate();
    
    const [user, setUser] = useState({
      name: "",
      email: "",
    });


    useEffect(() => {
      const fetchPersonal = async() => { 
        const data = await getPersonal(userData?.uid?? "");
        setPersonalData(data);
        setUser({
          name: data.name,
          email: data.email
        });
        setIntro(data.introduction)
      }
      fetchPersonal();
    }, [])

    const handleChange = (e:any) => {
        const { name, value } = e.target;
        setUser({
            ...user,
            [name]: value
        });
    };
    // text editor
    const [intro, setIntro] = useState("");
    const handleIntroChange = (value:any, delta:any) => {
        setIntro(value);
    };

    const OnSubmit = async() => {
      if (!user.name || !user.email) {
        alert("Name and email cannot be empty.");
        return;
      }
      else {
        if (personalData) {
          personalData.name = user.name;
          personalData.email = user.email;
          personalData.introduction = intro ?? "";
          await updatePersonal(personalData);
          await refreshToken();
          navigate(`/personal/${userData?.uid}`);
          window.location.reload()
        }
      }
    }

    return (
        <div id="PersonalEditPage">
              <div className="twoSide">
                  <div className="leftSide">
                      <img alt="avatar" src={personalData?.avatar}/>
                      <div className="Name">
                          <input
                              className="NameInput"
                              type="text"
                              name='name' 
                              value={user.name}
                              onChange={handleChange}
                              maxLength={20}
                              placeholder="學生姓名"
                          />
                      </div>
                      <div className="EditPerson"  onClick={OnSubmit}>
                          <div>&nbsp;結束編輯</div>
                      </div>

                  </div>
                  <div className="rightSide">
                      <div className="OtherInfo">
                          <div className="OtherInfoTag" >國家</div>
                          <div className="OtherInfoContent">
                              {userData?.country}
                          </div>
                      </div>
                      <div className="OtherInfo">
                          <div className="OtherInfoTag">科系</div>
                          <div className="OtherInfoContent">{userData?.department}</div>
                      </div>
                      <div className="OtherInfo">
                          <div className="OtherInfoTag">信箱</div>
                          <div className="OtherInfoContent">
                              <input
                                  className="InfoInput"
                                  type="email"
                                  name='email' 
                                  value={user.email}
                                  onChange={handleChange}
                                  required
                                  placeholder="學生信箱"
                              />
                          </div>
                      </div>
                      <div className="IntroTag">自我介紹</div>
                      <div className="IntroContent">
                        <ReactQuill
                            theme="snow"
                            placeholder="請輸入自我介紹..."
                            modules={modules}
                            value={intro}
                            onChange={handleIntroChange}
                            formats={formats}
                            ref={(el) => {
                                if (el) quillEditor = el.getEditor();
                              }}
                        />
                        <PersonalIntroEditor />
                      </div>
                  </div>
              </div>
        </div>
    )
}