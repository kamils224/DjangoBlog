<template>
    <div class="article-content">
        <div class="row m-5">
            <div class="col-lg-8">
                <h2>{{article.article_heading}}</h2>
                <span v-for="i in 5" v-bind:key="i" >
                    <span v-if="article.stars >= i-0.25" class="fa fa-star fa-2x star-checked" ></span>
                    <span v-else class="fa fa-star fa-2x" ></span>
                </span>
            </div>
            <div class="col-lg-4">
                <img width="300" height="200"  v-bind:src=article.image />
            </div>


        </div>
            <div class="row m-5 justify-content-lg-start">
                            <h2>Description</h2>
                {{article.article_body}}
            </div>
    </div>
</template>

<script>
    let unwatcher;
    export default {
        name: "ArticleDisplay",
        data: function() {
        return {
            article: {}
        }
    },
        methods:{
        selectArticle(route) {
                let articleId = route.params.id;
                let selectedArticle = this.$store.state.articles.find(a => a.id === articleId);
                this.article = {};
                Object.assign(this.article, selectedArticle);
            }
        },
        created() {
            unwatcher = this.$store.watch(state => state.articles,
                () => this.selectArticle(this.$route));
            this.selectArticle(this.$route);
        },
        beforeDestroy() {
            unwatcher();
        },
    }
</script>

<style scoped>
    .article-content{
        background: white;
        border: orange solid 5px;
    }
</style>