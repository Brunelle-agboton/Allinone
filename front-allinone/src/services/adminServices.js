import axios from 'axios';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});

export const getListClient = () => {
  return apiUrl.get('/admin/clients');
};

export const getListProject = () => {
  return apiUrl.get('/admin/projects');
};

export const addClient = (data) => {
  return apiUrl.post('/admin/client', data);
}

;export const addProject = (data) => {
  return apiUrl.post('/admin/project', data);
};
apiUrl
