<template>
    <div class="container-fluid" id="app">
        <div class="text-center">
            <img src="@/assets/CB_logo.png" />
        </div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-3">
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                 <ul class="navbar-nav mr-auto">
                     <li class="nav-item active">
                         <router-link to="/home" class="nav-link nav-text">
                            Main Page <span class="sr-only">(current)</span>
                         </router-link>
                     </li>
                     <li class="nav-item">
                         <router-link to="/" class="nav-link nav-text">
                            Categories
                         </router-link>
                     </li>
                     <li v-if="!loggedIn" class="nav-item">
                         <router-link to="/" class="nav-link nav-text">
                            Register
                         </router-link>
                     </li>
                     <li v-if="!loggedIn" class="nav-item">
                         <router-link to="/login" class="nav-link nav-text">
                            Login
                         </router-link>
                     </li>
                     <li v-else class="nav-item">
                         <router-link to="/logout" class="nav-link nav-text">
                            Logout
                         </router-link>
                     </li>

                 </ul>
                <form class="form-inline my-2 my-lg-0">
                  <input class="form-control mr-sm-2" type="search" placeholder="Type food name..." aria-label="Search">
                  <button class="btn btn-outline-default my-2 my-sm-0" type="submit">Search</button>
                </form>
              </div>
            </nav>
        <router-view/>
    </div>
</template>

<script>

export default {
  name: 'app',
  components: {

  },
  created() {
  this.$store.dispatch("getArticlesAction");
  },
  computed: {
    loggedIn(){
      return this.$store.getters.loggedIn;
    }
    },
    actions:{
     logout(){
       this.$store
     }
    },
}
</script>

<style>
  @import './assets/navbar_style.css';

  #app{
    background: wheat;
    min-height: 100vh;
  }
  .star-checked {
  color: orange;
  }
</style>