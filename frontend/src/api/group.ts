import axios from 'axios';
import { Group } from 'schemas/group';

export async function get_auto_team_preview(grouping_method: string, number_depend_on_grouping_method: number, distributing_method: string, naming_rule: string, course_id: string): Promise<Group[]> {
  let groups = [];
  let url = `http://localhost:8080/api/grouping/auto/preview?`;
  try {
      const response = await axios.get(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&distributing_method="+distributing_method+"&naming_rule="+naming_rule+"&course_id="+course_id);
      groups = response.data;
      console.log(groups);
  }
  catch {  
      console.log("hi");
  }
  return groups;
}

export async function cancel(course_id: string) {
  let url = `http://localhost:8080/api/grouping/auto/cancel?`;
  try {
      const response = await axios.delete(url+"course_id="+course_id);
      console.log("delete success");
  }
  catch {  
      console.log("hi");
  }
}

export async function post_auto(course_id: string) {
  let url = `http://localhost:8080/api/grouping/auto?`;
  try {
      const response = await axios.post(url+"course_id="+course_id);
      console.log("post auto groups success");
  }
  catch {  
      console.log("hi");
  }
}

export async function post_team_by_student(grouping_method: string, number_depend_on_grouping_method: number, naming_rule: string, create_deadline: string,  course_id: string) {
  let url = `http://localhost:8080/api/grouping/student?`;
  try {
      console.log(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&naming_rule="+naming_rule+"&create_deadline="+create_deadline+"&course_id="+course_id);
      const response = await axios.post(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&naming_rule="+naming_rule+"&create_deadline="+create_deadline+"&course_id="+course_id);
      console.log("post empty groups success");
  }
  catch {  
      console.log("hi");
  }
}

export async function get_all_groups_info(course_id: string): Promise<Group[]> {
  let groups = [];
  let url = `http://localhost:8080/api/group/info/${course_id}`;
  try {
      const response = await axios.get(url);
      groups = response.data;
      console.log(groups);
  }
  catch {  
      console.log("hi");
  }
  return groups;
}