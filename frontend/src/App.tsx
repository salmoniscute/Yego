import { ReactElement } from "react";
import { Routes } from "react-router-dom";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";
import CourseForum from "./components/CourseForum";

export default function App(): ReactElement {
    return (
        <div id="app">
            <NavigateBar />
            
            {/* for test  不需要的話可以助解掉*/}
            <CourseForum crouseID=""/> 
            
            <Routes>

            </Routes>
            <Footer />
        </div>
    );
}
