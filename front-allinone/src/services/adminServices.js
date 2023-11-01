import axios from 'axios';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});
/* Client*/
export const getListClient = () => {
  return apiUrl.get('/admin/clients');
};

export const getListProject = () => {
  return apiUrl.get('/admin/projects');
};

export const addClient = (data) => {
  return apiUrl.post('/admin/client', data);
}
/* Projet*/

;export const addProject = (data) => {
  return apiUrl.post('/admin/project', data);
};

export const getProject = (id) => {
  return apiUrl.get(`/admin/project/${id}`);
};

export const editProject = (id, data) => {
  return apiUrl.put(`/admin/editp/${id}`, data, {
    headers: {
      'Content-Type': 'application/json', // Spécifiez le type de contenu
    },
  });
};

/* Team*/
export const getTeams = () => {
  return apiUrl.get('/admin/teams');
};

apiUrl
