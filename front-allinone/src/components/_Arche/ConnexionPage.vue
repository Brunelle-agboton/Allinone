<template>
  <div>
      <div class="form-signin connect">
        <form @submit="handleSubmit">
          <h1 class="h4 mb-3 fw-normal">Connexion</h1>
          <div class="form-group">
            <label for="username">Username</label>
            <input id="username" type="text" class="form-control" v-model="username" required >
            
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input id="password" type="password" class="form-control" placeholder="Password" v-model="password" required>
          </div>
      
          <div class="checkbox mb-3 ml-0">
            <label>
              <input type="checkbox" value="remember-me"> Remember me
            </label>
          </div>
          <button class="w-100 btn btn-primary" type="submit">Login</button>
        </form>
      </div>
  </div>
</template>

<script>
import {login, AuthService} from '@/services/AuthService';
//import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'ConnexionPage',
  data() {
    return {
      username: '',
      password: '',
      //tokenData: '',
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  methods: {
    handleSubmit(event) {
      event.preventDefault();
      const userData = {
        username: this.username,
        password: this.password,
      };
      console.log(userData);
      login(userData)
      .then((response) => {
        AuthService.saveToken(response.data.access_token);
        //console.log(response.data.access_token)
        this.$store.commit('setAdminLoggedIn', true);
        const tokenData = AuthService.decodeToken()
        
        console.log(tokenData);

        this.$router.push('/admin');
      })
      .catch((error) => {
          console.log(error);
        });      
    },
} ,
}
</script>

<style src="../../style.css"> </style>