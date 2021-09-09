import axios from "axios";

export const toLogin = (params) => {
    return axios.post('http://127.0.0.1:8000/api-auth/token/', params)
}

export const getUserInfo = () => {
    return axios.get('http://127.0.0.1:8000/api/v1/users')
}

export const getUserBookcase = () => {
    return axios.get('http://127.0.0.1:8000/api/v1/bookcase')
}

export const getUserProfile = (param) => {

}
