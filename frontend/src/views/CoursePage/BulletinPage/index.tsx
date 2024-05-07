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

import { CourseBulletin } from "schemas/courseBulletin";
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
    const [courseBulletinList, setCourseBulletin] = useState<Array<CourseBulletin>>([]);
    // text editor
    const [content, setContent] = useState('');
    const [title , setTitle] = useState("");

    useEffect(() => {
        getCourseBulletinList(courseID).then(data => {
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
        const uid = userData?.uid;
        const publisher = userData?.name;
        if (uid) {
            const courseBulletin : CourseBulletin = {
                uid: uid,
                course_id:courseID,
                title: title,
                pin_to_top: false,
                content: content,
                publisher: publisher || "",
            }
            const result = await postCourseBulletin(courseBulletin);
            console.log(result);
        }
        else {}
        setContent("");
        setTitle("");
        getCourseBulletinList(courseID).then(data => {
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

    const setTimeString = (release_time:number):string => {
        const releaseDate = new Date(release_time);
        const weekdays = ["日", "一", "二", "三", "四", "五", "六"];
        const formattedDate = `${releaseDate.getFullYear()}年${("0" + (releaseDate.getMonth() + 1)).slice(-2)}月${("0" + releaseDate.getDate()).slice(-2)}日(${weekdays[releaseDate.getDay()]}) ${("0" + releaseDate.getHours()).slice(-2)}:${("0" + releaseDate.getMinutes()).slice(-2)}`;
        return formattedDate;
    }

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
                                    <p className="cbTime">{setTimeString(data.release_time || 0)}</p>
                                </div>
                                { data.uid === userData?.uid && <label className="dropdownMenu">
                                    <SlOptions/>
                                    <input type="checkbox" />
                                    <div className="mask" style={{ "--length": 3 } as CSSProperties}>
                                        <div className="content body-bold">
                                            {
                                                editOptions(data.id || "").map((option, i) => <div
                                                    key={i}
                                                    onClick={option.action}
                                                ><p>{option.label}</p></div>)
                                            }
                                        </div>
                                    </div>
                                </label>}
                                      
                            </div>
                            <h3>{data.title}</h3>  
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
