import {
    CSSProperties,
    ReactElement,
    useCallback,
    useContext,
    useEffect,
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
import { updateCourseInfoOrder } from "api/updateOrder";
import UpdateOrder from "schemas/updateOrder";


type propsType = Readonly<{
    isTeacher: boolean,
    currentData: Material,
    selectedTheme: number,
    updateData: () => Promise<Array<Material>>,
}>;

export default function MaterialContext(props: propsType): ReactElement {
    const {
        isTeacher,
        currentData,
        selectedTheme,
        updateData,
    } = props;

    const aRef = useRef<HTMLAnchorElement>(null);

    const [holdingKey1, setHoldingKey1] = useState<number>(-1);
    const [holdingKey2, setHoldingKey2] = useState<number>(-1);
    const [editMode, setEditMode] = useState<boolean>(false);
    const [currentWindow, setCurrentWindow] = useState<number>(0);
    const [showSelectFile, setShowSelectFile] = useState<boolean>(false);
    const [selectFiles, setSelectFiles] = useState<Array<File>>([]);
    const [displayData, setDisplayData] = useState<Material>(currentData);

    const { getText } = useContext(functionContext);

    const saveChange = useCallback(() => {
        updateCourseInfoOrder((displayData?.material_infos ?? []).map(v => ({
            id: v.id,
            order: v.order,
            type: "material_info"
        } as UpdateOrder)).concat((displayData?.assignments ?? []).map(v => ({
            id: v.id,
            order: v.order,
            type: "assignment"
        } as UpdateOrder))));
        console.log(displayData);
    }, [displayData]);

    const switchOrder = useCallback((a: number, b: number, type: "material_info" | "assignment") => {
        setDisplayData(v => {
            let materials = type === "material_info" ? v.material_infos : v.assignments;
            if (a < 0 || a >= materials.length || b < 0 || b >= materials.length) return v;
            let newValue = Object.assign({}, v);
            let bOrder = materials[b].order;
            (type === "material_info" ? newValue.material_infos : newValue.assignments)[b].order = materials[a].order;
            (type === "material_info" ? newValue.material_infos : newValue.assignments)[a].order = bOrder;

            return newValue;
        })
    }, []);

    useEffect(() => {
        setDisplayData(currentData);
        setHoldingKey1(-1);
        setHoldingKey2(-1);
        setEditMode(false);
    }, [currentData]);

    // useEffect(() => {
    //     if (!editMode) {
    //         saveChange();
    //     }
    // }, [editMode, saveChange]);

    useEffect(() => {
        setSelectFiles([]);
    }, [currentWindow]);

    return <div className="context" data-edit={editMode ? true : undefined} onDragOver={event => event.preventDefault()}>
        <a ref={aRef} />
        <h2>
            <span>{displayData?.title}</span>
            <button className="switchEdit caption" onClick={() => setEditMode(v => {
                if (v) {
                    saveChange();
                }
                return !v;
            })}>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.71 7.04006C21.1 6.65006 21.1 6.00006 20.71 5.63006L18.37 3.29006C18 2.90006 17.35 2.90006 16.96 3.29006L15.12 5.12006L18.87 8.87006M3 17.2501V21.0001H6.75L17.81 9.93006L14.06 6.18006L3 17.2501Z" fill="black" />
                </svg>
                <span>{editMode ? getText("edit_finish") : getText("edit_mode")}</span>
            </button>
        </h2>
        {
            isTeacher && editMode ? <NewMaterial
                show={currentWindow == 1}
                themeId={displayData.id}
                closeBeforeCallback={false}
                close={() => setCurrentWindow(0)}
                callback={(selectType: number) => {
                    setCurrentWindow(selectType + 2);
                }}
            /> : undefined
        }
        {isTeacher && editMode ? <NewAssignments
            show={currentWindow === 3}
            themeId={displayData.id}
            files={selectFiles}
            close={() => setCurrentWindow(-1)}
            selectFile={() => setShowSelectFile(true)}
            updateData={updateData}
        /> : undefined}
        {isTeacher && editMode ? <NewFiles
            show={currentWindow === 4}
            themeId={displayData.id}
            files={selectFiles}
            selectedTheme={selectedTheme}
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
            displayData?.material_infos.map((v, i) => <div
                key={v.id}
                className="material"
                data-ondrag={holdingKey1 === i}
                draggable={(editMode && isTeacher) ? true : undefined}
                onDrag={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey1(i);
                } : undefined}
                onDragEnter={editMode ? (event) => {
                    event.preventDefault();
                    if (holdingKey1 === i || holdingKey1 === -1) return;
                    switchOrder(holdingKey1, i, "material_info");
                } : undefined}
                onDragEnd={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey1(-1);
                } : undefined}
                style={{ "--order": v.order ?? 0 } as CSSProperties}
                onClick={() => {
                    console.log(v);
                    if (v.files.length === 0)
                        return;
                    axios.get(`/file?file_id=${v.files[0].id}`, {
                        responseType: "blob"
                    }).then(r => {
                        const file: Blob = r.data;

                        const url = URL.createObjectURL(file);
                        if (aRef.current !== null) {
                            aRef.current.href = url;
                            aRef.current.download = v.files[0].path.split("/").reverse()[0]
                            aRef.current.click();
                            URL.revokeObjectURL(url);
                        }
                    })
                }}
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
        {
            displayData?.assignments.map((v, i) => <div
                key={v.id}
                className="material"
                data-ondrag={holdingKey2 === i}
                draggable={(editMode && isTeacher) ? true : undefined}
                onDrag={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey2(i);
                } : undefined}
                onDragEnter={editMode ? (event) => {
                    event.preventDefault();
                    if (holdingKey2 === i || holdingKey2 === -1) return;
                    switchOrder(holdingKey2, i, "assignment");
                } : undefined}
                onDragEnd={editMode ? (event) => {
                    event.preventDefault();
                    setHoldingKey2(-1);
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
