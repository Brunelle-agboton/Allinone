<template>
    <div>
      <div class="admin-page" :class="{ 'blurred': !isAdminLoggedIn }">
      <!-- Contenu de la page Admin -->
      <NavBar />
      <HomePage />
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
import HomePage from '../_Arche/HomePage.vue'
import NavBar from '../_Arche/NavBar.vue'
import ConnexionPage from '../_Arche/ConnexionPage.vue';

export default {
name: 'LayoutAdmin',
data() {
  return {
    //isAdminLoggedIn: false,
  };
},
components: {
  HomePage,
  NavBar,
  ConnexionPage
},
computed: {
    isAdminLoggedIn() {
      return this.$store.state.auth.isAdminLoggedIn;
    },
},
methods: {
  handleSubmit() {
    // Logique de connexion, puis mettez à jour l'état d'authentification
    //this.$store.commit('setAdminLoggedIn', true);
  },
},

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../style.css"> </style>
