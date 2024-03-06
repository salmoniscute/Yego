import en_US from "local/en_US.json";
import zh_Hant from "local/zh_Hant.json";

const localMap: {
    [key: string]: { [key: string]: string }
} = {
    "en_US": en_US,
    "zh_Hant": zh_Hant,
}

export default function getText(id: string): string {
    const zone = localStorage.getItem("local") || "zh_Hant";
    const localData = localMap[zone] || localMap.en_US;
    const result = localData[id] || localMap.en_US[id] || id;

    return result;
};
