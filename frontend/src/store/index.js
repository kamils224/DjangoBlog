import Vue from 'vue'
import Vuex from 'vuex'
import Axios from "axios";
import AuthModule from "./auth"
import chunk from "chunk";

Vue.use(Vuex);
Vue.config.productionTip = false;

const baseUrl = 'http://127.0.0.1:8000';
const articlesUrl = `${baseUrl}/api/articles`;
const categoriesUrl = `${baseUrl}/api/categories`;

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {auth: AuthModule},
    state: {
        articles: [],
        categories: [],
        pageLimit: 6,
        totalArticles: 0,
        searchQuery: ''
    },
    mutations: {
        saveArticle(currentState, article) {
            let index = currentState.articles.findIndex(a => a.id === article.id);
            if (index === -1) {
                currentState.articles.push(article);
            } else {
                Vue.set(currentState.articles, index, article);
            }
        },
        sortArticles(currentState) {
            currentState.articles.sort((a, b) => {
                if (a.stars > b.stars) return -1;
                if (a.stars < b.stars) return 1;
                else return 0;
            });
        },
        saveCategory(currentState, category) {
            let index = currentState.categories.findIndex(c => c.id === category.id);
            if (index === -1) {
                currentState.categories.push(category);
            } else {
                Vue.set(currentState.categories, index, category);
            }
        },
        clearArticles(currentState) {
            if (currentState.articles.length > 0) {
                currentState.articles = [];
            }
        },
        selectArticle(currentState, article) {
            this.selectArticle = article;
        },
        setTotalArticles(currentState, totalArticles) {
            currentState.totalArticles = totalArticles;
        },
        getCategoryName(currentState, id) {
            return currentState.categories.find(i => i.id === id);
        },
        setSearchQuery(currentState, value){
            currentState.searchQuery=value;
        }
    },
    actions: {
        async getArticlesAction(context, query = {search: '', page: 1}) {

            if (!Number.isInteger(query.page)) {
                return;
            }

            let nextPage = parseInt(query.page) - 1;
            let limit = parseInt(this.state.pageLimit);
            let offset = nextPage * limit;
            let queryString = `?limit=${this.state.pageLimit}&offset=${offset}&search=${query.search}`;
            let data = (await Axios.get(articlesUrl + queryString)).data;
            if (data.results !== undefined) {
                context.commit("clearArticles");
                data.results.forEach(a => context.commit("saveArticle", a));
                context.commit('sortArticles');
                context.commit("setTotalArticles", data.count)

            }
        },
        async getCategoriesAction(context) {
            let data = (await Axios.get(categoriesUrl)).data;
            data.results.forEach(c => context.commit("saveCategory", c));
        },
        async saveArticlesAction(context, article) {
            let index = context.state.articles.findIndex(a => a.id === article.id);
            if (index) {
                await Axios.post(articlesUrl, article);
            } else {
                await Axios.put(articlesUrl, article);
            }
            context.commit("saveArticle", article);
        },

    },
    getters: {
        chunkedArticles: state => {
            return chunk(state.articles, 3);
        },
        categories: state => {
            return state.categories;
        },
        nextPage: state => {
            return state.nextPage;
        },
        previousPage: state => {
            return state.previousPage;
        },
        pageLimit: state => {
            return state.pageLimit;
        },
        searchQuery: state => {
            return state.searchQuery;
        },
    }
})
