import {
    createContext
} from "react";

import { User } from "../schemas/user";

const userDataContext = createContext<User | null>(null);
export default userDataContext;
