import {
  useEffect,
  useState,
} from "react";
import { RxCross2 } from "react-icons/rx";
import Select from 'react-select';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
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

  let minuteOptions = [
      { value: "0", label: "00" }
  ];
  let hourOptions = [
    { value: "0", label: "00" }
  ];

  const [selectedDate, setSelectedDate] = useState<Date | null>(null);

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
  
  useEffect(() => {
    for (let i = 1; i < 60; i++) {
      const value = i.toString();
      const label = i.toString().padStart(2, '0');
      minuteOptions.push({ value: value, label: label });
    }
    for (let i = 1; i < 24; i++) {
      const value = i.toString();
      const label = i.toString().padStart(2, '0');
      hourOptions.push({ value: value, label: label });
    }
    const currentDate = new Date();
    setSelectedDate(currentDate);
  }, []);

  return (
      <div id="selfTeam">
          <RxCross2 className="closeCross" onClick={close}/>
          <p>由教師建立空群組，讓學生自行加入。</p>
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

          <div className="optionGroup">
              <p>截止時間</p>
              <DatePicker
                selected={selectedDate}
                onChange={handleDateChange}
                dateFormat="yyyy-MM-dd"
              />
              <div className="selectOption">
                  <Select
                      className="basic-single"
                      classNamePrefix="select"
                      placeholder = "時"
                      options={hourOptions}
                      styles={customStyles}
                  />
              </div>
              <div className="selectOption">
                  <Select
                      className="basic-single"
                      classNamePrefix="select"
                      placeholder = "分"
                      options={minuteOptions}
                      styles={customStyles}
                  />
              </div>
          </div>

          <div className="buttons">
              <button className="cancel" onClick={close}>取消</button>
              <button className="confirm">預覽</button>
          </div>

      </div>
  );
}
function dayjs(startDate: any) {
  throw new Error("Function not implemented.");
}

