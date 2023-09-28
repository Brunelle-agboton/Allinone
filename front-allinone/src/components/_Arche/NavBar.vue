<template>
    <div>
        <header class="navbar sticky-top  flex-md-nowrap p-0 shadow">
            <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-20 " href="/home">Allinone</a>
            <ul class="nav col-12 col-md-auto mb-2  mb-md-0">
                <li><a href="#" class="nav-link px-4 link-secondary">Home</a></li>
                <li><a href="#" class="nav-link px-4">About</a></li>
                <li><a href="#" class="nav-link px-4">Assitance</a></li>
            </ul>

      <!-- <div class="col-md-3 text-end">
        <button type="button" class="btn btn-outline-primary me-2">Login</button>
        <button type="button" class="btn btn-primary">Sign-up</button>
      </div>-->
  </header>
    </div>
</template>
<script>
export default {
  name: 'NavBar',
};
</script>

<style>
.navbar-search {
    display: block;
  }
/*
 * Navbar
 */

 .navbar {
    position: absolute;
  padding-top: .75rem;
  padding-bottom: .75rem;
  background-color: #77933C;
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, .25);
}

.navbar-brand {
  font-weight: 500;
  color: #002060;
}
.navbar .form-control {
  padding: .75rem 1rem;
}
.nav .li {
  padding-right: 15px;
}

</style>