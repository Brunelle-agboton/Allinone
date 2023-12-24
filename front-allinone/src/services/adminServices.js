import axios from 'axios';
import {AuthService} from './AuthService';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});
axios.defaults.withCredentials = true;


const token = AuthService.getToken();
//axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

/* Client*/
export const getListClient = () => {
  return apiUrl.get('/admin/clients', {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};
export const addClient = (data) => {
  return apiUrl.post('/admin/client', data, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
}
/* Projet*/

;export const addProject = (data) => {
  return apiUrl.post('/admin/project', data, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

export const getListProject = () => {
  return apiUrl.get('/admin/projects', {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};
export const getProject = (id) => {
  return apiUrl.get(`/admin/project/${id}`, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

export const editProject = (id, data) => {
  return apiUrl.put(`/admin/editp/${id}`, data, {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Authorization': `Bearer ${token}`,
    },
  });
};

export const delProject = (id) => {
  return apiUrl.delete(`/admin/delp/${id}`);
};

/************************************************* Team **************************************************/
export const getTeams = () => {
  return apiUrl.get('/admin/teams', {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

export const addTeam = (data) => {
  return apiUrl.post('/admin/team', data, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
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
      'Authorization': `Bearer ${token}`,
    },
  });
};
export const delTeam = (id) => {
  return apiUrl.delete(`/admin/delt/${id}`);
};

export const getMember = (id) => {
  return apiUrl.get(`/team/member/${id}`, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
}

export const getMembers = () => {
  return apiUrl.get(`/admin/members `, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

export const delMemberOfTeam = (idt,idm) => {
  return apiUrl.delete(`/admin/team/${idt}/del/${idm}`, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
};

export const getProjectsTeam = (id) =>{
  return apiUrl.get(`/team/project/${id}`, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

export const addTask = (id,data) => {
  return apiUrl.post(`/project/${id}/tasks`, data, {
    headers: {
      'Authorization': 'Bearer '+ token
    }
  });
};

apiUrl
