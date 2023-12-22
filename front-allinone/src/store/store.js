import { createStore } from 'vuex'; 
//import createPersistedState from "vuex-persistedstate";

import auth from './auth';

// Créez le store Vuex
const store = createStore({
  modules: {
    auth,
  },
  // plugins: [createPersistedState()],
});

export default store;