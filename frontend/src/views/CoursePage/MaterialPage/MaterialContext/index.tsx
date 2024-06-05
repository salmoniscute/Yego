import {
    CSSProperties,
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useMemo,
    useRef,
    useState
} from "react";

import "./index.scss";
import functionContext from "context/function";
import NewMaterial from "./NewMaterial";
import NewFiles from "./NewFiles";
import UploadFiles from "components/UploadFiles";
import NewAssignments from "./NewAssignments";
import { Material } from "schemas/material";
import axios from "axios";


type propsType = Readonly<{
    isTeacher: boolean,
    currentData: Material,
    updateData: () => void,
}>;

// let exampleData: {
//     [key: number]: {
//         name: string,
//         materials: Array<{
//             type: "rc" | "asm" | "file",
//             name: string,
//             id: number,
//             order: number,
//         }>
//     }
// } = {
//     0: {
//         name: "第一周",
//         materials: [
//             {
//                 type: "rc",
//                 name: "點名一",
//                 id: 0,
//                 order: 0,
//             },
//             {
//                 type: "asm",
//                 name: "作業一",
//                 id: 1,
//                 order: 1,
//             },
//             {
//                 type: "file",
//                 name: "檔案一",
//                 id: 2,
//                 order: 2,
//             },
//         ]
//     },
//     1: {
//         name: "第二周",
//         materials: [
//             {
//                 type: "rc",
//                 name: "點名一",
//                 id: 0,
//                 order: 0,
//             },
//             {
//                 type: "rc",
//                 name: "點名二",
//                 id: 1,
//                 order: 1,
//             },
//             {
//                 type: "rc",
//                 name: "點名三",
//                 id: 2,
//                 order: 2,
//             },
//         ]
//     },
//     2: {
//         name: "第三周",
//         materials: [
//             {
//                 type: "asm",
//                 name: "作業一",
//                 id: 0,
//                 order: 0,
//             },
//             {
//                 type: "asm",
//                 name: "作業二",
//                 id: 1,
//                 order: 1,
//             },
//             {
//                 type: "asm",
//                 name: "作業三",
//                 id: 2,
//                 order: 2,
//             },
//         ]
//     },
//     3: {
//         name: "第四周",
//         materials: [
//             {
//                 type: "file",
//                 name: "檔案一",
//                 id: 0,
//                 order: 0,
//             },
//             {
//                 type: "file",
//                 name: "檔案二",
//                 id: 1,
//                 order: 1,
//             },
//             {
//                 type: "file",
//                 name: "檔案三",
//                 id: 2,
//                 order: 2,
//             },
//         ]
//     },
//     4: {
//         name: "第五周",
//         materials: []
//     },
// }

