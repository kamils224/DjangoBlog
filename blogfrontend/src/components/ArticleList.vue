<template>
    <div class="container">
        <div v-for="articles in chunkedArticles" v-bind:key="articles.id" class="row justify-content-between">
            <div v-for="article in articles" v-bind:key="article.id" class="col-lg-4">
                <div class="article" style="background: white">
                    <div class="row justify-content-center">
                        <h2>{{article.article_heading}}</h2>
                        <img v-bind:src=article.image width="250" height="180" class="img-responsive"/>
                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<script>

    import{
        mapActions,
        mapGetters,
    } from "vuex"
    export default {
        computed: {
            ...mapGetters(["chunkedArticles"])
        },
        methods: {
            ...mapActions({
                getArticles: "getArticlesAction",
            })
        },
    }
</script>

<style scoped>

    .article{
        width: auto;
        border: orange solid 5px;
    }

    .article-image{
        min-width: 200px;
        min-height: 200px;
    }

</style>