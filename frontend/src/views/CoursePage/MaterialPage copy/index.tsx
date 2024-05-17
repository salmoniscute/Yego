import {
    CSSProperties,
    ReactElement,
    useCallback,
    useEffect,
    useState
} from "react";

import "./index.scss";

type propsType = Readonly<{
    courseID: string
}>;

interface DataType {
    [key: string]: {
        order: number,
        materials?: Array<{
            name: string,
            order: number,
        }>
    }
};

let exampleData: DataType = {
    "第一周": {
        order: 0,
        materials: [
            { name: "M1", order: 0 },
            { name: "M2", order: 1 },
            { name: "M3", order: 2 },
            { name: "M4", order: 3 },
            { name: "M5", order: 4 },
        ]
    },
    "第二周": {
        order: 1,
        materials: [
            { name: "M6", order: 0 },
            { name: "M7", order: 1 },
            { name: "M8", order: 2 },
            { name: "M9", order: 3 },
            { name: "M10", order: 4 },
            { name: "M11", order: 5 },
        ]
    },
    "第三周": {
        order: 2,
    },
}

export default function MaterialPage(props: propsType): ReactElement {
    const [selectTheme, setSelectTheme] = useState<string>("");
    const [selectMaterial, setSelectMaterial] = useState<Array<number>>([]);
    const [editMode, setEditMode] = useState<boolean>(false);
    const [holding, setHolding] = useState<string>("");
    const [holdingMaterial, setHoldingMaterial] = useState<number>(-1);
    const [data, setData] = useState<DataType>(exampleData);

    const addTheme = useCallback(() => {
        setData(v => {
            let i = 0;
            let name = "新主題";
            while (Object.keys(v).includes(name)) {
                name = `新主題 (${++i})`;
            }
            const newData: DataType = {};
            newData[name] = {
                order: Object.keys(v).length
            }
            return Object.assign(newData, v);
        })
    }, []);

    useEffect(() => {
        setSelectMaterial([]);

        const keys = Object.keys(data);
        if (keys.includes(selectTheme) || keys.length === 0) return;
        setSelectTheme(keys[0]);
    }, [selectTheme]);

    return <div id="courseMaterialPage" data-edit={editMode}>
        <div className="side" onDragOver={event => event.preventDefault()}>
            <button className="edit" onClick={() => setEditMode(v => !v)}>
                <span>編輯模式</span>
                <span className="ms">edit</span>
            </button>
            {
                editMode ? <button className="newTheme" onClick={addTheme}>
                    <span>新增主題</span>
                </button> : undefined
            }
            {
                Object.keys(data).map((key) => <div
                    key={key}
                    onClick={() => setSelectTheme(key)}
                    onDrag={editMode ? (event) => {
                        event.preventDefault();
                        setHolding(key);
                    } : undefined}
                    onDragEnter={editMode ? (event) => {
                        event.preventDefault();
                        if (holding === key || holding === "") return;
                        setData(v => {
                            let newValue = Object.assign({}, v);
                            const temp = v[key].order;
                            newValue[key].order = v[holding].order;
                            newValue[holding].order = temp;
                            return newValue;
                        })
                    } : undefined}
                    onDragEnd={editMode ? (event) => {
                        event.preventDefault();
                        setHolding("");
                    } : undefined}
                    className="theme caption-bold"
                    data-select={key === selectTheme}
                    data-ondrag={holding == key}
                    draggable={editMode}
                    style={{ "--order": data[key].order } as CSSProperties}
                >
                    <span>{key}</span>
                </div>)
            }
        </div>
        <div className="main">
            <h2>{selectTheme}</h2>
            <div className="materialBlock">
                <div className="materials" onDragOver={event => event.preventDefault()}>
                    {
                        data[selectTheme]?.materials?.map((material, i) => <div
                            key={i}
                            className="material caption"
                            onClick={() => {
                                setSelectMaterial((selectMaterial) => {
                                    if (selectMaterial.includes(i)) {
                                        return selectMaterial.filter(d => d !== i);
                                    }
                                    return [i, ...selectMaterial];
                                });
                            }}
                            onDrag={editMode ? (event) => {
                                event.preventDefault();
                                setHoldingMaterial(i);
                            } : undefined}
                            onDragEnter={editMode ? (event) => {
                                event.preventDefault();
                                if (holdingMaterial === i || holdingMaterial === -1) return;
                                setData(v => {
                                    let newValue = Object.assign({}, v);
                                    const selectThemeMaterials = v[selectTheme].materials;
                                    if (selectThemeMaterials === undefined) return v;
                                    const temp = selectThemeMaterials[i].order;
                                    selectThemeMaterials[i].order = selectThemeMaterials[holdingMaterial].order;
                                    selectThemeMaterials[holdingMaterial].order = temp;
                                    newValue[selectTheme].materials = selectThemeMaterials;
                                    return newValue;
                                })
                            } : undefined}
                            onDragEnd={editMode ? (event) => {
                                event.preventDefault();
                                setHoldingMaterial(-1);
                            } : undefined}
                            draggable={editMode}
                            data-select={selectMaterial.includes(i)}
                            data-ondrag={holdingMaterial === i}
                            style={{ "--order": material.order } as CSSProperties}
                        >
                            <span>{material.name}</span>
                            <div className="background" />
                        </div>)
                    }
                </div>
                <button className="body-bold">
                    <span className="ms">download</span>
                    <span>下載</span>
                </button>
            </div>
        </div>
    </div>
}
