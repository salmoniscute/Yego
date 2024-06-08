import {
    ReactElement
} from "react";

import "./index.scss";

type propsType = Readonly<{
    show: boolean
}>;

export default function LoadingPage(props: propsType): ReactElement {
    const {
        show
    } = props;

    return <div id="loadingPage" data-show={show}>
        <div className="box">
            <img alt="yegoo icon" src={`${process.env.PUBLIC_URL}/assets/Yegogo2.png`} />
            <div className="text">Loading...</div>
        </div>
    </div>
};
