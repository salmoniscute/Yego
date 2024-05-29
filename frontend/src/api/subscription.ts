import axios from "axios";

export async function create_subscription(uid: String, component_id: number) {
  let url = `http://localhost:8080/api/subscription?`;
  try {
      const response = await axios.post(url+"uid="+uid+"&component_id="+component_id);
  }
  catch {  
      console.log("hi");
  }
}

export async function cancel_subscription(uid: String, component_id: number) {
  let url = `http://localhost:8080/api/subscription/${uid}/${component_id}`;
  try {
      const response = await axios.delete(url);
  }
  catch {  
      console.log("hi");
  }
}