import {
    useEffect,
    useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import Select from 'react-select';
import "./index.scss";
import { get_auto_team_preview, cancel, post_auto } from "api/group";
import { Group } from "schemas/group";

type propsType = Readonly<{
    close : () => void

}>;

export default function AutoTeam(props:propsType): React.ReactElement {
    const {
        close,
    } = props;
    const [showPreview, setshowPreview] = useState(false);
    const [groups, setgroups] = useState<Group[]>([]);
    const [groupingMethod, setGroupingMethod] = useState<string | null>(null);
    const [number, setnumber] = useState<number>(0);
    const [namingMethod, setNamingMethod] = useState<string | null>(null);
    const [distributeMethod, setdistributeMethod] = useState<string| null>("random");
    const [listRender, setlistRender] = useState<JSX.Element[]>();

    const numberOptions = [
        { value: 1, label: "1" },
    ];
    const methodOptions = [
        { value: "random", label: "隨機" },
        { value: "first_name", label: "依姓氏" },
    ];

    const customStyles = {
        control: (provided: any, state: any) => ({
            ...provided,
            width : "6em",
            fontSize : "15px",
            border:  "1px solid #ccc",
            boxShadow: "none",
            "&:hover": {
                border: "1px solid #c1c1c1"
            }
        }),
        option: (provided: any, state: any) => ({
            ...provided,
            fontSize : "15px",
            textAlign:"start",
            backgroundColor: "white",
            color: "black",
            "&:hover": {
                backgroundColor: "#c1c1c1",
                color: "white"
            }
        })
    };

    const grouping = async () => { //course_id 待改
        if(groupingMethod && number && distributeMethod && namingMethod){
            await get_auto_team_preview(groupingMethod, number, distributeMethod, namingMethod, "CSE101").then(data => {
                if(data) setgroups(data);
              });
            console.log(groups);
            if(groups) {
                setlistRender(groups.map((group) => { 
                    return <div key={group.name} className="group">
                            <h3>第{group.name}組</h3>
                                <div className="members">
                                    {group.members.map(member => (
                                    <p>{member.name}</p>
                                    ))}  
                                </div>
                            </div>}));
                setshowPreview(true);
            }
        }
        else alert("請勾選所有項目");
    }
    
    const lastStep = () => {
        cancel("CSE101");
        setshowPreview(false);
    }

    const confirm = () => {
        post_auto("CSE101");
        setshowPreview(false);
        close();
        setGroupingMethod(null);
        setNamingMethod(null);
        setnumber(0);
        setdistributeMethod("random");
    }
    useEffect(() => {
        for (let i = 2; i <= 24; i++) { // generate dynamic options for number choice
            const value = i;
            const label = i.toString();
            numberOptions.push({ value: value, label: label });
        }
    });
    useEffect(() => {
        if (groups.length > 0) {
          const renderedList = groups.map((group) => (
            <div key={group.name} className="group">
              <h3>第{group.name}組</h3>
              <div className="members">
                {group.members.map(member => (
                <p>{member.name}</p>
                ))}  
            </div>
            </div>
          ));
          setlistRender(renderedList);
          setshowPreview(true);
        }
      }, [groups]);

    return (
        <div id="autoTeam">
            <RxCross2 className="closeCross" onClick={() => {
                close();
                if(showPreview === true) cancel("CSE101"); 
                setshowPreview(false);
                setGroupingMethod(null);
                setNamingMethod(null);
                setnumber(0);
                setdistributeMethod("random");
            }}/>
            <div className={showPreview === false ? "setting" : "hide"} data-show={showPreview}>
                <h3>自動分組 - 設定</h3>
                <div className="optionGroup">
                    <p>分組方式</p>
                    <div>
                        <div className="selectOption">
                            <input type="checkbox" checked={groupingMethod === "numbers_of_groups"}
                                    onChange={() => setGroupingMethod("numbers_of_groups")} id="checkboxGroup"/>
                            <label htmlFor="checkboxGroup" className="checkboxLabel"></label>
                            <p>依組別數 , 分成</p>
                            <Select
                                className="basic-single"
                                classNamePrefix="select"
                                placeholder = "組數"
                                options={numberOptions}
                                styles={customStyles}
                                onChange={(selectedOption) => {
                                    if (selectedOption) {
                                        setnumber(selectedOption.value);
                                    }
                                }}
                            />
                        </div>
                        <div className="selectOption"> 
                            <input type="checkbox" checked={groupingMethod === "numbers_of_members"}
                                    onChange={() => setGroupingMethod("numbers_of_members")} id="checkboxMember"/>
                            <label htmlFor="checkboxMember" className="checkboxLabel"></label>
                            <p>依成員數 , 分成</p>
                            <Select
                                className="basic-single"
                                classNamePrefix="select"
                                placeholder = "人數"
                                options={numberOptions}
                                styles={customStyles}
                                onChange={(selectedOption) => {
                                    if (selectedOption) {
                                        setnumber(selectedOption.value);
                                    }
                                }}
                            />
                        </div>
                    </div>
                </div>

                <div className="optionGroup">
                    <p>分配方式</p>
                    <div>
                        <Select
                            className="basic-single"
                            classNamePrefix="select"
                            defaultValue={methodOptions[0]}
                            options={methodOptions}
                            styles={customStyles}
                            onChange={(selectedOption) => {
                                if (selectedOption) {
                                    setdistributeMethod(selectedOption.value);
                                }
                            }}
                        />
                    </div>
                </div>

                <div className="optionGroup">
                    <p>命名規則</p>
                    <div>
                        <div className="selectOption" >
                            <input type="checkbox" checked={namingMethod === "alphabet"}
                                    onChange={() => setNamingMethod("alphabet")} id="checkboxLetter"/>
                            <label htmlFor="checkboxLetter" className="checkboxLabel"></label>
                            <p>字母編號</p>
                        </div>
                        <div className="selectOption"> 
                            <input type="checkbox" checked={namingMethod === "number"}
                                    onChange={() => setNamingMethod("number")} id="checkboxNumber"/>
                            <label htmlFor="checkboxNumber" className="checkboxLabel"></label>
                            <p>數字編號</p>
                        
                        </div>
                    </div>
                </div>

                <div className="buttons">
                    <button className="cancel" onClick={close}>取消</button>
                    <button className="confirm" onClick={grouping}>預覽</button>
                </div>
            </div>
            <div className={showPreview === true ? "preview" : "hide"} data-show={showPreview}>
                <h3>自動分組 - 預覽</h3>
                <div className="groupList">{listRender}</div>
                <div className="buttons">
                    <button className="cancel" onClick={lastStep}>上一步</button>
                    <button className="confirm" onClick={confirm}>確認</button>
                </div>
            </div>
        </div>
    );
}
