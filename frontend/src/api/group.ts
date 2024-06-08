import axios from 'axios';
import { Group } from 'schemas/group';

export async function get_auto_team_preview(grouping_method: string, number_depend_on_grouping_method: number, distributing_method: string, naming_rule: string, course_id: number): Promise<Group[]> {
  let groups = [];
  let url = `/grouping/auto/preview?`;
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

export async function cancel(course_id: number) {
  let url = `/grouping/auto/cancel?`;
  try {
      await axios.delete(url+"course_id="+course_id);
      console.log("delete success");
  }
  catch {  
      console.log("hi");
  }
}

export async function post_auto(course_id: number) {
  let url = `/grouping/auto?`;
  try {
      await axios.post(url+"course_id="+course_id);
      console.log("post auto groups success");
  }
  catch {  
      console.log("hi");
  }
}

export async function post_team_by_student(grouping_method: string, number_depend_on_grouping_method: number, naming_rule: string, create_deadline: string,  course_id: number) {
  let url = `/grouping/student?`;
  try {
      console.log(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&naming_rule="+naming_rule+"&create_deadline="+create_deadline+"&course_id="+course_id);
      await axios.post(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&naming_rule="+naming_rule+"&create_deadline="+create_deadline+"&course_id="+course_id);
      console.log("post empty groups success");
  }
  catch {  
      console.log("hi");
  }
}

export async function get_all_groups_info(course_id: number): Promise<Group[]> {
  let groups = [];
  let url = `/grouping/${course_id}`;
  try {
      const response = await axios.get(url);
      groups = response.data;
      console.log(groups);
  }
  catch {  
      console.log("hi");
      groups = [];
  }
  return groups;
}

export async function get_user_group_info(uid: string | null, course_id: number): Promise<String | null> {
  let group = "";
  let url = `/selected_course/particular/${uid}/${course_id}`;
  try {
      const response = await axios.get(url);
      if(response.data !== null) group = response.data;
      console.log(group);
  }
  catch {  
      console.log("hi");
  }
  return group;
}

export async function join_group(uid: string | null, course_id: number, group_id: number) {
  let url = `/grouping/group/join?`;
  try {
      await axios.put(url + "uid=" + uid + "&course_id=" + course_id + "&group_id=" + group_id);
  }
  catch {  
      console.log("hi");
  }
}

export async function exit_group(uid: string | null, course_id: number) {
  let url = `/grouping/group/exit?`;
  try {
      await axios.put(url + "uid=" + uid + "&course_id=" + course_id);
  }
  catch {  
      console.log("hi");
  }
}