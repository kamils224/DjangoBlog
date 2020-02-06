<template>
    <div class="container-fluid" id="app">
        <div class="text-center">
            <img class="img-fluid" src="@/assets/CB_logo.png"/>
        </div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="text-center">
                <ul class="navbar-nav ">
                    <li class="nav-item">
                        <router-link to="/home" class="nav-link nav-text">
                            Main Page <span class="sr-only">(current)</span>
                        </router-link>
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
                    <li class="nav-item navbar-right">
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
        mapGetters,mapActions,
    } from "vuex"

    export default {
        name: 'app',
        components: {},

        created() {
            console.log(this.$route.query.search);
            this.$store.dispatch("getArticlesAction");
            this.$store.dispatch("getCategoriesAction");
        },
        computed: {
            loggedIn() {
                return this.$store.getters.loggedIn;
            },
            ...mapGetters(["categories"]),
        },
        methods: {
            ...mapActions({
                getArticles: "getArticlesAction",
            }),
        },
        mounted() {
        }
    }
</script>

<style>
    @import './assets/navbar_style.css';

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