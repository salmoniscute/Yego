import {
    CSSProperties,
    Dispatch,
    ReactElement,
    SetStateAction,
    useCallback,
    useContext,
    useMemo,
    useState
} from "react";
import { Link } from "react-router-dom";

import "./index.scss";
import getText, { localMap } from "utils/getText";
import languageContext from "context/language";

type propsType = Readonly<{
    setLanguage: Dispatch<SetStateAction<string>>,
}>;

export default function NavigateBar(props: propsType): ReactElement {
    const { setLanguage } = props;

    const languageCode = useContext(languageContext);

    const getTextWrap = useCallback((id: string) => {
        return getText(id, languageCode);
    }, [getText, languageCode]);

    const languageList: Array<string> = useMemo(
        () => Object.keys(localMap).map(
            key => getText("current_language", key)
        ),
        [localMap]
    );
    const changeLanguage: Array<() => void> = useMemo(
        () => Object.keys(localMap).map(
            key => () => setLanguage(key)
        ),
        [localMap]
    );

    return (
        <div id="navigateBar">
            <div className="logo">
                <h1>YEGO</h1>
            </div>
            <label className="dropdownMenu">
                <input type="checkbox" />
                <div className="ms">language</div>
                <div className="body-bold">{getTextWrap("current_language")}</div>
                <div className="ms dropDown">arrow_drop_down</div>
                <div className="mask" style={{ "--length": languageList.length } as CSSProperties}>
                    <div className="content body-bold">
                        {
                            languageList.map((name, i) => <div
                                key={i}
                                onClick={changeLanguage[i]}
                            ><p>{name}</p></div>)
                        }
                    </div>
                </div>
            </label>
            <Link className="loginButton body-bold" to={"/login"} >{getTextWrap("login")}</Link>
        </div>
    );
}
