<template>
  <div>
    <body class="text-center">
      <main class="form-signin">
        <form @submit="handleSubmit">
          <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
      
          <div class="form-floating">
            <label for="pseudo">Pseudo</label>
            <input id="pseudo" type="text" class="form-control" required >
            
          </div>
          <div class="form-floating">
            <label for="password">Password</label>
            <input id="password" type="password" class="form-control" placeholder="Password" required>
          </div>
      
          <div class="checkbox mb-3 ml-0">
            <label>
              <input type="checkbox" value="remember-me"> Remember me
            </label>
          </div>
          <button class="w-100 btn btn-lg" type="submit">Login</button>
        </form>
        
      </main>
    </body>

      <footer class="py-3 mb-0">
        <div class="container con-foot">
          <span class="text-muted">&copy; 2017–2021 Place sticky footer content here.</span>
        </div>
      </footer>
  </div>
</template>

<script>
export default {
  name: 'NuxtTutoriel',
  data() {
    return {
      pseudo: '',
      password: '',
    };
  },
  methods: {
    handleSubmit(event) {
      event.preventDefault();
      // Envoyez les données du formulaire à votre API pour l'inscription
      // const userData = {
        // pseudo: this.pseudo,
        // password: this.password,
      // };

      
    },
  },
};
</script>

<style src="../../style.css"> </style>