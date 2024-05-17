import { useState } from "react";
import { RxCross2 } from "react-icons/rx";
import 'react-datepicker/dist/react-datepicker.css';
import "./index.scss";

export default function TeamModifyModel(): React.ReactElement {
  const [isShow, setisShow] = useState(true);

  const close = () => {
    setisShow(false);
  }

  return <div id={isShow === true ? "teamModifyModel" : "none"}>
    <div className="box">
    <RxCross2 className="closeCross" onClick={close}/>
      <h3>是否確認刪除？</h3>
      <p>一旦刪除便不能復原</p>
      <div>
        <input type="checkbox"/>
        <label >今天不要再提醒我</label>
      </div>
      <div className="buttons">
          <button className="cancel" onClick={close}>取消</button>
          <button className="confirm">確認</button>
      </div>
    </div>
  </div>
}


