import {
    useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import "./index.scss";

type propsType = Readonly<{
    close:()=>void
}>;

export default function ManaulTeam(props:propsType): React.ReactElement {

    const {
        close
    } = props;

    const [teamTitle , setTeamTitle] = useState("");

    type teamMember = {
        name: string;
        id:string;
    };

    const [teamMembers, setTeamMembers] = useState<teamMember[]>([
        { name: "鮭魚", id: "F74106050" },
        { name: "柯有倫", id: "F74106050" },
        { name: "皮卡丘", id: "F74106050" },
        { name: "葉子", id: "F74106050" },
        { name: "小明", id: "F74106050" },
        { name: "皓哥", id: "F74106050" },
        { name: "鮭魚", id: "F74106050" },
        { name: "柯有倫", id: "F74106050" },
        { name: "皮卡丘", id: "F74106050" },
        { name: "葉子", id: "F74106050" },
        { name: "小明", id: "F74106050" },
        { name: "皓哥", id: "F74106050" },
    ]);

    const deleteTeamMember = (index:number) => {
        const newTeamMembers = [...teamMembers]; 
        newTeamMembers.splice(index, 1); 
        setTeamMembers(newTeamMembers); 
    } ; 
    // const addTeamMember = () => {
    //     teamMembers.push();
    // } ; 
    
    return (
        <div id="manualTeam">
            <RxCross2 className="closeCross" onClick={close}/>
            <div className="setting">
            <h3>手動建立新分組 - 設定</h3>
                <div className="content">
                    <div className="left">
                        <div className="upper">
                            <p>群組名稱</p>
                            <input 
                                value={teamTitle}
                                onChange={(e) => setTeamTitle(e.target.value)}
                            >
                            </input>
                        </div>
                        <div className="upper">
                            <p>新增成員</p>
                            <input></input>
                        </div>
                    </div>
                    <div className="member">
                        <p>現有成員</p>
                        <div>
                            {
                                teamMembers.map(( data , i )=> <div className="memberCard" key={i}>
                                    <p>{data.name}</p>
                                    <RxCross2 className="icon" onClick={()=>deleteTeamMember(i)}/>
                                </div>
                            )}
                        </div>
                    </div>
                </div>

                <div className="buttons">
                    <button className="cancel" onClick={close}>取消</button>
                    <button className="confirm">確認</button>
                </div>
            </div>
        

        </div>
    );
}
