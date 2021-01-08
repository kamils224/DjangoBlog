<template>
    <div class="article-content mt-3">
        <div class="row m-5">
            <div class="col-lg-4">
                <h2 class="category">{{categoryName}}</h2>
                <h2 class="author">Author: {{author.username}}</h2>
                <h2>{{article.article_heading}}</h2>
                <span v-for="i in 5" v-bind:key="i">
                    <span v-if="countStars(i)" class="fa fa-star fa-2x star-checked"></span>
                    <span v-else class="fa fa-star fa-2x"></span>
                </span>
                <hr>
            </div>
            <div class="col-lg-4">
                <template v-if="loggedIn">
                    <h2 class="author"> Your rate: </h2>
                    <template>
                        <a-rate @change="onStarsChanged" v-model="currentRate"/>
                    </template>
                    <h2 v-if="currentRate >-1" class="category">{{currentRate}}/5</h2>
                    <h2 v-else class="category">No rating</h2>
                </template>

            </div>
            <div class="col-lg-4">
                <img class="img-fluid" v-bind:src=article.image height="200"/>
            </div>
        </div>
        <div class="row m-5 justify-content-center">
            <h2>Description</h2>
        </div>
        <div v-html="article.article_body" class="row m-5 justify-content-center">
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
    import {mapGetters} from "vuex";
    import Axios from 'axios'

    const baseUrl = 'http://127.0.0.1:8000';
    const articleUrl = `${baseUrl}/api/articles/`;
    const ratingUrl = `${baseUrl}/api/rating`;
    const ratingSendUrl = `${baseUrl}/api/rating`;
    const imagesUrl = `${baseUrl}/api/articleImages?article_id=`;
    const ownerUrl = `${baseUrl}/api/users/`;

    export default {
        name: "ArticleDisplay",
        data: function () {
            return {
                article: {},
                author: {},
                images: [],
                rating: {},
                currentRate: -1,
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

            ...mapGetters(["loggedIn"]),
            ...mapGetters(["getToken"]),
        },
        methods: {

            async getArticleDetails() {
                this.article = (await Axios.get(articleUrl + this.$route.params.id)).data;
                this.author = (await Axios.get(ownerUrl + this.article.owner)).data;

                let token = this.getToken;
                let rating = ((await Axios.get(ratingUrl + `?owner=${this.author.id}&article_id=${this.article.id}`, token))
                    .data);

                if (rating.count !== 0) {
                    this.rating = rating.results[0];
                    this.currentRate = this.rating.rate;
                } else {
                    this.currentRate = -1;
                }
            },
            async getArticleImages() {
                let images = (await Axios.get(imagesUrl + this.$route.params.id)).data.results;
                images.forEach(i => this.images.push(i));
            },
            async sendRating(value) {

                let token = this.getToken;
                let ratingRequest = {
                    rate: value,
                    article_id: this.$route.params.id,
                };

                if (this.isEmpty(this.rating)) {
                    console.log('POST');
                    this.rating = await Axios.post(ratingSendUrl, ratingRequest, token);
                } else {
                    console.log('PUT');
                    await Axios.put(ratingSendUrl + `/${this.rating.id}`, ratingRequest, token);
                }
            },
            getImgUrl(i) {
                return this.images[i].image;
            },
            countStars(rate) {
                return this.article.stars >= rate - 0.25
            },
            onStarsChanged(value) {
                this.currentRate = value;
                this.sendRating(value);
            },
            isEmpty(obj) {
                return Object.entries(obj).length === 0;
            }
        },
        created() {
            this.getArticleDetails();
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