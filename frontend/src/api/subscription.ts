import axios from "axios";
import { Subscription } from "schemas/subscription";

export async function create_subscription(uid: String, component_id: String, type: String) {
  let url = `http://localhost:8080/api/subscription?`;
  let requestBody = {
    type: type
  };
  try {
      const response = await axios.post(url+"uid="+uid+"&component_id="+component_id, requestBody);
  }
  catch {  
      console.log("hi");
  }
}

export async function cancel_subscription(uid: String, component_id: String) {
  let url = `http://localhost:8080/api/subscription/${uid}/${component_id}`;
  try {
      const response = await axios.delete(url);
  }
  catch {  
      console.log("hi");
  }
}