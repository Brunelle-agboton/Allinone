import { createRouter, createWebHistory } from 'vue-router';
import ProjectDetails from './components/ProjectDetails.vue';
import ClientsDetail from './components/ClientsDetail.vue';
import TeamDetail from './components/TeamDetail.vue';


export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/h',
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
      path: '/projet/:id',
      name: 'projetDetails',
      component: ProjectDetails,
      props: true,
    },

    {
      path: '/cld/:id',
      name: 'ClientsDetail',
      component: ClientsDetail,
      props: true,

    },
    
    {
      path: '/teams',
      name: 'TeamPage',
      component: () => import('./components/TeamPage.vue'), 
    },
    {
      path: '/teamdetail/:id',
      name: 'TeamDetail',
      component: TeamDetail, 
      props: true,
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