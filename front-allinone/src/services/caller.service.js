import axios from "axios";
import {AuthService} from "../services/AuthService";

const Axios = axios.create({
    baseURL: 'http://localhost:5000'
  }
)

Axios.interceptors.response.use(response => {
  response.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept, Access-Control-Allow-Origin "
  response.headers["Access-Control-Allow-Origin"] = '*'
  response.headers["Content-Type"] = 'application/json'
  return response;
}, error => {
  console.log(error);
  if (!error.response) {
    this.$store.commit("SetDisplayNotif", {d: true, mes: error.message});
    return Promise.reject(error);
  }
  if (error.response.status === 401) {
    //AuthService.logout();
    this.$router.push('/');
  } else {
    this.$store.commit("SetDisplayNotif", {d: true, mes: error.response.data.message});
    return Promise.reject(error);
  }
});

Axios.interceptors.request.use(request => {
    request.headers["Access-Control-Allow-Headers"] = "Content-Type, Accept, Access-Control-Allow-Origin "
    request.headers["Content-Type"] = 'application/json'
    request.headers["Cross-Origin-Request"] = '*'
    request.headers.Accept = '*'
    request.headers["Access-Control-Allow-Origin"] = '*'
    const token = AuthService.getToken()
    if (token) {
      request.headers.Authorization = 'Bearer ' + token
    }
    return request
  }
)
export default Axios
