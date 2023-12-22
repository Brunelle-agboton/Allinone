<template>
  <div>
    <div class="admin-page" :class="{ 'blurred': !isAdminLoggedIn }">
      <NavBar />
      <SidebarPage />
    </div>
    <!-- Afficher ConnexionPage avec un fond transparent -->
    <div class="connexion-overlay" v-if="!isAdminLoggedIn">
      <ConnexionPage />
    </div>
    
    <!--<main class="col-lg-12 ms-sm-auto px-md-4" >
        <router-view />
      </main>-->
  </div>
</template>

<script>
import SidebarPage from '../equipe/SidebarPage.vue'
import NavBar from '../_Arche/NavBar.vue'

export default {
  name: 'LayoutEquipe',
  components: {
    SidebarPage,
    NavBar
  },
computed: {
    isAdminLoggedIn() {
      return this.$store.state.auth.isAdminLoggedIn;
    },
},
}
</script>
<style src="../../style.css"> </style>
