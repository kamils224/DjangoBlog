<template>
    <div>
        <div v-for="articles in chunkedArticles" v-bind:key="articles.id" class="row justify-content-between mt-2">
            <div v-for="article in articles" v-bind:key="article.id" class="col-xl-4 mt-2 mb-2">
                <div class="article">
                    <router-link class="article-link" v-bind:to="{name: 'display',
                                        params: { op: 'display', id: article.id}}">
                        <div class="article-block">
                            <div class="row justify-content-center">
                                <h2>{{article.article_heading}}</h2>
                            </div>

                            <div class="row justify-content-center">
                                <img v-bind:src=article.image class="img-responsive article-image"/>
                            </div>
                            <div class="row justify-content-center">
                                <span v-for="i in 5" v-bind:key="i">
                                    <span v-if="article.stars >= i-0.25" class="fa fa-star fa-2x star-checked"></span>
                                    <span v-else class="fa fa-star fa-2x"></span>
                                </span>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
        <div class="justify-content-center pagination">
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    <li v-on:click="getArticles('todo')" class="page-item"><a class="page-link" href="#">Previous
                        Page</a></li>
                    <li v-on:click="getArticles('todo')" class="page-item"><a class="page-link"
                                                                                href="#">Next Page</a>
                    </li>
                </ul>
            </nav>
        </div>
    </div>
</template>

<script>

    import {
        mapGetters,
        mapActions,
        mapState,
    } from "vuex"


    export default {
        computed: {
            ...mapGetters(["chunkedArticles"]),
            ...mapGetters(["nextPage"]),
            ...mapGetters(["previousPage"]),
            ...mapState(["categories"]),
        },
        methods: {
            ...mapActions({
                getArticles: "getArticlesAction",
            }),
        },
    }
</script>

<style scoped>

    .article {
        width: auto;
        border: orange solid 5px;
        background: white;
    }

    .article-image {
        width: 250px;
        height: 180px;
    }

    .article-block:hover {
        background-color: yellowgreen;
    }

    .article-link {
        text-decoration: none;
        color: black;

    }

</style>