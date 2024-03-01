import { ReactElement } from "react";
import { Routes } from "react-router-dom";

import NavigateBar from "./components/NavigateBar";
import Footer from "./components/Footer";

export default function App(): ReactElement {
    return (
        <div id="app">
            <NavigateBar />
            <Routes>

            </Routes>
            <Footer />
        </div>
    );
}
