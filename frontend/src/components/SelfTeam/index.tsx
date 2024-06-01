import {
  useEffect,
  useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import Select from 'react-select';
import moment from 'moment';
import DatePicker from "react-datepicker";
import "react-datepicker/src/stylesheets/datepicker.scss";
import "./index.scss";

import { post_team_by_student } from "api/group";
import { getCourseMemberList } from "api/courseMember";

type propsType = Readonly<{
  close : () => void,
  course_id: number
}>;

export default function AutoTeam(props:propsType): React.ReactElement {

  const {
      close,
  } = props;
  const [groupingMethod, setGroupingMethod] = useState<string | null>(null);
  const [number, setnumber] = useState<number>(0);
  const [namingMethod, setNamingMethod] = useState<string | null>(null);
  const [studentNum, setstudentNum] = useState<number>(0);

  const numberOptions = [
      { value: 1, label: "1" },
  ];

  let minuteOptions = [
      { value: 0, label: "00" }
  ];
  let hourOptions = [
    { value: 0, label: "00" }
  ];

  const [selectedDate, setSelectedDate] = useState<Date | null>(new Date());
  const [hour, sethour] = useState<string>("");
  const [minute, setminute] = useState<string>("");

  const handleDateChange = (date: Date | null) => {
    setSelectedDate(date);
  };
  //https://liuyuqin1991.github.io/react-datepicker/doc-date-picker

  const customStyles = {
      control: (provided: any, state: any) => ({
          ...provided,
          width : "6em",
          margin: "0 0.1rem",
          fontSize : "15px",
          border:  "1px solid #ccc",
          boxShadow: "none",
          "&:hover": {
              border: "1px solid #c1c1c1",
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
  
  const grouping = async () => {
    if(groupingMethod && number && namingMethod && selectedDate && hour && minute && props.course_id){
        await post_team_by_student(groupingMethod, number, namingMethod, moment(selectedDate).format('YYYY-MM-DD')+" "+hour+":"+minute+":00", props.course_id);
        close();
    }
    else alert("請勾選所有項目");
}

const get_members_number = async () => {
    await getCourseMemberList(props.course_id).then(data => {
        if(data) setstudentNum(data.filter(user => user.role === "student").length);
    });
}

  useEffect(() => {
    get_members_number();
    if(studentNum > 0){
        for (let i = 2; i <= studentNum; i++) { // generate dynamic options for number choice
            const value = i;
            const label = i.toString();
            numberOptions.push({ value: value, label: label });
        }
    }
    for (let i = 1; i < 60; i++) {
      const value = i;
      const label = i.toString().padStart(2, '0');
      minuteOptions.push({ value: value, label: label });
    }
    for (let i = 1; i < 24; i++) {
      const value = i;
      const label = i.toString().padStart(2, '0');
      hourOptions.push({ value: value, label: label });
    }
  });

  return (
      <div id="selfTeam">
        <div className="header">
            <h3>學生自行分組 - 設定</h3>
            <RxCross2 className="closeCross" onClick={close}/>
        </div>
        <p>由教師建立空群組，讓學生自行加入。</p>
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

        <div className="optionGroup">
            <p>截止時間</p>
            <DatePicker
                selected={selectedDate}
                onChange={handleDateChange}
                dateFormat="yyyy-MM-dd"
                className="datePicker"
            />
            <div className="selectOption">
                <Select
                    className="basic-single"
                    classNamePrefix="select"
                    placeholder = "時"
                    options={hourOptions}
                    styles={customStyles}
                    onChange={(selectedOption) => {
                        if (selectedOption) {
                            sethour(selectedOption.label);
                        }
                    }}
                />
            </div>
            <div className="selectOption">
                <Select
                    className="basic-single"
                    classNamePrefix="select"
                    placeholder = "分"
                    options={minuteOptions}
                    styles={customStyles}
                    onChange={(selectedOption) => {
                        if (selectedOption) {
                            setminute(selectedOption.label);
                        }
                    }}
                />
            </div>
        </div>
        <div className="buttons">
            <button className="confirm" onClick={grouping}>確定</button>
            <button className="cancel" onClick={close}>取消</button>
        </div>
      </div>
  );
}
function dayjs(startDate: any) {
  throw new Error("Function not implemented.");
}

