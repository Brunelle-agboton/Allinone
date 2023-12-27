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
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'ConnexionPage',
  data() {
    return {
      username: '',
      password: '',
      tokenData: '',
    };
  },
  computed: {
    ...mapGetters(['currentToken'], ['currentUser']), 
  },
  methods: {
    ...mapActions(['login']),

    async handleSubmit(event) {
      event.preventDefault();
      const userData = {
        username: this.username,
        password: this.password,
      };
      try {
        await this.login(userData);
        if (this.currentToken !== ''){
            if (this.$store.state.auth.user.role == 'admin') {
              this.$router.push('/admin/dash');
              console.log(`Redirection de l'utilisateur après ${this.$store.state.auth.user.username} une connexion réussie.`);
            }
            else {
              this.$router.push('/team');
            }
                   
          } else {
            throw new Error('Invalid credentials');
            }        
      }
      catch (error) {
        alert(error.message);
        }
    },
    mounted() {
    console.log(this.currentUser);
  },
} ,
}
</script>

<style src="../../style.css"> </style>