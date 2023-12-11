import { createStore } from 'vuex'; // Importez createStore de vuex
import auth from './auth';

// Créez le store Vuex
const store = createStore({
  modules: {
    auth,
  },
});

export default store;