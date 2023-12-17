<template>
    <div class="container-fluid">
      <div class="row">
        <div class="sidebarMenu col-md-3 col-lg-2 p-0">
          <div class="offcanvas-md offcanvas-end " tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
              <ul class="nav flex-column">
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/dash">
                    Tableau de bord
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="/admin/projects">
                    Projets
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/cl">
                    Clients
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/teams">
                    Equipe
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/company">
                    Entreprise
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/meet">
                    Réunions
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/admin/stats">
                    Statistiques
                  </a>
                </li>
              </ul>
              
            </div>
          
          </div>
          <div class="dropdown bottom-div">
          <hr>
            <a href="#" class="d-flex align-items-center text-dark text-decoration-none dropdown-toggle " data-bs-toggle="dropdown" aria-expanded="false">
            <div class="rounded-circle me-4 ppp"><i class="bi bi-person pppp"></i>
            <strong class="h6 profile"> Jupiter {{ username }}</strong>
          </div>
            </a>
            <ul class="dropdown-menu text-small shadow">
              <li><a class="dropdown-item" href="#"><i class="bi bi-chat-left-dots"></i>   Custums instructions</a></li>
              <li><a class="dropdown-item" href="#"><i class="bi bi-gear"></i>   Setting</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="/auth"><i class="bi bi-box-arrow-right"></i>   Sign out</a></li>
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
export default {
  name: 'HomePage',
  components: {
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    username() {
      const username = this.currentUser.username;
      console.log('Username:', username); // Utilisez console.log pour afficher la valeur dans la console
      return username;
    },
  },
  
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../style.css"> </style>
