import axios from 'axios';

const apiService = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});

export const getSomeData = () => {
  return apiService.get('/endpoint');
};

export const postData = (data) => {
  return apiService.post('/endpoint', data);
};
