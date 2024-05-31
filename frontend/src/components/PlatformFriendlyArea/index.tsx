import {
    ReactElement,
    useContext,
} from "react";
import { Link } from "react-router-dom";

import functionContext from "context/function";

import "./index.scss";

interface HelpInfo {
    id: string,
    title: string,
    description: string,
    link : string
};

const HelpList: Array<HelpInfo> = [
    {
        id: "0",
        title: "母課程申請",
        description: "提供教師在多門課程使用共同教材的需求。",
        link : ""
    },
    {
        id: "1",
        title: "操作手冊",
        description: "操作教學說明",
        link : ""
    },
    {
        id: "2",
        title: "常見問題",
        description: "操作教學說明",
        link : ""
    },
    {
        id: "3",
        title: "問題回報",
        description: "操作教學說明",
        link: "/reportBug"
    },
];

type propsType = Readonly<{
    titleId: string
}>;

export default function PlatformFriendlyArea(props: propsType): ReactElement {
    const { titleId } = props;

    const {
        getText,
    } = useContext(functionContext)

    return <div className="platformFriendlyArea">
        <h2>{getText(titleId)}</h2>
        <div className="content">
            {
                HelpList.map((data, i) => <Link
                    key={i}
                    to={data.link}
                    className="block"
                >
                    <div className="body-bold">{data.title}</div>
                    <div className="body">{data.description}</div>
                </Link>)
            }
        </div>
    </div>
}
