import { createRouter, createWebHistory } from 'vue-router';
import ProjectDetails from './components/admin/ProjectDetails.vue';
import ClientsDetail from './components/admin/ClientsDetail.vue';
import TeamDetail from './components/admin/TeamDetail.vue';
import LayoutEquipe from './components/equipe/LayoutEquipe.vue';
import TaskPage from './components/equipe/TaskPage.vue';
import ProjectTeamPage from './components/equipe/ProjectTeamPage.vue'
import store from './store/auth';


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'App',
      component: () => import('./App.vue'),
    },
    {
      path: '/home',
      name: 'HomePage',
      component: () => import('./components/_Arche/HomePage.vue'),
    },
    {
      path: '/auth',
      name: 'ConnexionPage',
      component: () => import('./components/_Arche/ConnexionPage.vue'),
    },
    {
      path: '/admin',
      component: () => import('./components/admin/LayoutAdmin.vue'),
      meta: { requiresAuth: true },
      children: [
        {
          path: 'dash',
          name: 'DashboardPage',
          component: () => import('./components/admin/DashboardPage.vue'),
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
      path: '/side',
      name: 'SidebarPage',
      component: () => import('./components/equipe/SidebarPage.vue'),
    },    
    {
      path: '/team/:id',
      name: 'LayoutEquipe',
      component: LayoutEquipe,
      meta: { requiresAuth: true },
      props: true,
      children:[
        { path: 'tasks/:id', name:'TaskPage', component: TaskPage,props: true,},
        { path: 'project/:id', name:'ProjectTeamPage', component: ProjectTeamPage,props: true,},

        ]
    }
  ],
  
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next('/auth'); // Rediriger vers la page de connexion si le jeton n'est pas présent
    } else {
      next();
    }
  } else {
    next(); // Continuer vers d'autres routes non protégées
  }
});

export default router;