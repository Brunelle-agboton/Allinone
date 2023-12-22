<template>
    <div class="container-fluid">
      <div class="row">
        <div class="sidebarMenu col-md-3 col-lg-2 p-0">
          <div class="offcanvas-md offcanvas-end " tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu"></button>
            </div>
            <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
              <ul class="nav flex-column">
                <li v-for="project in projects" :key="project.idproject" class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" :href="idmember +'/project/' + project.idproject">
                    {{ project.name }} 
                  </a>
                </li>
               
              </ul>
              
            </div>
          
          </div>
          <div class="dropdown bottom-div">
          <hr>
            <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle " data-bs-toggle="dropdown" aria-expanded="false">
            <div class="rounded-circle me-4 ppp"><i class="bi bi-person pppp"></i>
            <strong class="h6 profile">{{username }}</strong>
          </div>
            </a>
            <ul class="dropdown-menu text-small shadow">
              <li><a class="dropdown-item" href="#"><i class="bi bi-chat-left-dots"></i>   Custums instructions</a></li>
              <li><a class="dropdown-item" href="#"><i class="bi bi-gear"></i>   Setting</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" @click="logOut"><i class="bi bi-box-arrow-right"></i>   Sign out</a></li>
            </ul>
            </div>
          </div>
        <div class="col-md-9 ms-sm-auto col-lg-12 px-md-4" style="margin-top: 30px;">
          <router-view />
        </div>
      </div>
    </div>
</template>

<script>
import { logout, AuthService } from '@/services/AuthService';
import { mapActions, mapGetters } from 'vuex';
import {getListProject,getMember} from '@/services/adminServices';

export default {
  name: 'HomePage',
  data() {
    return {
      idmember: 0,
      projects: [], // Nouvelle propriété pour stocker la liste des projets
      adminProjects: [],
      username:'',
    };
  },
  components: {
  },
  computed: {
    ...mapGetters(['currentToken'], ['currentUser']), 
  },
  methods: {
    ...mapActions(['logout']),
    logOut() {
      logout().then(() => {
        this.$router.push('/auth');
        });
    },
  },
  mounted() {
    this.idmember = this.$route.params.id;
    if (this.currentToken !== ''){
      const cuser = AuthService.decodeToken();

      this.$store.commit('setUser', cuser.payload.sub)
      this.username = this.$store.state.auth.user.username;
    if (this.$store.state.auth.user.role == 'admin') {
      getListProject()
      .then((response) => {
          this.projects = response.data
        })
        .catch((error) => {
          console.error(error)
        });
    }else{
    getMember(this.idmember)
        .then(response => {
          this.projects = response.data.projects; 
        })
        .catch(error => {
          console.error('Erreur lors de la récupération des projets :', error);
        });
  }
}
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../style.css"> </style>
