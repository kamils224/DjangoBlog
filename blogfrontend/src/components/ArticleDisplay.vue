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
        <div class="">
            <a-carousel arrows dotsClass="slick-dots slick-thumb">
                <a slot="customPaging" slot-scope="props">
                    <img :src="getImgUrl(props.i)"/>
                </a>
                <div v-for="img in images" v-bind:key="img.id" alt="">
                    <img :src="img.image" height="500" width="auto"/>
                </div>
            </a-carousel>
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
            getImgUrl(i) {
                return this.images[i].image;
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
        padding-bottom: 5%;
    }

    /* For demo */
    .ant-carousel >>> .slick-dots {
        height: auto;
    }

    .ant-carousel >>> .slick-slide img {
        border: 5px solid #fff;
        display: block;
        margin: auto;
        max-width: 80%;
    }

    .ant-carousel >>> .slick-thumb {
        bottom: -45px;
    }

    .ant-carousel >>> .slick-thumb li {
        width: 60px;
        height: 45px;
    }

    .ant-carousel >>> .slick-thumb li img {
        width: 100%;
        height: 100%;
        filter: grayscale(100%);
    }

    .ant-carousel >>> .slick-thumb li.slick-active img {
        filter: grayscale(0%);
    }

</style>