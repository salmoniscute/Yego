import axios from "axios";

export async function uploadFile(component_id: number, files: Array<File>): Promise<boolean> {
    const formData = new FormData();
    files.forEach(file => {
        formData.append("files", file);
    })
    
    const response = await axios.post(
        `/file?component_id=${component_id}`,
        formData
    );

    return response.status === 204;
};
