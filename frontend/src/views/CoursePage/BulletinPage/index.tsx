import {
    useEffect,
    useState,
    useContext,
    CSSProperties,
} from "react";
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import CourseBulletinEditor , {modules,formats} from "components/CourseBulletinEditor";
import userDataContext from "context/userData";
import "./index.scss";
import { SlOptions } from "react-icons/sl";

import { CourseBulletinInfo } from "schemas/courseBulletin";
import { getCourseBulletinList,postCourseBulletin } from "api/courseBulletin";

const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{
    courseID: string
}>;

export default function BulletinPage(props: propsType): React.ReactElement {
    const {
        courseID
    } = props;
    const userData = useContext(userDataContext);
    const [courseBulletinList, setCourseBulletin] = useState<Array<CourseBulletinInfo>>([]);
    // text editor
    const [content, setContent] = useState('');
    const [title , setTitle] = useState("");

    useEffect(() => {
        getCourseBulletinList().then(data => {
            setCourseBulletin(data);
        }).catch( error =>{
            if (error.response && error.response.status === 404) {
                
            } else {
                
            }
        });
    }, []);

    const handleContentChange = (value:string, delta:any) => {
        setContent(value);
    };

    const onSubmit = async () =>{
        const nowTime = new Date().getTime();
        const uid = userData?.uid;
        if (uid) {
            const courseBulletin = await postCourseBulletin(uid, "CSE101", title, nowTime, content, false);
            console.log(courseBulletin);
        }
        else {}
        setContent("");
        setTitle("");
        getCourseBulletinList().then(data => {
            setCourseBulletin(data);
        });
    }

    const deleteBulletin = async(id:string) =>{
        console.log("hihi"+id);
    }

    const pinBulletin = async(id:string) =>{
        console.log("hi"+id);
    }

    type Option = {
        label: string;
        action: (() => void) | undefined;
    };
    
    const editOptions = (id: string): Option[] => [
        { label: "編輯" ,action:() => deleteBulletin(id)},
        { label: "刪除", action: () => deleteBulletin(id) },
        { label: "置頂", action: () => pinBulletin(id) }
    ];

    return (
        <div id="courseBulletinPage">
            { userData?.role == "student" && <p>課程公告</p>}
            <textarea
                placeholder="輸入公告標題"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                rows={1}
            >

            </textarea>
            <ReactQuill
                theme="snow"
                placeholder="發文..."
                modules={modules}
                value={content}
                onChange={handleContentChange}
                formats={formats}
            />
            <CourseBulletinEditor submitBulletin={onSubmit}/>
            { courseBulletinList.length == 0 && <p>尚無公告</p>}
            <div className="courseBulletin">
                {
                    courseBulletinList.map((data , i) =>
                        <div className="courseBulletinContent" key={i}>
                            <div className="cbContent">
                                <div>
                                    { data.pin_to_top === true && <div className="cbPin">置頂</div>}
                                    <img src={UserIcon} />
                                    <p className="cbAuther">{data.publisher}</p>
                                    <p className="cbTime">{data.release_time}</p>
                                </div>
                                { data.uid === userData?.uid && <label className="dropdownMenu">
                                    <SlOptions/>
                                    <input type="checkbox" />
                                    <div className="mask" style={{ "--length": 3 } as CSSProperties}>
                                        <div className="content body-bold">
                                            {
                                                editOptions(data.id).map((option, i) => <div
                                                    key={i}
                                                    onClick={option.action}
                                                ><p>{option.label}</p></div>)
                                            }
                                        </div>
                                    </div>
                                </label>}
                                      
                            </div>
                            <div
                                className="cbInfor"
                                dangerouslySetInnerHTML={{ __html: data.content }}
                            />        
                        </div>)
                }
            </div>
        </div>
    );
}
