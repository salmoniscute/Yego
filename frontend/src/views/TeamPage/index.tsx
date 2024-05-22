import {
  ReactElement,
  useContext,
  CSSProperties,
  useState,
  useEffect
} from "react";

import userDataContext from "context/userData";

import ManaulTeam from "components/ManualTeam";
import AutoTeam from "components/AutoTeam";
import SelfTeam from "components/SelfTeam";

import { get_all_groups_info } from "api/group";
import { Group } from "schemas/group";

import "./index.scss";

export default function TeamPage(): ReactElement {
  const userData = useContext(userDataContext);

  const [selectMethod, setSelectMethod] = useState("");
  const [showWork, setShowWork] = useState<boolean>(false);
  const [groups, setgroups] = useState<Group[]>([]);
  const [listRender, setlistRender] = useState<JSX.Element[]>();

  const closeWindow = () =>{
    setShowWork(false);
    showGroups();
  }

  type Option = {
    label: string;
  };
  const teamOptions = (): Option[] => [
    { label: "自動分組" },
    { label: "學生自行分組" },
    { label: "手動建立新群組"}
  ];

  const showGroups = async () => {
    await get_all_groups_info("CSE101").then(data => {
      if(data) setgroups(data);
    });
    console.log(groups);
  }

  useEffect(() => {
    showGroups();
    if (groups.length > 0) {
      const renderedList = groups.map((group) => (
        <div key={group.name} className="groups">
          <p>第{group.name}組</p>
          <div className="members">
            {group.members.map(member => (
            <p>{member.name}</p>
            ))}  
        </div>
        </div>
      ));
      setlistRender(renderedList);
    }
  }, []);

  useEffect(() => {
    if (groups.length > 0) {
      const renderedList = groups.map((group) => (
        <div key={group.name} className="group">
          <p className="name">第{group.name}組</p>
          <div className="members">
            {group.members.map(member => (
            <p>{member.name}</p>
            ))}  
        </div>
        </div>
      ));
      setlistRender(renderedList);
    }
  }, [groups]);

  return (
      <div id="teamPage">
        <h1>分組設定</h1>
        
        <label className="dropdownMenu">
          <div className="button">建立群組</div>
          <input type="checkbox" />
          <div className="mask" style={{ "--length": 3 } as CSSProperties}>
            <div className="content body-bold">
              { teamOptions().map((option, i) => <div
              key={i}
              onClick={()=> {
                setShowWork(true);
                setSelectMethod(option.label);
              }}
              ><p>{option.label}</p></div>)
              }
            </div>
          </div>
        </label>
        <h2>群組總覽</h2>

        <div className="selectedWork" data-show={showWork} >
            { selectMethod === "手動建立新群組" && <div className="manual">
              <ManaulTeam close={closeWindow}/>
            </div>}
            { selectMethod === "自動分組" && <div className="auto">
              <AutoTeam close={closeWindow}/>
            </div>}
            { selectMethod === "學生自行分組" && <div className="byStudent" >
              <SelfTeam close={closeWindow}/>
            </div>}
            <div className="close ms" onClick={() => {}}>close</div>
        </div>
        <div className="groups">
          <div className="header">
            <p className="nameTitle">組別名稱</p>
            <p className="memberTitle">成員名稱</p>
          </div>
          {listRender}
        </div>
      </div>
  )
}