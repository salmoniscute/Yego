import { MaterialAssignment } from "./materialAssignment";
import { MaterialInfo } from "./materialInfo";

export interface Material {
    id: number,
    title: string,
    order: number,
    material_infos: Array<MaterialInfo>,
    assignments: Array<MaterialAssignment>
};
