import { createApp } from 'vue';
import App from './App.vue';

import Dialog from 'vue3-dialog';
import 'vue3-dialog/';
import router from './router';

// Importer des fichiers Bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-icons/font/bootstrap-icons.css'
// Importer le module JavaScript Bootstrap 
import 'bootstrap/dist/js/bootstrap.js';

  const app = createApp(App);
  app.use(Dialog);
  app.use(router);
  app.mount('#app');