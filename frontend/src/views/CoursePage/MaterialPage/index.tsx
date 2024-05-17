import {
    CSSProperties,
    ReactElement,
    useCallback,
    useEffect,
    useState
} from "react";

import "./index.scss";
import MaterialSideBar from "./MaterialSideBar";
import MaterialContext from "./MaterialContext";

type propsType = Readonly<{
    courseID: string
}>;

let themeExample: Array<{
    name: string,
    order: number,
    id: number
}> = [
        {
            name: "第一周",
            order: 0,
            id: 0,
        },
        {
            name: "第二周",
            order: 1,
            id: 1,
        },
        {
            name: "第三周",
            order: 2,
            id: 2,
        },
        {
            name: "第四周",
            order: 3,
            id: 3,
        },
        {
            name: "第五周",
            order: 4,
            id: 4,
        },
    ];

export default function MaterialPage(props: propsType): ReactElement {
    const [selectedTheme, setSelectTheme] = useState<number>(0);
    const [themeData, setThemeData] = useState<Array<{ name: string, order: number, id: number }>>(themeExample);

    return <div id="courseMaterialPage">
        <MaterialSideBar
            isTeacher={true}
            themeList={themeData}
            selectedTheme={selectedTheme}
            setSelectTheme={setSelectTheme}
            switchOrder={(a: number, b: number) => setThemeData(v => {
                if (a < 0 || a >= v.length || b < 0 || b >= v.length) return v;
                let newValue = Array.from(v);
                let bOrder = v[b].order;
                newValue[b].order = v[a].order;
                newValue[a].order = bOrder;
                return newValue;
            })}
            restore={() => setThemeData(themeExample)}
            saveChange={() => { themeExample = Array.from(themeData); }}
            addTheme={(themeName: string) => {
                themeExample.push({
                    name: themeName,
                    order: themeExample.length,
                    id: themeExample.length
                })
                setThemeData(themeExample);
            }}
        />
        <MaterialContext
            isTeacher={true}
            themeId={selectedTheme}
        />
    </div>
}
