import axios from "axios";

export const toLogin = (params) => {
    return axios.post('api-auth/token/', params)
}

export const getUserInfo = () => {
    return axios.get('api/v1/users')
}

export const getUserBookcase = () => {
    return axios.get('api/v1/bookcase')
}
