import {
    createContext
} from "react"

interface Function {
    getText: (id: string) => string
};

const functionContext = createContext<Function>({
    getText: (id: string) => id,
});
export default functionContext;
