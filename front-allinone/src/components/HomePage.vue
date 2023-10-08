<template>
  <div>
    <NavBar />
    <div class="container-fluid">
      <div class="row">
        <div class="sidebar col-md-3 col-lg-2 p-0">
          <div class="offcanvas-md offcanvas-end " tabindex="-1" id="sidebarMenu" aria-labelledby="sidebarMenuLabel">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" data-bs-target="#sidebarMenu" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto">
              <ul class="nav flex-column">
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="/dash">
                    Tableau de bord
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/projects">
                    Project
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/cl">
                    Clients
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/teams">
                    Equipe
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/company">
                    Entreprise
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/meet">
                    Reunions
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link d-flex align-items-center gap-2" href="/stats">
                    Statistiques
                  </a>
                </li>
              </ul>
              
            </div>
          
          </div>
          <div class="dropdown bottom-div">
          <hr>
            <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle mr-5" data-bs-toggle="dropdown" aria-expanded="false">
            <p class="rounded-circle me-2"><i class="bi bi-person"></i></p>
            <strong class="h6">Pseudo</strong>
            
            </a>
            <ul class="dropdown-menu text-small shadow">
              <li><a class="dropdown-item" href="#"><i class="bi bi-chat-left-dots"></i>   Custums instructions</a></li>
              <li><a class="dropdown-item" href="#"><i class="bi bi-gear"></i>   Setting</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#"><i class="bi bi-box-arrow-right"></i>   Sign out</a></li>
            </ul>
            </div>
        </div>
        <div class="col-md-9 col-lg-12 content">
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './_Arche/NavBar'
// import Swiper from 'swiper'; // Importez Swiper
// import 'swiper/package.json'; // Importez les styles CSS de Swiper

export default {
  name: 'HomePage',
  components: {
    NavBar,
  },
  
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bi {
  display: inline-block;
  width: 1rem;
  height: 1rem;
}
p{
  margin-right: 61px;
}

/*
 * Sidebar
 */

@media (min-width: 768px) {
  .sidebar .offcanvas-lg {
    position: -webkit-sticky;
    position: sticky;
    top: 48px;
  }
  
}

.sidebar {
  position: fixed; /* Définir la position absolue */
  height: 94vh;
  flex: 0 0 auto;
  background-color: #77933C
}

.sidebar .nav-link {
  font-size: .875rem;
  font-weight: 500;
  color: #fff;

}

.sidebar .nav-link.active {
  color: #002060;
  background: #9A7029;
}
.sidebar .nav-link:focus {
  color: #002060;
  background: #9A7029;
}

.sidebar-heading {
  font-size: .75rem;
}
.dropdown.bottom-div {
  position: absolute; 
  bottom: 0; /* La div sera placée en bas de la sidebar */
  width: 100%;
  color: #fff; /* Couleur du texte de la div */
  padding: 10px; 
  align-items:display;
}
.row{
  background-color: #EAE1D2;
}
.content {
  overflow-y: auto; /* Ajoutez ceci pour activer le défilement vertical lorsque le contenu dépasse la hauteur */
  max-height: calc(100vh - 48px); /* Réglez la hauteur maximale pour que le contenu reste dans la fenêtre visible */
}
</style>
