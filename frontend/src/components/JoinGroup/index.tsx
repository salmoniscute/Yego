import {
  useEffect,
  useState,
  useContext,
  useCallback
} from "react";

import "./index.scss";

import { get_user_group_info } from "api/group";

import userDataContext from "context/userData";
import { useParams } from "react-router-dom";

import JoinGroupModel from "components/JoinGroupModel";

export default function JoinGroup(): React.ReactElement {
  const [group, setGroup] = useState<String>("");
  const [showJoin, setshowJoin] = useState<Boolean>(false);
  const userData = useContext(userDataContext);
  const params = useParams();

  const close = () => {
    setshowJoin(false);
  }

  const get_group = useCallback(async () => {
    const data = await get_user_group_info(userData ? userData.uid : null, Number(params.courseID));
    if(data == null) setGroup("");
    else setGroup(data);
    console.log(group);
  }, [userData, params.courseID]);

  useEffect(() => {
    get_group();
  }, [get_group]);

  useEffect(() => {
    get_group();
  }, [showJoin, get_group]);

  return (
      <div id="joinGroup">
        <button onClick={() => {setshowJoin(true)}}>
          <img alt="yego" src="/assets/Yegogo.png"/>{group === "" ? <p><span className="no">尚未加入</span>YEGO注意到你還沒有自己的組別，趕快加入！</p> : <p><span className="yes">已加入</span>你已經找到你的好隊友了，棒棒！</p>}
        </button>
        {showJoin ? <JoinGroupModel close={close} course_id={Number(params.courseID)}/> : ""}
      </div>
  );
}