import {
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss"
import functionContext from "context/function";
import NumberDropDownMenu from "components/NumberDropDownMenu";

type propsType = Readonly<{
    show: boolean,
    themeId: number,
    close: () => void,
    callback: (type: number) => void,
}>;

export default function NewFiles(props: propsType): ReactElement {
    const {
        show,
        close,
        callback,
    } = props;

    const { getText } = useContext(functionContext);

    const onKeyDown = useCallback((event: KeyboardEvent) => {
        if (event.key === "Escape") {
            close()
        }
    }, [close]);

    useEffect(() => {
        document.addEventListener("keydown", onKeyDown);
    }, [onKeyDown]);

    useEffect(() => () => {
        document.removeEventListener("keydown", onKeyDown);
    }, [onKeyDown]);

    return <div id="newFiles" data-show={show ? true : undefined} onClick={(event) => {
        const target: HTMLElement = event.target as HTMLElement;
        if (target.id === "newMaterial") {
            close();
        }
    }}>
        <div className="box">
            <button className="close ms" onClick={() => close()}>close</button>
            <div className="title body-bold">{getText("add_material_setting")}</div>
            <div className="content">
                <div className="setting">
                    <div className="left">
                        <div className="row">
                            <div className="key">教材名稱</div>
                            <input />
                        </div>
                        <div className="row">
                            <div className="key">教材說明</div>
                            <textarea />
                        </div>
                    </div>
                    <div className="right">
                        <div className="visible">
                            <div className="row">
                                <div className="key">教材可見</div>
                                <label>
                                    <input type="checkbox" />
                                </label>
                            </div>
                        </div>
                        <div className="row first">
                            <div className="key">
                                啟用時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={0}
                                setValue={(value: number) => { }}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={0}
                                setValue={(value: number) => { }}
                            />
                        </div>
                        <div className="row">
                            <div className="key">
                                停用時間
                            </div>
                            <svg width="18" height="20" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 18H2V7H16M13 0V2H5V0H3V2H2C0.89 2 0 2.89 0 4V18C0 18.5304 0.210714 19.0391 0.585786 19.4142C0.960859 19.7893 1.46957 20 2 20H16C16.5304 20 17.0391 19.7893 17.4142 19.4142C17.7893 19.0391 18 18.5304 18 18V4C18 2.89 17.1 2 16 2H15V0" fill="black" />
                            </svg>
                            <input className="date" type="date" />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={23}
                                value={0}
                                setValue={(value: number) => { }}
                            />
                            <NumberDropDownMenu
                                rangeStart={0}
                                rangeEnd={59}
                                value={0}
                                setValue={(value: number) => { }}
                            />
                        </div>
                    </div>
                </div>
                <div className="addFiles">
                    <div className="title">
                        <div>選擇檔案</div>
                        <button>選擇檔案</button>
                    </div>
                </div>
            </div>
            <div className="buttonBar">
                <button
                    className="cancel caption-bold"
                    onClick={() => close()}
                >{getText("cancel")}</button>
                <button
                    className="next caption-bold"
                    onClick={() => callback(0)}
                >{getText("confirm")}</button>
            </div>
        </div>
    </div>
};
