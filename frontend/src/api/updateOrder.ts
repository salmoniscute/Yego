import axios from "axios";
import UpdateOrder from "schemas/updateOrder";

export async function updateCourseMaterialOrder(list: Array<UpdateOrder>) {
    await axios.post("/order_update/update_order/course_material", list);
}

export async function updateCourseInfoOrder(list: Array<UpdateOrder>) {
    await axios.post("/order_update/update_order/material_info_and_assignment", list);
}
