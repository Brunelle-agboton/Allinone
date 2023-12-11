//import {AuthService} from '../service/AuthService';

export default {
    state: {
      isAdminLoggedIn: false,
      user: {
        id: 0,
        username: '',
        role: '',
      }
    },
    getters : {
      currentUser: (state) => {
        return state.user;
      },
      isAuthenticated: (state) => state.isAdminLoggedIn,
      
    },
    mutations: {
      setAdminLoggedIn(state, value) {
        state.isAdminLoggedIn = value;
      },
      setUser(state, user) {
        state.user = {
          id: user.id,
          username: user.username,
          role: user.role,
        };
      },
    }, 
    actions: {
      // Actions pour gérer la connexion, la déconnexion, etc.
    },
  }
