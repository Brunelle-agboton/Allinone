import {authenticate, AuthService} from '../services/AuthService';

export default {
    state: {
      isAdminLoggedIn: false,
      user: {
        id: 0,
        username: '',
        role: '',
      },
      token: null,
    },
    getters : {
      currentUser: (state) => state.user,
      isAuthenticated: (state) => state.isAdminLoggedIn,
      currentToken: (state) => state.token,
    },
    mutations: {
      setToken(state, token) {
        state.token = token;
      },
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
   clearAuthState(state) {
      state.token = null;
      state.isAdminLoggedIn = false;
      state.user = {
        id: 0,
        username: '',
        role: '',
      };
    },
  },
  actions: {
    async login({commit}, user){
      try{
        const response = await authenticate(user);
        await AuthService.saveToken(response.data.access_token);

        const cuser = AuthService.decodeToken();

        await commit('setUser', cuser.payload.sub);
        console.log("set ik");
        await commit('setAdminLoggedIn', true);
        } catch(err) {
          console.log("Error in Login Action", err);
          throw new Error(`Authentication failed! ${err}`);
          }
          }, 

    logout({ commit }) {
      // Effacer toutes les informations d'authentification
      commit('clearAuthState');
      // Vous pouvez également ajouter des étapes supplémentaires, telles que la déconnexion côté serveur
    },
    },
  }
