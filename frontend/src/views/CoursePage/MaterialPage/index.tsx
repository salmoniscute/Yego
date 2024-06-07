import {
    CSSProperties,
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss";
import MaterialSideBar from "./MaterialSideBar";
import MaterialContext from "./MaterialContext";
import JoinGroup from "components/JoinGroup";

import { get_all_groups_info } from "api/group";
import { useParams } from "react-router-dom";
import { Material } from "schemas/material";
import { createMaterial, getMaterials } from "api/courseMaterials";
import userDataContext from "context/userData";
import { updateCourseMaterialOrder } from "api/updateOrder";

type propsType = Readonly<{
    courseID: number
}>;

// let themeExample: Array<{
//     name: string,
//     order: number,
//     id: number
// }> = [
//         {
//             name: "第一周",
//             order: 0,
//             id: 0,
//         },
//         {
//             name: "第二周",
//             order: 1,
//             id: 1,
//         },
//         {
//             name: "第三周",
//             order: 2,
//             id: 2,
//         },
//         {
//             name: "第四周",
//             order: 3,
//             id: 3,
//         },
//         {
//             name: "第五周",
//             order: 4,
//             id: 4,
//         },
//     ];

export default function MaterialPage(props: propsType): ReactElement {
    const {
        courseID,
    } = props;

    const [selectedTheme, setSelectTheme] = useState<number>(0);
    const [themeData, setThemeData] = useState<Array<Material>>([]);
    const [originThemeData, setOriginThemeData] = useState<Array<Material>>([]);
    const [showJoinGroup, setshowJoinGroup] = useState<Boolean>(false);
    const params = useParams();

    const userData = useContext(userDataContext);
    
    const isGroup = useCallback(async () => {
        await get_all_groups_info(Number(params.courseID)).then(data => {
            if(data.length > 0) setshowJoinGroup(true);
        });
    }, []);

    const updateThemeData = useCallback(async () => {
        const response = await getMaterials(courseID);
        setOriginThemeData(response);
        return response;
    }, []);

    useEffect(() => {
        setThemeData(originThemeData);
    }, [originThemeData]);

    useEffect(() => {
        isGroup();
        updateThemeData();
    }, [isGroup, updateThemeData]);

    return <div id="courseMaterialPage">
        <MaterialSideBar
            isTeacher={userData?.role === "teacher" || userData?.role === "assistant" || userData?.uid === "admin"}
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
            restore={() => setThemeData(originThemeData)}
            saveChange={() => {
                updateCourseMaterialOrder(themeData.map(v => ({
                    id: v.id,
                    order: v.order,
                    type: "",
                }))).then(() => {
                    updateThemeData();
                })
            }}
            addTheme={(themeName: string) => {
                if (userData !== null) {
                    createMaterial(userData.uid, courseID, themeName).then(() => {
                        updateThemeData();
                    });
                }
            }}
        />
        <div className="block">
            {showJoinGroup && userData?.role === "student" ? <JoinGroup /> : ""}
            <MaterialContext
                isTeacher={userData?.role === "teacher" || userData?.role === "assistant" || userData?.uid === "admin"}
                selectedTheme={selectedTheme}
                currentData={themeData[selectedTheme]}
                updateData={updateThemeData}
            />
        </div>
    </div>
}
