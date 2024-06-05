import axios from "axios";

// let dealError: (error: AxiosError) => any = (error) => {
//     throw error;
// };

// export function setDealError(func: (error: AxiosError) => any) {
//     dealError = func;
// }

export function setRequestConfig() {
    axios.interceptors.request.use(async (config) => {
        config.baseURL = process.env.REACT_APP_API_END_POINT ?? "";

        let token = localStorage.getItem("access_token");
        let tokenType = localStorage.getItem("token_type");
        // if JWT exist, put it into header
        if (token !== null && tokenType !== null) {
            config.headers.Authorization = `${tokenType} ${token}`;
        }
        return config;
    });
};

// export function setResponseConfig() {
//     axios.interceptors.response.use(
//         response => response,
//         (error) => {
//             dealError(error);
//         }
//     )
// };
