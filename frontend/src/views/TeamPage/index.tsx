import {
  ReactElement,
  useContext,
  CSSProperties,
  useState,
  MouseEvent
} from "react";

import userDataContext from "context/userData";

import ManaulTeam from "components/ManualTeam";

import "./index.scss";

export default function TeamPage(): ReactElement {
  const userData = useContext(userDataContext);

  const [selectMethod, setSelectMethod] = useState("");
  const [showWork, setShowWork] = useState<boolean>(false);

  type Option = {
    label: string;
  };
  const teamOptions = (): Option[] => [
    { label: "自動分組" },
    { label: "學生自行分組" },
    { label: "手動建立新群組"}
  ];

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
              <h3>{selectMethod} - 設定</h3>
              <ManaulTeam/>
            </div>}
            { selectMethod === "自動分組" && <div className="auto">
            </div>}
            { selectMethod === "學生自行分組" && <div className="byStudent" >
            </div>}
            <div className="close ms" onClick={() => {}}>close</div>
        </div>

      </div>
  )
}