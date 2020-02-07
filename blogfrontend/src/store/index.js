import Vue from 'vue'
import Vuex from 'vuex'
import Axios from "axios";
import AuthModule from "./auth"
import chunk from "chunk";

Vue.use(Vuex);
Vue.config.productionTip = false;

const baseUrl = 'http://127.0.0.1:8000';
const articlesUrl = `${baseUrl}/api/articles?search=`;
const categoriesUrl = `${baseUrl}/api/categories`;

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {auth: AuthModule},
    state: {
        articles: [],
        categories: [],
        nextPage: null,
        previousPage: null,
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
        saveCategory(currentState, category) {
            let index = currentState.categories.findIndex(c => c.id === category.id);
            if (index === -1) {
                currentState.categories.push(category);
            } else {
                Vue.set(currentState.categories, index, category);
            }
        },
        savePages(currentState, pageUrls) {
            if (pageUrls.next != null) {
                this.state.nextPage = pageUrls.next;
            }
            if (pageUrls.previous != null) {
                this.state.previousPage = pageUrls.previous;
            }
        },
        clearArticles(currentState) {
            if (currentState.articles.length > 0) {
                currentState.articles = [];
            }
        },
        selectArticle(currentState, article) {
            console.log(article);
            this.selectArticle = article;
        },
        searchValue(value) {
            this.state.search = value;
        }
    },
    actions: {
        async getArticlesAction(context, search='') {

            console.log(articlesUrl+search);
            let data = (await Axios.get(articlesUrl+search)).data;
            if (data.results !== undefined) {
                context.commit("clearArticles");
                data.results.forEach(a => context.commit("saveArticle", a));
                context.commit("savePages", {previous: data.previous, next: data.next});
            }
        },
        async getSpecificArticleAction(context, id) {
            console.log('data ' + id);
            let data = (await Axios.get(articlesUrl + '/' + id)).data;
            context.commit('selectArticle', data);
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
        }
    }
})
