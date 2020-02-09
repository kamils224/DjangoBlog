<template>
    <div class="article-content mt-3">
        <div class="row m-5">
            <div class="col-lg-8">
                <h2 class="category">{{categoryName}}</h2>
                <h2 class="author">Author: {{author}}</h2>
                <h2>{{article.article_heading}}</h2>
                <span v-for="i in 5" v-bind:key="i">
                    <span v-if="article.stars >= i-0.25" class="fa fa-star fa-2x star-checked"></span>
                    <span v-else class="fa fa-star fa-2x"></span>
                </span>
            </div>
            <div class="col-lg-4">
                <img v-bind:src=article.image width="300" height="200"/>
            </div>
        </div>
        <div class="row m-5 justify-content-center">
            <h2>Description</h2>
        </div>
        <div class="row m-5 justify-content-center">
            {{article.article_body}}
        </div>
        <div class="row m-5 justify-content-center">
            <div v-for="img in images" v-bind:key="img.id" class="col-lg">
                <img v-bind:src=img.image width="300" height="200"/>
            </div>
        </div>
    </div>
</template>

<script>
    const baseUrl = 'http://127.0.0.1:8000';
    const articleUrl = `${baseUrl}/api/articles/`;
    const imagesUrl = `${baseUrl}/api/articleImages?article_id=`;
    const ownerUrl = `${baseUrl}/api/users/`;

    import Axios from 'axios'

    export default {
        name: "ArticleDisplay",
        data: function () {
            return {
                article: {},
                author: {},
                images: [],
            }
        },
        computed: {
            categoryName() {
                let result = this.$store.state.categories.find(i => i.id === this.article.category);
                if (result) {
                    return result.category_name;
                } else {
                    return '';
                }
            },
        },
        methods: {
            async getArticle() {
                this.article = (await Axios.get(articleUrl + this.$route.params.id)).data;
                this.author = (await Axios.get(ownerUrl + this.article.owner)).data.username;
            },
            async getArticleImages() {
                let images = (await Axios.get(imagesUrl + this.$route.params.id)).data.results;
                images.forEach(i => this.images.push(i));
            },
        },
        created() {
            this.getArticle();
            this.getArticleImages();
        },
    }
</script>

<style scoped>
    .article-content {
        background: white;
        border: orange solid 5px;
    }

</style>