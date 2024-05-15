import axios from 'axios';
import { Group } from 'schemas/group';

export async function post_auto_team(grouping_method: string, number_depend_on_grouping_method: number, distributing_method: string, naming_rule: string, course_id: string): Promise<Group[]> {
  let groups = [];
  let url = `http://localhost:8080/api/grouping/auto?`;
  try {
      const response = await axios.post(url+"grouping_method="+grouping_method+"&number_depend_on_grouping_method="+number_depend_on_grouping_method+"&distributing_method="+distributing_method+"&naming_rule="+naming_rule+"&course_id="+course_id);
      groups = response.data;
      console.log(groups);
  }
  catch {  
      console.log("hi");
  }

  return groups;
}