<template>
  <div>
    <NavBar />
    <HomePage/>
  </div>
</template>

<script>
import HomePage from './components/_Arche/HomePage.vue'
import NavBar from './components/_Arche/NavBar.vue'

export default {
  name: 'App',
  components: {
    HomePage,
    NavBar
  }
}
</script>

<style src="./style.css">
</style>
