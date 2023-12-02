<template>
    <div>
        <NavBar />
        <HomePage />
        <!--<main class="col-lg-12 ms-sm-auto px-md-4" >
      <router-view />
    </main>-->
    </div>
</template>

<script>
import HomePage from '../_Arche/HomePage.vue'
import NavBar from '../_Arche/NavBar.vue'

export default {
name: 'LayoutAdmin',
components: {
  HomePage,
  NavBar
}

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="../../style.css"> </style>
