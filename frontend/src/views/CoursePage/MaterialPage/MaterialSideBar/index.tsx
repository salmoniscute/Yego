import {
    CSSProperties,
    Dispatch,
    MouseEvent,
    ReactElement,
    SetStateAction,
    useCallback,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss";
import functionContext from "context/function";

type propsType = Readonly<{
    isTeacher: boolean,
    themeList: Array<{
        order: number,
        name: string,
        id: number,
    }>;
    selectedTheme: number,
    setSelectTheme: Dispatch<SetStateAction<number>>,
    switchOrder: (a: number, b: number) => void,
    restore: () => void,
    saveChange: () => void,
    addTheme: (themeName: string) => void,
}>

export default function MaterialSideBar(props: propsType): ReactElement {
    const {
        isTeacher,
        themeList,
        selectedTheme,
        setSelectTheme,
        switchOrder,
        saveChange,
        addTheme,
    } = props;

    const [holdingKey, setHoldingKey] = useState<number>(-1);
    const [editMode, setEditMode] = useState<boolean>(false);
    const [showNewTheme, setShowNewTheme] = useState<boolean>(false);
    const [newThemeName, setNewThemeName] = useState<string>("");

    const { getText } = useContext(functionContext);

    const addNewTheme = useCallback(() => {
        if (newThemeName === "") return;
        addTheme(newThemeName);
        setNewThemeName("");
        setShowNewTheme(false);
    }, [newThemeName, addTheme]);

    useEffect(() => {
        if (!editMode) {
            saveChange();
        }
    }, [editMode, saveChange]);

    return <div className="sideBar" data-edit={isTeacher ? editMode : undefined} onDragOver={event => event.preventDefault()}>
        {
            isTeacher ? <button className="switchEdit body" onClick={() => setEditMode(v => !v)}>
                <span>{editMode ? getText("edit_finish") : getText("edit_mode")}</span>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.71 7.04006C21.1 6.65006 21.1 6.00006 20.71 5.63006L18.37 3.29006C18 2.90006 17.35 2.90006 16.96 3.29006L15.12 5.12006L18.87 8.87006M3 17.2501V21.0001H6.75L17.81 9.93006L14.06 6.18006L3 17.2501Z" fill="black" />
                </svg>
            </button> : undefined
        }
        {
            isTeacher && editMode ? <button
                className="addTheme body"
                onClick={() => setShowNewTheme(true)}
            >{getText("add_theme")}</button> : undefined
        }
        {
            isTeacher && editMode ? <div
                className="addThemeBox"
                data-show={showNewTheme ? true : undefined}
                onClick={(event: MouseEvent<HTMLElement>) => {
                    const element: HTMLElement = event.target as HTMLElement;
                    if (element.classList.contains("addThemeBox")) {
                        setShowNewTheme(false);
                    }
                }}
            >
                <div className="box">
                    <button
                        className="close ms"
                        onClick={() => setShowNewTheme(false)}
                    >close</button>
                    <h2>{getText("add_theme")}</h2>
                    <div className="column body">
                        <div className="key">{getText("add_theme_name")}</div>
                        <input className="value" value={newThemeName} onChange={(event) => { setNewThemeName(event.target.value) }} />
                    </div>
                    <div className="buttonBar">
                        <button
                            className="add caption"
                            onClick={addNewTheme}
                            disabled={newThemeName === ""}
                        >{getText("add")}</button>
                    </div>
                </div>
            </div> : undefined
        }
        <div className="themeBox">
            {
                themeList.map((v, i) => <div
                    key={v.id}
                    className="theme"
                    data-selected={selectedTheme === v.id}
                    data-ondrag={holdingKey === i}
                    draggable={(editMode && isTeacher) ? true : undefined}
                    onClick={() => setSelectTheme(v.id)}
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
                    style={{ "--order": v.order } as CSSProperties}
                >{v.name}</div>)
            }
        </div>
    </div>
};
