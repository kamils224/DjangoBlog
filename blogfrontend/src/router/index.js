import Vue from "vue";
import VueRouter from "vue-router";
import ArticleDisplay from "../components/ArticleDisplay";
import ArticleList from "../components/ArticleList";
Vue.use(VueRouter);
export default new VueRouter({
    mode: "history",
    routes: [{
            name: "list",
            path: "/",
            component: ArticleList,
            alias: "/list"
        },
        {
            name: "editor",
            path: "/:id(\\d+)?",
            component: ArticleDisplay
        },
        {
            path: "*",
            redirect: "/"
        }
    ]
})