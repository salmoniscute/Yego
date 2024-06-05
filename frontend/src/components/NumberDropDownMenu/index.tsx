import { ReactElement, useMemo, useState } from "react";

import "./index.scss";

type propsType = Readonly<{
    rangeStart: number,
    rangeEnd: number,
    value: number,
    setValue: (value: number) => void
}>;

export default function NumberDropDownMenu(props: propsType): ReactElement {
    const {
        rangeStart,
        rangeEnd,
        value,
        setValue
    } = props;

    const [open, setOpen] = useState<boolean>(false);

    const allValue: Array<number> = useMemo(() => {
        const length = rangeEnd - rangeStart + 1;
        return Array.from(Array(length)).map((_, i) => rangeStart + i)
    }, [rangeStart, rangeEnd]);

    return <div className="numberDropDownMenu" data-open={open}>
        <div className="mask">
            <div className="content" onClick={() => {setOpen(v => !v);}}>
                <span>{value}</span>
                <span className="ms">keyboard_arrow_down</span>
            </div>
            <div className="values">
                {
                    allValue.map((v) => <div
                        key={v}
                        className="value"
                        onClick={() => {
                            setValue(v);
                            setOpen(false);
                        }}
                    >{v}</div>)
                }
            </div>
        </div>
    </div>;
};
