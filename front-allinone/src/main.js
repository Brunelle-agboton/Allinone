import { createApp } from 'vue';
import App from './App.vue';
import './style.css';
import Dialog from 'vue3-dialog';
import 'vue3-dialog/';
import router from './router';
import store from './store/store';
import { AuthService } from './services/AuthService';



// Importer des fichiers Bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

import 'bootstrap-icons/font/bootstrap-icons.css'

  const app = createApp(App);

  const tokenData = AuthService.decodeToken();
if (tokenData) {
  store.commit('setAdminLoggedIn', true);
  store.commit('setUser', tokenData.payload); // Mettez à jour les informations de l'utilisateur dans le magasin
}

  app.use(Dialog);
  app.use(router);
  app.use(store);
  app.mount('#app');