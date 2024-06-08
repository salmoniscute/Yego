import axios from "axios";

export async function create_subscription(uid: String, component_id: number) {
  let url = `/subscription?`;
  try {
      await axios.post(url+"uid="+uid+"&component_id="+component_id);
  }
  catch {  
      console.log("hi");
  }
}

export async function cancel_subscription(uid: String, component_id: number) {
  let url = `/subscription/${uid}/${component_id}`;
  try {
      await axios.delete(url);
  }
  catch {  
      console.log("hi");
  }
}