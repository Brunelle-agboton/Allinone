import axios from 'axios';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});
/* Client*/
export const getListClient = () => {
  return apiUrl.get('/admin/clients');
};

export const getListProject = () => {
  return apiUrl.get('/admin/projects', {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
    },
  });
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
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
    },
  });
};

export const delProject = (id) => {
  return apiUrl.delete(`/admin/delp/${id}`);
};

/* Team*/
export const getTeams = () => {
  return apiUrl.get('/admin/teams');
};

export const addTeam = (data) => {
  return apiUrl.post('/admin/team', data);
};

export const getTeam = (id) => {
  return apiUrl.get(`/admin/team/${id}`);
};
export const editTeam = (id, data) => {
  return apiUrl.put(`/admin/editeq/${id}`, data, {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
    },
  });
};
export const delTeam = (id) => {
  return apiUrl.delete(`/admin/delt/${id}`);
};
apiUrl
