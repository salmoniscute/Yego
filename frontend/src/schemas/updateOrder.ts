export default interface UpdateOrder {
    id: number,
    order: number,
    type: "material_info" | "assignment" | ""
};
