<template>
  <div id="app">
    <blog/>
    <router-view/>
  </div>
</template>

<script>
import Blog from "./components/Blog";

export default {
  name: 'app',
  components: {
    Blog,
  },
  created() {
  this.$store.dispatch("getArticlesAction");
  }
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

