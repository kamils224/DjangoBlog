<template>
    <div class="container">
        <div v-for="articles in chunkedArticles" v-bind:key="articles.id" class="row justify-content-between">
            <div v-for="article in articles" v-bind:key="article.id" class="col-lg-4 mb-3">
                <div class="article" style="background: white">
                    <div class="row justify-content-center">
                        <h2>{{article.article_heading}}</h2>
                    </div>
                    <div class="row justify-content-center">
                        <img v-bind:src=article.image width="250" height="180" class="img-responsive"/>
                    </div>
                    <div class="row justify-content-center m-3">
                        <span v-for="i in 5" v-bind:key="i" >
                            <span v-if="article.stars >= i-0.25" class="fa fa-star fa-2x star-checked" ></span>
                            <span v-else class="fa fa-star fa-2x" ></span>
                        </span>
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
            ...mapGetters(["chunkedArticles"]),
            countStars(article,starIndex){
                return this.article.stars >= starIndex;

            }
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