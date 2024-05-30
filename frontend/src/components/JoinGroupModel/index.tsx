import {
  useContext,
  useEffect,
  useState,
} from "react";
import "./index.scss";
import { RxButton, RxCross2 } from "react-icons/rx";
import { MdGroupAdd, MdGroupRemove } from "react-icons/md";

import { get_all_groups_info, join_group, exit_group, get_user_group_info } from "api/group";
import { Group } from "schemas/group";

import userDataContext from "context/userData";

type propsType = Readonly<{
  close : () => void,
  course_id: number
}>;

export default function JoinGroupModel(props:propsType): React.ReactElement {
  const {
      close,
      course_id
  } = props;

  const [groups, setgroups] = useState<Group[]>([]);
  const [group, setGroup] = useState<String>("");
  const [listRender, setlistRender] = useState<JSX.Element[]>();
  const userData = useContext(userDataContext);

  const showGroups = async () => {
    await get_all_groups_info(1).then(data => {
      if(data) setgroups(data);
    });
    console.log(groups);
  }

  const get_group = async () => {
    await get_user_group_info(userData ? userData.uid : null, props.course_id).then(data => {
      if(data == null) setGroup("");
      else setGroup(data);
      console.log(group);
    });
  }

  const exit = async () => {
    await exit_group(userData ? userData.uid : null, props.course_id);
    get_group();
    showGroups();
  }

  const join = async (data: Group) => {
    await join_group(userData ? userData.uid : null, props.course_id, data.id);
    get_group();
    showGroups();
  }

  useEffect(() => {
    showGroups();
    get_group();
  }, []);

  useEffect(() => {
    if (groups.length > 0) {
      get_group();
      const renderedList = groups.map((data, i) => (
        <div key={i} className="group">
          <h3>第{data.name}組</h3>
          <div className="members">
            {data.members.map(member => (
            <p>{member.name}</p>
            ))}  
          </div>
          {group === data.name ? <button className="exit" onClick={() => exit()}><MdGroupRemove />&nbsp;退出群組</button> : ""}
          {group === "" ? <button className="join" onClick={() => join(data)}><MdGroupAdd />&nbsp;加入群組</button> : ""}
        </div>
      ));
      setlistRender(renderedList);
    }
  }, [groups]);

  return (
    <div id="joinGroupModel">
      <RxCross2 className="closeCross" onClick={() => {
                close();
      }}/>
      <h3>加入分組</h3>
      <div className="groupList">{listRender}</div>
    </div>
  );
}
