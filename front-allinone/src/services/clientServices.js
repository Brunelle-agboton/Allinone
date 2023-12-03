import axios from 'axios';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});
/* Client*/

export const getAllUsers = () => {
    return new Promise((resolve, reject) => {
        apiUrl.get('/users')
        .then(response => resolve(response))
        .catch(error => reject(error));
        }); 
        };
        

apiUrl
