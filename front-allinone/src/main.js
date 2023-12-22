import { createApp } from 'vue';
import App from './App.vue';
import './style.css';
import Dialog from 'vue3-dialog';
import 'vue3-dialog/';
import router from './router';
import store from './store/store';

// Importer des fichiers Bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
import 'bootstrap-icons/font/bootstrap-icons.css'

  const app = createApp(App);

  app.use(Dialog);
  app.use(router);
  app.use(store);
    // Charger le token depuis le localStorage après une actualisation
const storedToken = localStorage.getItem('access_token');
if (storedToken) {
  store.commit('setToken', storedToken );
  store.commit('setAdminLoggedIn', true);
}

  app.mount('#app');