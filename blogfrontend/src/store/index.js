import Vue from 'vue'
import Vuex from 'vuex'
import Axios from "axios";
import AuthModule from "./auth"
import chunk from "chunk";

Vue.use(Vuex);
Vue.config.productionTip = false;

const baseUrl ='http://127.0.0.1:8000';
const articlesUrl = `${baseUrl}/api/articles`;

export default new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    modules: {auth: AuthModule},
    state: {
        articles: [],
    },
    mutations:{
        saveArticle(currentState, article){
            let index = currentState.articles.findIndex(a=>a.id === article.id);
            if(index === -1){
                currentState.articles.push(article);
            }else{
                Vue.set(currentState.articles, index, article);
            }
        },
    },
    actions:{
        async getArticlesAction(context){
            let data = (await Axios.get(articlesUrl)).data;
            data.results.forEach(a=>context.commit("saveArticle",a));
        },
        async printArticlesAction(context){
            let result = await Axios.get(articlesUrl).data;
            context.commit("print", result);

        },
        async saveArticlesAction(context, article){
            let index = context.state.articles.findIndex(a=> a.id === article.id);
            if(index){
                await Axios.post(articlesUrl, article);
            }else{
                await Axios.put(articlesUrl, article);
            }
            context.commit("saveArticle", article);
        },
    },
    getters:{
        chunkedArticles: state => {return chunk(state.articles,3);},
    }
})
