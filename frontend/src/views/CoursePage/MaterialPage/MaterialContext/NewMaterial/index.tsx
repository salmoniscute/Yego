import {
    ReactElement,
    useCallback,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss"
import functionContext from "context/function";

type propsType = Readonly<{
    show: boolean,
    themeId: number,
    closeBeforeCallback?: boolean
    close: () => void,
    callback: (type: number) => void,
}>;

export default function NewMaterial(props: propsType): ReactElement {
    const {
        show,
        // themeId,
        closeBeforeCallback,
        close,
        callback,
    } = props;

    const [selectType, setSelectType] = useState<number>(-1);

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

    useEffect(() => {
        setSelectType(-1)
    }, [show]);

    return <div id="newMaterial" data-show={show ? true : undefined} onClick={(event) => {
        const target: HTMLElement = event.target as HTMLElement;
        if (target.id === "newMaterial") {
            close();
        }
    }}>
        <div className="box">
            <button className="close ms" onClick={() => close()}>close</button>
            <div className="title body-bold">{getText("add_material")}</div>
            <div className="content">
                <div className="radioButton">
                    <div className="option" data-select={selectType === 0} onClick={() => setSelectType(0)}>
                        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20.9999 16C19.7149 16 18.4724 15.4263 17.4999 14.385C16.5543 13.3694 15.9768 12.015 15.8749 10.5725C15.7662 9.03375 16.2356 7.61875 17.1962 6.5875C18.1568 5.55625 19.4999 5 20.9999 5C22.4893 5 23.8362 5.56625 24.7937 6.595C25.7606 7.63375 26.2312 9.04625 26.1224 10.5719C26.0181 12.0163 25.4412 13.37 24.4974 14.3844C23.5274 15.4263 22.2856 16 20.9999 16ZM29.2393 27H12.7612C12.4962 27.0014 12.2345 26.942 11.9961 26.8264C11.7578 26.7108 11.5491 26.542 11.3862 26.3331C11.2134 26.1066 11.094 25.844 11.0371 25.5649C10.9802 25.2857 10.9871 24.9973 11.0574 24.7213C11.5837 22.6081 12.8874 20.8556 14.8274 19.6538C16.5493 18.5875 18.7412 18 20.9999 18C23.3031 18 25.4374 18.5625 27.1693 19.6281C29.1137 20.8238 30.4193 22.5863 30.9431 24.725C31.0125 25.0013 31.0187 25.2897 30.9611 25.5687C30.9035 25.8477 30.7837 26.11 30.6106 26.3363C30.4478 26.5442 30.2396 26.7121 30.0019 26.8272C29.7642 26.9422 29.5034 27.0014 29.2393 27ZM9.18743 16.25C6.98805 16.25 5.0543 14.205 4.87493 11.6919C4.78618 10.4044 5.18743 9.21375 5.99993 8.34063C6.80368 7.47625 7.93743 7 9.18743 7C10.4374 7 11.5624 7.47875 12.3706 8.34813C13.1893 9.22813 13.5893 10.4163 13.4956 11.6931C13.3162 14.2056 11.3831 16.25 9.18743 16.25ZM13.2912 18.2156C12.1918 17.6781 10.7649 17.4094 9.18805 17.4094C7.3468 17.4094 5.55868 17.8894 4.15243 18.7606C2.55805 19.75 1.48555 21.1906 1.05243 22.93C0.989045 23.1802 0.98305 23.4415 1.03489 23.6943C1.08673 23.9471 1.19507 24.185 1.3518 24.39C1.50052 24.5809 1.69104 24.7352 1.90872 24.8409C2.1264 24.9467 2.36543 25.0011 2.60743 25H9.54493C9.66202 25 9.7754 24.9589 9.86528 24.8838C9.95517 24.8088 10.0159 24.7046 10.0368 24.5894C10.0437 24.55 10.0524 24.5106 10.0624 24.4719C10.5924 22.3431 11.8343 20.5444 13.6693 19.2331C13.7368 19.1845 13.7911 19.1198 13.8272 19.0448C13.8634 18.9699 13.8803 18.8871 13.8764 18.804C13.8725 18.7209 13.8479 18.6401 13.8048 18.5689C13.7618 18.4977 13.7017 18.4383 13.6299 18.3963C13.5318 18.3388 13.4193 18.2781 13.2912 18.2156Z" fill="black" />
                        </svg>
                        <span>{getText("material_roll_call")}</span>
                    </div>
                    <div className="option" data-select={selectType === 1} onClick={() => setSelectType(1)}>
                        <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M15 27.5H22.5C23.163 27.5 23.7989 27.2366 24.2678 26.7678C24.7366 26.2989 25 25.663 25 25V8.75L18.75 2.5H7.5C6.83696 2.5 6.20107 2.76339 5.73223 3.23223C5.26339 3.70107 5 4.33696 5 5V17.5" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            <path d="M17.5 2.5V7.5C17.5 8.16304 17.7634 8.79893 18.2322 9.26777C18.7011 9.73661 19.337 10 20 10H25M13 15.75C13.4973 15.2527 14.1717 14.9733 14.875 14.9733C15.5783 14.9733 16.2527 15.2527 16.75 15.75C17.2473 16.2473 17.5267 16.9217 17.5267 17.625C17.5267 18.3283 17.2473 19.0027 16.75 19.5L10 26.25L5 27.5L6.25 22.5L13 15.75Z" stroke="black" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                        </svg>

                        <span>{getText("material_assignment")}</span>
                    </div>
                    <div className="option" data-select={selectType === 2} onClick={() => setSelectType(2)}>
                        <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M18.6668 2.66669H8.00016C7.29292 2.66669 6.61464 2.94764 6.11454 3.44774C5.61445 3.94783 5.3335 4.62611 5.3335 5.33335V26.6667C5.3335 27.3739 5.61445 28.0522 6.11454 28.5523C6.61464 29.0524 7.29292 29.3334 8.00016 29.3334H24.0002C24.7074 29.3334 25.3857 29.0524 25.8858 28.5523C26.3859 28.0522 26.6668 27.3739 26.6668 26.6667V10.6667L18.6668 2.66669ZM24.0002 26.6667H8.00016V5.33335H17.3335V12H24.0002V26.6667Z" fill="black" />
                        </svg>
                        <span>{getText("material_file")}</span>
                    </div>
                </div>
                <div className="info">
                    <div className="body-bold">用途</div>
                    <ul>
                        <li>繳交任何數位內容（檔案），如文件、試算表、圖片或多媒體。</li>
                        <li>運用平台內建的文字編輯器繳交純文字檔案。</li>
                        <li>提醒學生完成“真實世界”的作業，例如手工作品。</li>
                    </ul>
                    <div className="body-bold">批改作業</div>
                    <ul>
                        <li>寫評語、上傳檔案回饋學生。例如已批注的學生作業、有評語的檔案或是語音回饋。</li>
                        <li>用數字或等第對作業評分，也可以用自訂的指標、進階的評分方式〈例如評量規準〉。最終成績將會記錄在成績單中。</li>
                    </ul>
                </div>
            </div>
            <div className="buttonBar">
                <button
                    className="cancel caption-bold"
                    onClick={() => close()}
                >{getText("cancel")}</button>
                <button
                    className="next caption-bold"
                    disabled={selectType === -1}
                    onClick={() => {
                        if (closeBeforeCallback !== false) {
                            close();
                        }
                        callback(selectType);
                    }}
                >{getText("next")}</button>
            </div>
        </div>
    </div>
};
