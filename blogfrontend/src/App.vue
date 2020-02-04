<template>
  <div id="app">
    <Blog/>
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
  #app{
    background: wheat;
    min-height: 100vh;
  }
</style>

