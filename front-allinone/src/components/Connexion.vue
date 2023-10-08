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
        <div class="container">
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

<style>
html,
body {
  height: 100%;
}

body {
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: auto;
}

.form-signin .checkbox {
  font-weight: 400;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
button {
  background: #9A7029;
}
.container {
  width: auto;
  max-width: 680px;
  padding: 0 15px;
}

footer {
  background-color: #d9d9d9;
}
</style>