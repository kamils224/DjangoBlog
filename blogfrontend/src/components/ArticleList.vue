<template>
    <div>
        <div v-for="articles in chunkedArticles" v-bind:key="articles.id" class="row justify-content-center  mt-2">
            <div v-for="article in articles" v-bind:key="article.id" class="col-xl-4 mt-1 mb-1">
                <div class="article">
                    <router-link class="article-link" v-bind:to="{name: 'display',
                                        params: { op: 'display', id: article.id}}">
                        <div class="article-block">
                            <div class="row justify-content-center">
                                <h2 class="category">{{categoryName(article.category)}}</h2>
                            </div>
                            <div class="row justify-content-center">
                                <h2>{{article.article_heading}}</h2>
                            </div>
                            <div class="row justify-content-center">
                                <img v-bind:src=article.image class="img-responsive article-image"/>
                            </div>
                            <div class="row justify-content-center">
                                <h2 class="category m-2">Difficulty: </h2>
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
        <div class="row justify-content-center">
            <a-pagination @change="onPageChange" v-model="current" :pageSize="pageLimit" :total="totalArticles"/>
        </div>
    </div>

</template>

<script>

    import {
        mapGetters,
        mapActions,
    } from "vuex"


    export default {
        data: function () {
            return {
                current: 1,
            }
        },
        computed: {
            ...mapGetters(["chunkedArticles"]),
            ...mapGetters(["pageLimit"]),
            ...mapGetters(["categories"]),
            totalArticles() {
                return this.$store.state.totalArticles;
            },
            searchQuery() {
                return this.$store.state.searchQuery;
            },
        },
        methods: {
            ...mapActions({
                getArticles: "getArticlesAction",
            }),
            onPageChange(current) {

                let search = this.searchQuery;
                this.getArticles({search, page: current});
            },
            categoryName(id){
                return this.categories.find(i=>i.id === id).category_name;
            }
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
        width: auto;
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