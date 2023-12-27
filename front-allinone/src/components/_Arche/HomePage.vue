<template>
  <div class="container-fluid">
    <div class="row">
      <div class="sidebarMenu col-md-3 col-lg-2 p-0">
        <div class="offcanvas-md offcanvas-end " tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu"
              aria-label="Close"></button>
          </div>
          <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
            <ul class="nav flex-column">
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'dashboard' }"
                  @click.prevent="setActiveLink('dashboard')" :aria-current="activeLink === 'dashboard' ? 'page' : null"
                  href="/admin/dash">
                  Tableau de bord
                </a>
              </li>
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'projects' }"
                  @click.prevent="setActiveLink('projects')" :aria-current="activeLink === 'projects' ? 'page' : null"
                  href="projects">
                  Projets
                </a>
              </li>
              <li class="nav-item">
                <a :class="{
                  'nav-link': true, 'd-flex': true,
                  'align-items-center': true,
                  'gap-2': true, 'active': activeLink === 'clients'
                }"
                  @click.prevent="setActiveLink('clients')" :aria-current="activeLink === 'clients' ? 'page' : null"
                  href="/admin/cl">
                  Clients
                </a>
              </li>
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'teams' }"
                  @click.prevent="setActiveLink('teams')" :aria-current="activeLink === 'teams' ? 'page' : null"
                  href="/admin/teams">
                  Equipe
                </a>
              </li>
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'company' }"
                  @click.prevent="setActiveLink('company')" :aria-current="activeLink === 'company' ? 'page' : null"
                  href="/admin/company">
                  Entreprise
                </a>
              </li>
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'meet' }"
                  @click.prevent="setActiveLink('meet')" :aria-current="activeLink === 'meet' ? 'page' : null"
                  href="/admin/meet">
                  Réunions
                </a>
              </li>
              <li class="nav-item">
                <a :class="{ 'nav-link': true, 'd-flex': true, 'align-items-center': true, 'gap-2': true, 'active': activeLink === 'stats' }"
                  @click.prevent="setActiveLink('stats')" :aria-current="activeLink === 'stats' ? 'page' : null"
                  href="/admin/stats">
                  Statistiques
                </a>
              </li>
            </ul>

          </div>

        </div>
        <div class="dropdown bottom-div">
          <hr>
          <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle "
            data-bs-toggle="dropdown" aria-expanded="false">
            <div class="rounded-circle me-4 ppp"><i class="bi bi-person pppp"></i>
              <strong class="h6 profile">{{ username }}</strong>
            </div>
          </a>
          <ul class="dropdown-menu text-small shadow">
            <li><a class="dropdown-item" href="#"><i class="bi bi-chat-left-dots"></i> Custums instructions</a></li>
            <li><a class="dropdown-item" href="#"><i class="bi bi-gear"></i> Setting</a></li>
            <li>
              <hr class="dropdown-divider">
            </li>
            <li><a class="dropdown-item" @click="logOut" href="/auth"><i class="bi bi-box-arrow-right"></i> Sign out</a>
            </li>
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
export default {
  name: 'HomePage',
  data() {
    return {
      username: '',
      activeLink: '',
    };
  },
  components: {
  },
  computed: {
    ...mapGetters(['currentUser']),

  },
  methods: {
    ...mapActions(['logout']),
    logOut() {
      logout().then(() => {
        this.$router.push('/auth');
      });
    },
    setActiveLink(link) {
      this.activeLink = link;
      
      if (link === 'dashboard') {
        this.$router.push('/admin/dash');
      } else if (link === 'projects') {
        this.$router.push('/admin/projects');
      }else if (link === 'clients') {
      this.$router.push('/admin/cl');
      }else if (link === 'teams') {
      this.$router.push('/admin/teams');
    }else if (link === 'company') {
      this.$router.push('/admin/company');
    }else if (link === 'meet') {
      this.$router.push('/admin/meet');
    }else if (link === 'stats') {
      this.$router.push('/admin/stats');
    }
    },
  },
  mounted() {
    if (this.currentToken !== '') {
      const cuser = AuthService.decodeToken();
      //console.log(cuser);
      this.$store.commit('setUser', cuser.payload.sub)
      this.username = this.currentUser.username;
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../style.css"></style>
