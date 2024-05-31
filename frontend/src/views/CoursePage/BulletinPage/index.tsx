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
import { getCourseBulletinList,postCourseBulletin , deleteCourseBulletin , updateCourseBulletin } from "api/courseBulletin";

const UserIcon = `${process.env.PUBLIC_URL}/assets/testUser.png`;

type propsType = Readonly<{
    courseID: number
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

    const [isEditing , setEdit] = useState(false);
    const [editingCB , setEditingCB] = useState<CourseBulletin>();

    useEffect(() => {
        handleCourseBulletinList();
    }, []);

    const handleCourseBulletinList = () => {
        getCourseBulletinList(courseID).then(data => {
            setCourseBulletin(data);
        }).catch( error =>{
            if (error.response && error.response.status === 404) {
                
            } else {
                
            }
        });
    }

    const handleContentChange = (value:string, delta:any) => {
        setContent(value);
    };

    const onSubmit = async () =>{

        if (!isEditing){
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
            }
            else {}
        }
        else {
            if(editingCB){
                editingCB.content = content;
                editingCB.title = title;
                await updateCourseBulletin(editingCB);
            }
            setEdit(false);
        }
        
        setContent("");
        setTitle("");
        handleCourseBulletinList();
    }

    const deleteBulletin = async(id:number) =>{
        await deleteCourseBulletin(id);
        handleCourseBulletinList();
    }

    const pinBulletin = async(id:number) =>{
        const theBulletin = courseBulletinList.find(item => item.id === id) ;
        if (theBulletin) {
            theBulletin.pin_to_top = !theBulletin.pin_to_top;
            await updateCourseBulletin(theBulletin);
        } else {
            console.error("theBulletin is undefined.");
        }
        handleCourseBulletinList();
    }

    const editBulletin = async(id:number) =>{
        const theBulletin = courseBulletinList.find(item => item.id === id);
        setContent(theBulletin?.content||"");
        setTitle(theBulletin?.title||"");
        setEditingCB(theBulletin);
        setEdit(true);
    }

    type Option = {
        label: string;
        action: (() => void) | undefined;
    };
    
    const editOptions = (id: number , isPinned: boolean): Option[] => [
        { label: "編輯" ,action:() => editBulletin(id)},
        { label: "刪除", action: () => deleteBulletin(id) },
        { label: isPinned ? "取消置頂" : "置頂" , action: () => pinBulletin(id) }
    ];

    const setTimeString = (release_time:string):string => {
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
                                    <p className="cbTime">{setTimeString(data.release_time || "")}</p>
                                </div>
                                { data.uid === userData?.uid && <label className="dropdownMenu">
                                    <SlOptions/>
                                    <input type="checkbox" />
                                    <div className="mask" style={{ "--length": 3 } as CSSProperties}>
                                        <div className="content body-bold">
                                            {
                                                editOptions(data.id || 0 , data.pin_to_top).map((option, i) => <div
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
