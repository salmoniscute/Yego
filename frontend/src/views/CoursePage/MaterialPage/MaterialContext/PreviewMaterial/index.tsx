import axios from "axios";
import { ReactElement, useCallback, useEffect, useRef, useState } from "react";
import { MaterialAssignment } from "schemas/materialAssignment";
import { MaterialInfo } from "schemas/materialInfo";

import "./index.scss";

type propsType = Readonly<{
    data: MaterialInfo | MaterialAssignment | null,
    close: () => void,
}>;

export default function PreviewMaterial(props: propsType): ReactElement {
    const {
        data,
        close
    } = props;

    const aRef = useRef<HTMLAnchorElement>(null);
    const [displayData, setDisplayData] = useState<MaterialInfo | MaterialAssignment>();

    const downloadFile = useCallback((fileId: number, fileName?: string) => {
        axios.get(`/file?file_id=${fileId}`, {
            responseType: "blob"
        }).then(r => {
            const file: Blob = r.data;

            const url = URL.createObjectURL(file);
            if (aRef.current !== null) {
                aRef.current.href = url;
                if (fileName)
                    aRef.current.download = fileName;
                aRef.current.click();
                URL.revokeObjectURL(url);
                // aRef.current.download = v.files[0].path.split("/").reverse()[0]
            }
        })
    }, [aRef]);

    useEffect(() => {
        if (data === null)
            return;
        setDisplayData(data);
    }, [data]);

    return <div id="previewMaterial" data-show={data !== null} onClick={(event) => {
        const target: HTMLElement = event.target as HTMLElement;
        if (target.id === "previewMaterial") {
            close();
        }
    }}>
        <div className="box">
            <button className="close ms" onClick={() => close()}>close</button>
            <img src={`${process.env.PUBLIC_URL}/assets/Yegogo.png`} />
            <div className="title body-bold">{displayData?.title}</div>
            <div className="description row">
                <div className="subtitle">
                    說明
                </div>
                <div className="rowContext">
                    {displayData?.content}
                </div>
            </div>
            {
                displayData && "start_time" in displayData ? <div
                    className="time row"
                >
                    <div className="subtitle">啟用時間</div>
                    <div className="rowContext">{displayData.start_time}</div>
                </div> : undefined
            }
            {
                displayData && "end_time" in displayData ? <div
                    className="time row"
                >
                    <div className="subtitle">停用時間</div>
                    <div className="rowContext">{displayData.end_time}</div>
                </div> : undefined
            }
            <div className="files row">
                <div className="subtitle">
                    檔案清單
                </div>
                <div className="rowContext">
                    {
                        displayData?.files.length !== 0 ? displayData?.files.map((v, i) => {
                            const fileName = v.path.match(/[^\/]+$/)?.[0];
                            if (fileName === undefined)
                                return undefined;

                            return <div
                                key={`${v.path}${i}`}
                                className="file"
                                onClick={() => downloadFile(v.id, fileName)}
                                title={fileName}
                            >{fileName}</div>;
                        }) : <div>無</div>
                    }
                </div>
            </div>
            <a ref={aRef} href="/" />
        </div>
    </div>
};
