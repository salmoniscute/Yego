import {
    useEffect,
    useState,
    useMemo,
    useContext,
} from "react";
import ReactQuill from 'react-quill';
import 'react-quill/dist/quill.snow.css';
import CourseBulletinEditor , {modules,formats} from "components/CourseBulletinEditor";
import userDataContext from "context/userData";
import "./index.scss";

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
        getCourseBulletinList("CSE101").then(data => {
            setCourseBulletin(data);
        });
    }, []);

    const handleContentChange = (value:string, delta:any) => {
        setContent(value);
    };

    const onSubmit = async () =>{
        const nowTime = new Date().getTime();
        const courseBulletin = await postCourseBulletin("salmon","CSE101",title,nowTime,content,false);
        if (courseBulletin){
            console.log(courseBulletin);
        }

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
            <div className="courseBulletin">
                {
                    courseBulletinList.map(data =>
                        <div className="courseBulletinContent">
                            
                            <div className="cb">
                                <div className="cbContent">
                                    <div className="cbPin">置頂</div>
                                    <img src={UserIcon} />
                                    <p className="cbAuther">{data.publisher}</p>
                                    <p className="cbTime">{data.release_time}</p>
                                </div>
                                <p className="cbInfor">{data.content}</p>
                            </div>
                        </div>)
                }
            </div>
        </div>
    );
}
