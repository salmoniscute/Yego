import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import "./index.scss";

const Overview = () => (
    <div>
        <div className="actions">
            <div className="square-button-container">
                <div className="square-button"></div>
                <span>全選</span>
            </div>
            <select className="select-action">
                <option value="">將選擇的項目</option>
                <option value="option1">動作1</option>
                <option value="option2">動作2</option>
                <option value="option3">動作3</option>
            </select>
            <select className="grading-action">
                <option value="">評分動作</option>
                <option value="grade1">評分1</option>
                <option value="grade2">評分2</option>
                <option value="grade3">評分3</option>
            </select>
        </div>
        <div className="title-row">
            <div>選擇</div>
            <div style={{ paddingLeft: '50px' }}>姓名</div>
            <div style={{ paddingLeft: '80px' }}>學號</div>
            <div style={{ paddingLeft: '80px' }}>科系名稱</div>
            <div style={{ paddingLeft: '80px' }}>狀態</div>
            <div style={{ paddingLeft: '120px' }}>檔案</div>
            <div style={{ paddingLeft: '120px' }}>成績</div>
            <div style={{ paddingLeft: '100px' }}>評語</div>
            <div style={{ paddingLeft: '100px' }}>編修</div>
        </div>
    </div>
);

const students = [
    { name: "張XX", fullName: "張維芹", id: "B34104065", department: "歷史系三年級", status: "檔案已繳交" },
    { name: "王XX", fullName: "王小明", id: "B34104066", department: "數學系二年級", status: "檔案未繳交" },
    { name: "柯XX", fullName: "柯有倫", id: "E64096300", department: "土木系四年級", status: "檔案未繳交" }
    // 可以在這裡添加更多學生
];

const Individual = () => {
    const [selectedStudent, setSelectedStudent] = useState(students[0]);
    const [grade, setGrade] = useState<number | null>(null);
    const [comment, setComment] = useState<string>("");

    const handleSelectStudent = (student: typeof students[0]) => {
        setSelectedStudent(student);
        setGrade(null);
        setComment("");
    };

    const handleSaveGrade = () => {
        console.log("儲存評分：", selectedStudent.fullName, grade, comment);
    };

    const handleNextStudent = () => {
        const currentIndex = students.findIndex(s => s.name === selectedStudent.name);
        const nextIndex = (currentIndex + 1) % students.length;
        handleSelectStudent(students[nextIndex]);
    };

    return (
        <div className="individual-page">
            <div className="student-list">
                {students.map(student => (
                    <div
                        key={student.id}
                        className="student-item"
                        onClick={() => handleSelectStudent(student)}
                    >
                        {student.name}
                    </div>
                ))}
            </div>
            <div className="student-info">
                <p>姓名：{selectedStudent.fullName}</p>
                <p>學號：{selectedStudent.id}</p>
                <p>科系：{selectedStudent.department}</p>
                <p>狀態：{selectedStudent.status}</p>
                <div className="other-actions">
                    <select className="other-actions-dropdown">
                        <option value="">其他動作</option>
                    </select>
                </div>
            </div>
            <div className="grade-input">
                <h3>成績</h3>
                <input
                    type="number"
                    value={grade !== null ? grade : ""}
                    onChange={(e) => setGrade(parseFloat(e.target.value))}
                />
                <div className="comment">
                    <h3>評語</h3>
                    <textarea
                        value={comment}
                        onChange={(e) => setComment(e.target.value)}
                    />
                    <div className="buttons">
                        <button onClick={handleSaveGrade}>儲存評分</button>
                        <button onClick={handleNextStudent}>下一個</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default function SubGradePage(): React.ReactElement {
    const { courseID, assignmentId } = useParams<{ courseID: string, assignmentId: string }>();
    const [activePage, setActivePage] = useState<'overview' | 'individual'>('overview');

    return (
        <div className="subcoursepage">
            <h2>課程名稱 - 第一週課程討論</h2>
            <div className="button-group">
    <div className={`button-container ${activePage === 'overview' ? 'active' : ''}`}
        onClick={() => setActivePage('overview')} >
        <div className={`circle-button ${activePage === 'overview' ? 'active' : ''}`}></div>
        <span>評分總覽</span>
    </div>
    <div className={`button-container ${activePage === 'individual' ? 'active' : ''}`}
        onClick={() => setActivePage('individual')}>
        <div className={`circle-button ${activePage === 'individual' ? 'active' : ''}`}></div>
        <span>個別評分</span>
    </div>
            </div>
            <div className="content">
                {activePage === 'overview' ? <Overview /> : <Individual />}
            </div>
        </div>
    );
}
