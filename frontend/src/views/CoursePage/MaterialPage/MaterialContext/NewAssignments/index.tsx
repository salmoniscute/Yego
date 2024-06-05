import {
    CSSProperties,
    ChangeEvent,
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss"
import functionContext from "context/function";
import NumberDropDownMenu from "components/NumberDropDownMenu";
import userDataContext from "context/userData";
import { createAssignment } from "api/courseMaterials";

type propsType = Readonly<{
    show: boolean,
    themeId: number,
    files: Array<File>,
    close: () => void,
    selectFile: () => void,
    updateData: () => void,
}>;

const formatType = [
    "純文字",
    "檔案",
    "無"
];

const date = new Date();
const dateString = `${date.getFullYear()}-${date.getMonth().toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`;

export default function NewAssignments(props: propsType): ReactElement {
    const {
        show,
        files,
        themeId,
        close,
        selectFile,
        updateData,
    } = props;

    const [time1Date, setTime1Date] = useState<string>(dateString);
    const [time1Hour, setTime1Hour] = useState<number>(0);
    const [time1Minute, setTime1Minute] = useState<number>(0);
    const [time2Date, setTime2Date] = useState<string>(dateString);
    const [time2Hour, setTime2Hour] = useState<number>(0);
    const [time2Minute, setTime2Minute] = useState<number>(0);
    const [time3Date, setTime3Date] = useState<string>(dateString);
    const [time3Hour, setTime3Hour] = useState<number>(0);
    const [time3Minute, setTime3Minute] = useState<number>(0);
    const [currentFormat, setFormat] = useState<number>(0);

    const [name, setName] = useState<string>("");
    const [description, setDescription] = useState<string>("");
    const [visible, setVisible] = useState<boolean>(false);
    
    const { getText } = useContext(functionContext);
    const userData = useContext(userDataContext);

    const onKeyDown = useCallback((event: KeyboardEvent) => {
        if (event.key === "Escape") {
            close()
        }
    }, [close]);

    useEffect(() => {
        document.addEventListener("keydown", onKeyDown);
    }, [onKeyDown]);

    useEffect(() => () => {
        document.removeEventListener("keydown", onKeyDown);
    }, [onKeyDown]);

    return <div id="newAssignments" data-show={show ? true : undefined} onClick={(event) => {
        const target: HTMLElement = event.target as HTMLElement;
        if (target.id === "newAssignments") {
            close();
        }
    }}>
        <div className="box">
            <button className="close ms" onClick={() => close()}>close</button>
            <div className="title body-bold">{getText("add_material_setting")}</div>
            <div className="content">
                <div className="setting">
                    <div className="left">
                        <div className="row">
                            <div className="key">教材名稱</div>
                            <input value={name} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setName(event.target.value);
                            }} />
                        </div>
                        <div className="row">
                            <div className="key">教材說明</div>
                            <textarea value={description} onChange={(event: ChangeEvent<HTMLTextAreaElement>) => {
                                setDescription(event.target.value);
                            }} />
                        </div>
                        <div className="addFiles">
                            <div className="subtitle">
                                <div>選擇檔案</div>
                                <button onClick={() => selectFile()}>選擇檔案</button>
                            </div>
                            <div className="files">
                                {files.map((file, i) => <div
                                    key={`${file.name}${i}`}
                                    className="file"
                                >
                                    {file.name}
                                </div>)}
                            </div>
                        </div>
                        <div className="format row">
                            <div className="subtitle">
                                <div>選擇檔案</div>
                            </div>
                            <div className="dropdown">
                                <label className="mask" style={{
                                    "--options": formatType.length
                                } as CSSProperties}>
                                    <div>{formatType[currentFormat]}</div>
                                    {formatType.map((v, i) => <div
                                        key={i}
                                        className="option"
                                        onClick={() => setFormat(i)}
                                    >{v}</div>)}
                                    <input type="checkbox" />
                                </label>
                            </div>
                        </div>
                    </div>
                    <div className="right">
                        <div className="visible">
                            <div className="row">
                                <div className="key">教材可見</div>
                                <label>
                                    <input type="checkbox" checked={visible} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                        setVisible(event.target.checked);
                                    }} />
                                </label>
                            </div>
                        </div>
                        <div className="row first">
                            <div className="key">
                                可繳交時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" value={time1Date} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setTime1Date(event.target.value);
                            }} />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={time1Hour}
                                setValue={setTime1Hour}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={time1Minute}
                                setValue={setTime1Minute}
                            />
                        </div>
                        <div className="row second">
                            <div className="key">
                                規定繳交時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" value={time2Date} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setTime2Date(event.target.value);
                            }} />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={time2Hour}
                                setValue={setTime2Hour}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={time2Minute}
                                setValue={setTime2Minute}
                            />
                        </div>
                        <div className="row">
                            <div className="key">
                                拒收作業時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" value={time3Date} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setTime3Date(event.target.value);
                            }} />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={time3Hour}
                                setValue={setTime3Hour}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={time3Minute}
                                setValue={setTime3Minute}
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div className="buttonBar">
                <button
                    className="cancel caption-bold"
                    onClick={() => close()}
                >{getText("cancel")}</button>
                <button
                    className="next caption-bold"
                    onClick={() => {
                        console.log(userData);
                        if (userData?.uid !== undefined) {
                            createAssignment(
                                userData.uid,
                                themeId,
                                {
                                    content: description,
                                    deadline: `${time2Date}T${time2Hour.toString().padStart(2, "0")}:${time2Minute.toString().padStart(2, "0")}:00`,
                                    display: visible,
                                    feedback_type: "",
                                    reject_time: `${time3Date}T${time3Hour.toString().padStart(2, "0")}:${time3Minute.toString().padStart(2, "0")}:00`,
                                    submitted_object: "",
                                    submitted_time: `${time1Date}T${time1Hour.toString().padStart(2, "0")}:${time1Minute.toString().padStart(2, "0")}:00`,
                                    submitted_type: "",
                                    title: name
                                }
                            ).then(() => {
                                updateData();
                            });
                        }
                        close();
                    }}
                >{getText("confirm")}</button>
            </div>
        </div>
    </div>
};
