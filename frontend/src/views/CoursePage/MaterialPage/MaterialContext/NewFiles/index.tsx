import {
    ChangeEvent,
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useMemo,
    useState
} from "react";

import "./index.scss"
import functionContext from "context/function";
import NumberDropDownMenu from "components/NumberDropDownMenu";
import { createMaterialInfo } from "api/courseMaterials";
import userDataContext from "context/userData";
import { Material } from "schemas/material";
import { uploadFile } from "api/file";

type propsType = Readonly<{
    show: boolean,
    themeId: number,
    files: Array<File>,
    selectedTheme: number,
    close: () => void,
    selectFile: () => void,
    updateData: () => Promise<Array<Material>>,
}>;

const date = new Date();
const dateString = `${date.getFullYear()}-${date.getMonth().toString().padStart(2, "0")}-${date.getDate().toString().padStart(2, "0")}`;

export default function NewFiles(props: propsType): ReactElement {
    const {
        show,
        files,
        themeId,
        selectedTheme,
        close,
        selectFile,
        updateData,
    } = props;

    const [upTimeDate, setUpTimeDate] = useState<string>(dateString);
    const [upTimeHour, setUpTimeHour] = useState<number>(0);
    const [upTimeMinute, setUpTimeMinute] = useState<number>(0);
    const [downTimeDate, setDownTimeDate] = useState<string>(dateString);
    const [downTimeHour, setDownTimeHour] = useState<number>(0);
    const [downTimeMinute, setDownTimeMinute] = useState<number>(0);

    const [name, setName] = useState<string>("");
    const [description, setDescription] = useState<string>("");
    const [visible, setVisible] = useState<boolean>(false);

    const { getText } = useContext(functionContext);
    const userData = useContext(userDataContext);
    const {
        setLoading
    } = useContext(functionContext);

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

    return <div id="newFiles" data-show={show ? true : undefined} onClick={(event) => {
        const target: HTMLElement = event.target as HTMLElement;
        if (target.id === "newFiles") {
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
                                啟用時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" value={upTimeDate} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setUpTimeDate(event.target.value);
                            }} />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={upTimeHour}
                                setValue={setUpTimeHour}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={upTimeMinute}
                                setValue={setUpTimeMinute}
                            />
                        </div>
                        <div className="row">
                            <div className="key">
                                停用時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" value={downTimeDate} onChange={(event: ChangeEvent<HTMLInputElement>) => {
                                setDownTimeDate(event.target.value);
                            }} />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={downTimeHour}
                                setValue={setDownTimeHour}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={downTimeMinute}
                                setValue={setDownTimeMinute}
                            />
                        </div>
                    </div>
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
            </div>
            <div className="buttonBar">
                <button
                    className="cancel caption-bold"
                    onClick={() => close()}
                >{getText("cancel")}</button>
                <button
                    className="next caption-bold"
                    onClick={() => {
                        if (userData !== null) {
                            setLoading(true);
                            createMaterialInfo(
                                userData.uid,
                                themeId,
                                {
                                    title: name,
                                    content: description,
                                    display: visible,
                                    start_time: `${upTimeDate}T${upTimeHour.toString().padStart(2, "0")}:${upTimeMinute.toString().padStart(2, "0")}:00`,
                                    end_time: `${downTimeDate}T${downTimeHour.toString().padStart(2, "0")}:${downTimeMinute.toString().padStart(2, "0")}:00`
                                }
                            ).then(() => {
                                updateData().then(newData => {
                                    const materialId = Array.from(newData[selectedTheme].material_infos).pop()?.id;
                                    if (materialId !== undefined)
                                        uploadFile(materialId, files).then(() => {
                                            updateData();
                                        }).finally(() => {
                                            setLoading(false);
                                        });
                                }).catch(() => {
                                    setLoading(false);
                                });
                            }).catch(() => {
                                setLoading(false);
                            });
                        }
                        close();
                    }}
                >{getText("confirm")}</button>
            </div>
        </div>
    </div>
};
