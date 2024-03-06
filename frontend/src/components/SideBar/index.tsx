import { ReactElement } from "react";

import "./index.scss";

type propsType = Readonly<{
    show: boolean,
}>;

export default function SideBar(props: propsType): ReactElement {
    const {
        show
    } = props;

    return <div id="sideBar" data-show={show}>
        <div className="mask">
            
        </div>
    </div>
};
