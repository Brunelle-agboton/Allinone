import { createRouter, createWebHistory } from 'vue-router';
import ProjectDetails from './components/admin/ProjectDetails.vue';
import ClientsDetail from './components/admin/ClientsDetail.vue';
import TeamDetail from './components/admin/TeamDetail.vue';
import LayoutEquipe from './components/equipe/LayoutEquipe.vue';
import TaskPage from './components/equipe/TaskPage.vue';
import BoardPage from './components/equipe/BoardPage.vue'

export default createRouter({
  history: createWebHistory(),
  routes: [
    /*{
      path: '/',
      name: 'App',
      component: () => import('./App.vue'),
    },*/
    {
      path: '/admin',
      component: () => import('./components/admin/LayoutAdmin.vue'),
      children: [
        {
          path: 'home',
          name: 'HomePage',
          component: () => import('./components/_Arche/HomePage.vue'),
        },
        {
          path: 'dash',
          name: 'DashboardPage',
          component: () => import('./components/admin/DashboardPage.vue'),
        },
        {
          path: 'connexion',
          name: 'ConnexionPage',
          component: () => import('./components/_Arche/Connexion.vue'),
        },
        {
          path: 'projects',
          name: 'ProjectPage',
          component: () => import('./components/admin/ProjectPage.vue'),
        },
        {
          path: 'projet/:id',
          name: 'projetDetails',
          component: ProjectDetails,
          props: true,
        },
        {
          path: 'cld/:id',
          name: 'ClientsDetail',
          component: ClientsDetail,
          props: true,
        },
        {
          path: 'teams',
          name: 'TeamPage',
          component: () => import('./components/admin/TeamPage.vue'),
        },
        {
          path: 'teamdetail/:id',
          name: 'TeamDetail',
          component: TeamDetail,
          props: true,
        },
        {
          path: 'cl',
          name: 'ClientsPage',
          component: () => import('./components/admin/ClientsPage.vue'),
        },
        {
          path: 'company',
          name: 'CompanyPage',
          component: () => import('./components/admin/CompanyPage.vue'),
        },
        {
          path: 'meet',
          name: 'MeetingPage',
          component: () => import('./components/admin/MeetingPage.vue'),
        },
        {
          path: 'stats',
          name: 'StatistiquesPage',
          component: () => import('./components/admin/StatistiquesPage.vue'),
        },
        {
          path: 'listd',
          name: 'StatistiquesPage',
          component: () => import('./components/admin/StatistiquesPage.vue'),
        },
      ],
    },    
    {
      path: '/team',
      name: 'LayoutEquipe',
      component: LayoutEquipe,
      children:[
        { path: 'tasks', name:'TaskPage', component: TaskPage},
        { path: 'board', name:'BoardPage', component: BoardPage},

        ]
    }
  ],
});