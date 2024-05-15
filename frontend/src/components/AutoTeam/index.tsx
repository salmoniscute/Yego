import {
    useEffect,
    useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import Select from 'react-select';
import "./index.scss";
import { post_auto_team } from "api/group";
import { Group } from "schemas/group";

type propsType = Readonly<{
    close : () => void

}>;

export default function AutoTeam(props:propsType): React.ReactElement {

    const {
        close,
    } = props;
    const [groups, setgroups] = useState<Group[]>([]);
    const [groupingMethod, setGroupingMethod] = useState<string | null>(null);
    const [number, setnumber] = useState<number>(0);
    const [namingMethod, setNamingMethod] = useState<string | null>(null);
    const [distributeMethod, setdistributeMethod] = useState<string| null>(null);
    const [listRender, setlistRender] = useState<JSX.Element[]>();

    const numberOptions = [
        { value: 1, label: "1" },
        { value: 2, label: "2" },
        { value: 3, label: "3" },
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
            setgroups(await post_auto_team(groupingMethod, number, distributeMethod, namingMethod, "CSE101"));
            console.log(groups);
            if(groups) {
                console.log(groups[0].name);
                setlistRender(groups.map((item) => { 
                    return <div>
                            <h3>{item.name}</h3>
                            <p>{item.members}</p>
                            </div>}));
            }
        }
        else alert("請勾選所有項目");
    }
    

    return (
        <div>
            <div id="autoTeam">
                <RxCross2 className="closeCross" onClick={close}/>
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
                <div className="preview">
                    {listRender}
                </div>
            </div>
        </div>
    );
}
