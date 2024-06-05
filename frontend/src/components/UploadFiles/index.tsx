import {
    CSSProperties,
    DragEvent,
    ReactElement,
    useContext,
    useEffect,
    useState
} from "react";

import "./index.scss";
import functionContext from "context/function";

type propsType = Readonly<{
    show: boolean,
    closeBeforeCallback?: boolean,
    initFiles: Array<File>,
    close: () => void,
    callback: (files: Array<File>) => void
}>;

const fileSource: Array<string> = [
    "從電腦上傳",
    // "已上傳的檔案",
];

const licenceList: Array<string> = [
    "保留所有著作權",
    "公共領域",
    "創用CC",
    "創用CC 禁止改作",
    "創用CC 非商用性、禁止改作",
    "創用CC 非商用性、相同方式分享",
    "創用CC 相同方式分享",
    "其他",
];

const sizeToString = (size: number) => {
    if (size < 1024) return `${size}B`;
    size /= 1024;
    if (size < 1024) return `${size.toFixed(1)}KB`;
    size /= 1024;
    if (size < 1024) return `${size.toFixed(1)}MB`;
    size /= 1024;
    return `${size.toFixed(1)}GB`;
}

export default function UploadFiles(
    props: propsType
): ReactElement {
    const {
        show,
        closeBeforeCallback,
        initFiles,
        close,
        callback,
    } = props;

    const [currentSource, setSource] = useState<number>(0);
    const [currentLicence, setLicence] = useState<number>(0);
    // const [filename, setFilename] = useState<string>("");
    const [uploadFiles, setUploadFiles] = useState<Array<File>>([]);
    const [onDrag, setOnDrag] = useState<boolean>(false);

    useEffect(() => {
        setUploadFiles(initFiles);
    }, [initFiles]);

    const {
        getText,
    } = useContext(functionContext);

    return <div className="uploadFiles" data-show={show}>
        <div className="box">
            <button className="close ms" onClick={() => close()}>close</button>
            <div className="title body-bold">檔案選擇</div>
            <div className="content">
                <div className="setting">
                    <div className="source dropdown">
                        <label className="mask" style={{
                            "--options": fileSource.length
                        } as CSSProperties}>
                            <div>{fileSource[currentSource]}</div>
                            {fileSource.map((v, i) => <div
                                key={i}
                                className="option"
                                onClick={() => setSource(i)}
                            >{v}</div>)}
                            <input type="checkbox" />
                        </label>
                    </div>
                    {/* <div className="filename">
                        <input type="text" onChange={(event) => {
                            setFilename(event.target.value)
                        }} value={filename} />
                    </div> */}
                    <div className="licence dropdown">
                        <label className="mask" style={{
                            "--options": licenceList.length
                        } as CSSProperties}>
                            <div>{licenceList[currentLicence]}</div>
                            {licenceList.map((v, i) => <div
                                key={i}
                                className="option"
                                onClick={() => setLicence(i)}
                            >{v}</div>)}
                            <input type="checkbox" />
                        </label>
                    </div>
                </div>
                <div className="files">
                    <div
                        className="dragBox"
                        onDrop={(event: DragEvent<HTMLDivElement>) => {
                            event.preventDefault();
                            Array.from(event.dataTransfer.items).forEach(item => {
                                const file = item.getAsFile();
                                if (file === null) return;
                                setUploadFiles(v => {
                                    if (v.map(u => u.name).includes(file.name)) {
                                        return v;
                                    }
                                    return [...v, file];
                                })
                            });
                            setOnDrag(false);
                        }}
                        onDragOver={(ev) => ev.preventDefault()}
                    >
                        <label
                            onDragEnter={() => setOnDrag(true)}
                            onDragLeave={() => setOnDrag(false)}
                            data-ondrag={onDrag}
                        >
                            {
                                uploadFiles.length === 0 ? <input type="file" onChange={(event) => {
                                    setUploadFiles(v => Array.from(event.target.files ?? []));
                                }} /> : undefined
                            }
                            {uploadFiles.length === 0 ? <div className="empty">
                                將檔案拖曳自此上傳
                            </div> : <div>
                                {uploadFiles.map((file, i) => <div
                                    key={`${file.name}${i}`}
                                    className="file"
                                >
                                    <span
                                        className="name"
                                        onClick={() => {setUploadFiles(v => {
                                            return v.filter(u => u.name !== file.name);
                                        })}}
                                    >{file.name}</span>
                                    <span className="size">{sizeToString(file.size)}</span>
                                </div>)}    
                            </div>}
                        </label>
                    </div>
                    {/* <div className="subtitle">最近使用</div>
                    <div className="list">
                        <FilesIcon iconType="PPT" filename="TestTestTestTestTestTestTestTestTestTestTestTestTestTest"/>
                        <FilesIcon iconType="WORD" filename="TestTestTestTestTestTestTestTestTestTestTestTestTestTest"/>
                        <FilesIcon iconType="PDF" filename="TestTestTestTestTestTestTestTestTestTestTestTestTestTest"/>
                        <FilesIcon filename="TestTestTestTestTestTestTestTestTestTestTestTestTestTest"/>
                    </div> */}
                </div>
            </div>
            <div className="buttonBar">
                <button
                    className="cancel caption-bold"
                    onClick={() => close()}
                >{getText("cancel")}</button>
                <button
                    className="next caption-bold"
                    onClick={() => {
                        if (closeBeforeCallback !== null)
                            close();
                        callback(uploadFiles);
                    }}
                >{getText("confirm")}</button>
            </div>
        </div>
    </div>;
};
