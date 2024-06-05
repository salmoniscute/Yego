import { MaterialFile } from "./materialFile"

export interface MaterialAssignment {
    id: number
    title: string
    content: string
    submitted_type: string
    submitted_object: string
    display: boolean
    submitted_time: string
    deadline: string
    reject_time: string
    feedback_type: string
    files: Array<MaterialFile>
};
