import {
    ReactElement,
    useMemo
} from "react";

import ICON_MAP, { IMAGE } from "./icons";

import "./index.scss";

type propsType = Readonly<{
    filename: string,
    iconType?: "PDF" | "WORD" | "PPT" | "IMAGE"
    onClick?: () => void
}>;

export default function FilesIcon(props: propsType): ReactElement {
    const {
        filename,
        iconType,
        onClick
    } = props;

    const icon: ReactElement = useMemo(() => {
        if (iconType !== undefined && Object.keys(ICON_MAP).includes(iconType))
            return ICON_MAP[iconType];

        return IMAGE;
    }, [iconType]);

    return <div className="fileIcon">
        <div className="icon">
            {icon}
        </div>
        <div className="name">{filename}</div>
    </div>
};
