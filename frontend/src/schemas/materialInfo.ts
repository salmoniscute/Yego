import { MaterialFile } from "./materialFile";

export interface MaterialInfo {
    id: number,
    title: string,
    content: string,
    start_time: string,
    end_time: string,
    display: boolean,
    order: number,
    files: Array<MaterialFile>
}