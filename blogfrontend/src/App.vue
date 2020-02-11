<template>
    <div class="container-fluid" id="app">
        <div class="text-center">
            <img class="img-fluid" src="@/assets/CB_logo.png"/>
        </div>
        <nav class="justify-content-center navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="text-center">
                <ul class="navbar-nav ">
                    <li class="nav-item">
                        <a @click="mainPage()" href="#" class="nav-link nav-text" >
                            Main Page <span class="sr-only">(current)</span>
                        </a>
                    </li>
                    <li>
                        <div class=" form-inline mt-2">
                            <input v-model="currentSearch" class="form-control ml-2" style="max-width: 200px"
                                   type="search" placeholder="Search" aria-label="Search">
                            <button @click="searchArticles()" class="btn btn-outline-success ml-2 mr-2">
                                Search
                            </button>
                        </div>
                    </li>
                    <li v-if="!loggedIn" class="nav-item">
                        <router-link to="/register" class="nav-link nav-text">
                            Register
                        </router-link>
                    </li>
                    <li v-if="!loggedIn" class="nav-item">
                        <router-link to="/login" class="nav-link nav-text">
                            Login
                        </router-link>
                    </li>
                    <li v-else class="nav-item navbar-left">
                        <router-link to="/logout" class="nav-link nav-text">
                            Logout
                        </router-link>
                    </li>

                    <li v-if="loggedIn" class="nav-item navbar-right">
                        <a href="http://localhost:8000/admin/" target="_blank" class="nav-link nav-text">Admin site</a>
                    </li>
                </ul>
            </div>
        </nav>
        <router-view/>

    </div>
</template>

<script>
    import {
        mapGetters,
    } from "vuex"

    export default {
        name: 'app',
        components: {},
        data: function () {
            return {
                currentSearch: '',
                searchMode: false
            }
        },
        created() {
            this.$store.dispatch("getCategoriesAction");
            this.$store.dispatch("getArticlesAction");

        },
        computed: {
            loggedIn() {
                return this.$store.getters.loggedIn;
            },
            ...mapGetters(["categories"]),
        },
        methods: {
            searchArticles() {
                let query = this.currentSearch;
                this.$store.commit('setSearchQuery', query);
                this.$store.dispatch('getArticlesAction', {search: query, page: 1});
                this.$router.push('/home');
            },
            mainPage() {
                let query = '';
                this.$store.commit('setSearchQuery', query);
                this.$store.dispatch('getArticlesAction', {search: query, page: 1});
                this.$router.push('/home').catch(()=>{});
            }
        },
    }
</script>

<style>
    @import './assets/navbar_style.css';
    @import './assets/style.css';

    #app {
        background: wheat;
        min-height: 100vh;
    }

    .star-checked {
        color: orange;
    }

    .router-link-exact-active {
        color: white !important;
    }

</style>