export default function MaterialContext(props: propsType): ReactElement {
    const {
        isTeacher,
        currentData,
        updateData,
    } = props;

    const aRef = useRef(null);

    const [holdingKey, setHoldingKey] = useState<number>(-1);
    const [editMode, setEditMode] = useState<boolean>(false);
    const [currentWindow, setCurrentWindow] = useState<number>(0);
    const [showSelectFile, setShowSelectFile] = useState<boolean>(false);
    const [selectFiles, setSelectFiles] = useState<Array<File>>([]);

    const { getText } = useContext(functionContext);

    const saveChange = useCallback(() => {
        // if (currentData === undefined) return;
        // exampleData[themeId] = currentData;
    }, []);

    const switchOrder = useCallback((a: number, b: number) => {
        // setCurrentData(v => {
        //     if (v === undefined) return;
        //     let materials = v.materials;
        //     if (a < 0 || a >= materials.length || b < 0 || b >= materials.length) return v;
        //     let newValue = Object.assign({}, v);
        //     let bOrder = materials[b].order;
        //     newValue.materials[b].order = materials[a].order;
        //     newValue.materials[a].order = bOrder;

        //     return newValue;
        // })
    }, []);

    useEffect(() => {
        // setCurrentData(exampleData[themeId]);
        setHoldingKey(-1);
        setEditMode(false);
    }, [currentData]);

    useEffect(() => {
        if (!editMode) {
            saveChange();
        }
    }, [editMode, saveChange]);

    useEffect(() => {
        setSelectFiles([]);
    }, [currentWindow]);

    return <div className="context" data-edit={editMode ? true : undefined} onDragOver={event => event.preventDefault()}>
        <h2>
            <span>{currentData?.title}</span>
            <button className="switchEdit caption" onClick={() => setEditMode(v => !v)}>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.71 7.04006C21.1 6.65006 21.1 6.00006 20.71 5.63006L18.37 3.29006C18 2.90006 17.35 2.90006 16.96 3.29006L15.12 5.12006L18.87 8.87006M3 17.2501V21.0001H6.75L17.81 9.93006L14.06 6.18006L3 17.2501Z" fill="black" />
                </svg>
                <span>{editMode ? getText("edit_finish") : getText("edit_mode")}</span>
            </button>
        </h2>
        {
            isTeacher && editMode ? <NewMaterial
                show={currentWindow == 1}
                themeId={currentData.id}
                closeBeforeCallback={false}
                close={() => setCurrentWindow(0)}
                callback={(selectType: number) => {
                    setCurrentWindow(selectType + 2);
                }}
            /> : undefined
        }
        {isTeacher && editMode ? <NewAssignments
            show={currentWindow === 3}
            themeId={currentData.id}
            files={selectFiles}
            close={() => setCurrentWindow(-1)}
            selectFile={() => setShowSelectFile(true)}
            updateData={updateData}
        /> : undefined}
        {isTeacher && editMode ? <NewFiles
            show={currentWindow === 4}
            themeId={currentData.id}
            files={selectFiles}
            close={() => setCurrentWindow(-1)}
            selectFile={() => setShowSelectFile(true)}
            updateData={updateData}
        /> : undefined}
        {isTeacher && editMode ? <UploadFiles
            show={showSelectFile}
            initFiles={selectFiles}
            close={() => setShowSelectFile(false)}
            callback={(files: Array<File>) => {
                setSelectFiles(files);
            }}
        /> : undefined}
        {
            isTeacher && editMode ? <button
                className="addMaterial caption"
                onClick={() => setCurrentWindow(1)}
            >{getText("add_material")}</button> : undefined
        }
        {
            currentData?.material_infos.map((v, i) => <div
                key={v.id}
                className="material"
                data-ondrag={holdingKey === i}
                draggable={(editMode && isTeacher) ? true : undefined}
                onDrag={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey(i);
                } : undefined}
                onDragEnter={editMode ? (event) => {
                    event.preventDefault();
                    if (holdingKey === i || holdingKey === -1) return;
                    switchOrder(holdingKey, i);
                } : undefined}
                onDragEnd={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey(-1);
                } : undefined}
                style={{ "--order": v.order ?? 0 } as CSSProperties}
                onClick={() => {
                    if (v.files.length === 0)
                        return;
                    axios.get(`/file`)
                }}
            >
                <a ref={aRef} />
                <span>{v.title}</span>
                {
                    isTeacher && editMode ? <button
                        className="editMaterial"
                    >
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20.71 7.04006C21.1 6.65006 21.1 6.00006 20.71 5.63006L18.37 3.29006C18 2.90006 17.35 2.90006 16.96 3.29006L15.12 5.12006L18.87 8.87006M3 17.2501V21.0001H6.75L17.81 9.93006L14.06 6.18006L3 17.2501Z" fill="black" />
                        </svg>
                        <span>{getText("edit_material")}</span>
                    </button> : undefined
                }
            </div>)
        }
        {
            currentData?.assignments.map((v, i) => <div
                key={v.id}
                className="material"
                data-ondrag={holdingKey === i}
                draggable={(editMode && isTeacher) ? true : undefined}
                onDrag={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey(i);
                } : undefined}
                onDragEnter={editMode ? (event) => {
                    event.preventDefault();
                    if (holdingKey === i || holdingKey === -1) return;
                    switchOrder(holdingKey, i);
                } : undefined}
                onDragEnd={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey(-1);
                } : undefined}
                style={{ "--order": v.order ?? 0 } as CSSProperties}
            >
                <span>{v.title}</span>
                {
                    isTeacher && editMode ? <button
                        className="editMaterial"
                    >
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20.71 7.04006C21.1 6.65006 21.1 6.00006 20.71 5.63006L18.37 3.29006C18 2.90006 17.35 2.90006 16.96 3.29006L15.12 5.12006L18.87 8.87006M3 17.2501V21.0001H6.75L17.81 9.93006L14.06 6.18006L3 17.2501Z" fill="black" />
                        </svg>
                        <span>{getText("edit_material")}</span>
                    </button> : undefined
                }
            </div>)
        }
    </div>
};
