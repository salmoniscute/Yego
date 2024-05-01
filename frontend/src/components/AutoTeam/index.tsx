import {
    useEffect,
    useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import Select from 'react-select';
import "./index.scss";

type propsType = Readonly<{
    close : () => void

}>;

export default function AutoTeam(props:propsType): React.ReactElement {

    const {
        close,
    } = props;
    const [groupingMethod, setGroupingMethod] = useState<string | null>(null);
    const [namingMethod, setNamingMethod] = useState<string | null>(null);

    const numberOptions = [
        { value: "1", label: "1" },
        { value: "2", label: "2" },
        { value: "3", label: "3" },
    ];
    const methodOptions = [
        { value: "隨機", label: "隨機" },
        { value: "依姓氏", label: "依姓氏" },
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
    
    return (
        <div id="autoTeam">
            <RxCross2 className="closeCross" onClick={close}/>
            <div className="optionGroup">
                <p>分組方式</p>
                <div>
                    <div className="selectOption">
                        <input type="checkbox" checked={groupingMethod === "組別"}
                                onChange={() => setGroupingMethod("組別")} id="checkboxGroup"/>
                        <label htmlFor="checkboxGroup" className="checkboxLabel"></label>
                        <p>依組別數 , 分成</p>
                        <Select
                            className="basic-single"
                            classNamePrefix="select"
                            placeholder = "組數"
                            options={numberOptions}
                            styles={customStyles}
                        />
                    </div>
                    <div className="selectOption"> 
                        <input type="checkbox" checked={groupingMethod === "成員"}
                                onChange={() => setGroupingMethod("成員")} id="checkboxMember"/>
                        <label htmlFor="checkboxMember" className="checkboxLabel"></label>
                        <p>依成員數 , 分成</p>
                        <Select
                            className="basic-single"
                            classNamePrefix="select"
                            placeholder = "人數"
                            options={numberOptions}
                            styles={customStyles}
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
                    />
                </div>
            </div>

            <div className="optionGroup">
                <p>命名規則</p>
                <div>
                    <div className="selectOption" >
                        <input type="checkbox" checked={namingMethod === "字母"}
                                onChange={() => setNamingMethod("字母")} id="checkboxLetter"/>
                        <label htmlFor="checkboxLetter" className="checkboxLabel"></label>
                        <p>字母編號</p>
                    </div>
                    <div className="selectOption"> 
                        <input type="checkbox" checked={namingMethod === "數字"}
                                onChange={() => setNamingMethod("數字")} id="checkboxNumber"/>
                        <label htmlFor="checkboxNumber" className="checkboxLabel"></label>
                        <p>數字編號</p>
                       
                    </div>
                </div>
            </div>

            <div className="buttons">
                <button className="cancel" onClick={close}>取消</button>
                <button className="confirm">預覽</button>
            </div>

        </div>
    );
}
