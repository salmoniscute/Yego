import {
    createContext
} from "react"

interface Function {
    getText: (id: string) => string,
    setLoading: (show: boolean) => void,
};

const functionContext = createContext<Function>({
    getText: (id: string) => id,
    setLoading: (show: boolean) => {},
});
export default functionContext;
