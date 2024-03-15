import {
    ReactElement,
    useEffect,
    useState
} from "react";

import "./index.scss";

type propsType = Readonly<{
    courseID: string
}>;

let data: {
    [key: string]: {
        order: number,
        materials?: Array<{
            name: string,
        }>
    }
} = {
    "第一周": {
        order: 0,
        materials: [
            { name: "M1" },
            { name: "M2" },
            { name: "M3" },
            { name: "M4" },
            { name: "M5" },
        ]
    },
    "第二周": {
        order: 1,
        materials: [
            { name: "M6" },
            { name: "M7" },
            { name: "M8" },
            { name: "M9" },
            { name: "M10" },
            { name: "M11" },
        ]
    },
    "第三周": {
        order: 2,
    },
}

export default function MaterialPage(props: propsType): ReactElement {
    const [selectTheme, setSelectTheme] = useState<string>("");
    const [selectMaterial, setSelectMaterial] = useState<Array<number>>([]);

    useEffect(() => {
        setSelectMaterial([]);

        const keys = Object.keys(data);
        if (keys.includes(selectTheme) || keys.length === 0) return;
        setSelectTheme(keys[0]);
    }, [selectTheme]);

    return <div id="courseMaterialPage">
        <div className="side">
            {
                Object.keys(data).map((key, i) => <div
                    key={i}
                    onClick={() => setSelectTheme(key)}
                    className="theme caption-bold"
                    data-select={key === selectTheme}
                >
                    {key}
                </div>)
            }
        </div>
        <div className="main">
            <h2>{selectTheme}</h2>
            <div className="materialBlock">
                <div className="materials">
                    {
                        data[selectTheme]?.materials?.map((data, i) => <div
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
                            data-select={selectMaterial.includes(i)}
                        >
                            {data.name}
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
