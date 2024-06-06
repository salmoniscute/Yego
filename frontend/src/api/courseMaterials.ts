import axios, { AxiosError } from "axios";
import { Material } from "schemas/material";

export async function getMaterials(courseId: number): Promise<Array<Material>> {
    let data: Array<Material> = [];
    try {
        const response = await axios.get(`/course_material/particular_course/${courseId}`);
        data = response.data;
    }
    catch (error) {}


    return data.map(v => {
        if (v.order === undefined) {
            return Object.assign({order: 0}, v);
        }
        return v;
    })
}

export async function createMaterial(uid: string, courseId: number, title: string) {
    await axios.post(`/course_material?uid=${uid}&course_id=${courseId}`, {
        title: title
    });
}

export async function createMaterialInfo(uid: string, courseMaterialId: number, data: {
    "content": string,
    "display": boolean,
    "end_time": string,
    "start_time": string,
    "title": string
}) {
    await axios.post(`/material_info?uid=${uid}&course_material_id=${courseMaterialId}`, data);
}

export async function createAssignment(uid: string, courseMaterialId: number, data: {
    "content": string,
    "deadline": string,
    "display": boolean,
    "feedback_type": string,
    "reject_time": string,
    "submitted_object": string,
    "submitted_time": string,
    "submitted_type": string,
    "title": string
}) {
    await axios.post(`/assignment?uid=${uid}&course_material_id=${courseMaterialId}`, data);
}
