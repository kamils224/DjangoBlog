<template>
    <div class="container">
        <div class="text-center">
            <img src="@/assets/CB_logo.png" />
        </div>
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-3">
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                 <ul class="navbar-nav mr-auto">
                     <li class="nav-item active">
                        <a class="nav-link nav-text" href="#">Main Page <span class="sr-only">(current)</span></a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link nav-text" href="#">Categories</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link nav-text" href="#">Login</a>
                     </li>
                     <li class="nav-item">
                         <a class="nav-link nav-text" href="#">Register</a>
                     </li>
                 </ul>
                <form class="form-inline my-2 my-lg-0">
                  <input class="form-control mr-sm-2" type="search" placeholder="Type food name..." aria-label="Search">
                  <button class="btn btn-outline-default my-2 my-sm-0" type="submit">Search</button>
                </form>
              </div>
            </nav>
            <article-list/>
    </div>
</template>

<script>
    import ArticleList from "./ArticleList";
    export default {
        name: "Blog",
        components: {ArticleList}
    }
</script>

<style scoped>

</style>
