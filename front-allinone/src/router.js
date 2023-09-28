import { createRouter, createWebHistory } from 'vue-router';

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/home',
      name: 'HomePage',
      component: () => import('./components/HomePage.vue'),
    },
    {
      path: '/dash',
      name: 'DashboardPage',
      component: () => import('./components/DashboardPage.vue'),
    },
    {
      path: '/connexion',
      name: 'ConnexionPage',
      component: () => import('./components/Connexion.vue'),
    },
    {
      path: '/projects',
      name: 'ProjectPage',
      component: () => import('./components/ProjectPage.vue'),
    },
    {
      path: '/projectdetails',
      name: 'ProjectDetails',
      component: () => import('./components/ProjectDetails.vue'),
    },
    {
      path: '/cld',
      name: 'ClientsDetail',
      component: () => import('./components/ClientsDetail.vue'),
    },
    {
      path: '/teams',
      name: 'TeamPage',
      component: () => import('./components/TeamPage.vue'), 
    },
    {
      path: '/cl',
      name: 'ClientsPage',
      component: () => import('./components/ClientsPage.vue'), 
    },
    {
      path: '/company',
      name: 'CompanyPage',
      component: () => import('./components/CompanyPage.vue'), 
    }
    ,{
      path: '/meet',
      name: 'MeetingPage',
      component: () => import('./components/MeetingPage.vue'),
    },{
      path: '/stats',
      name: 'StatistiquesPage',
      component: () => import('./components/StatistiquesPage.vue'),
    },
    {
      path: '/listd',
      name: 'StatistiquesPage',
      component: () => import('./components/StatistiquesPage.vue'),
    }
  ],
});