import { createApp } from 'vue';
import App from './App.vue';
import './style.css';
import Dialog from 'vue3-dialog';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import router from './router';

// Importer des fichiers Bootstrap
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap-icons/font/bootstrap-icons.css';
import 'bootstrap/dist/js/bootstrap';

const app = createApp(App);
app.use(BootstrapVue);
app.use(IconsPlugin);
app.use(Dialog);
app.use(router);
app.mount('#app');
