import Vue from "vue";
import VueRouter from "vue-router";
import ArticleDisplay from "../components/ArticleDisplay";
import ArticleList from "../components/ArticleList";
import Login from "../components/Login"
import Logout from "../components/Logout";
Vue.use(VueRouter);
export default new VueRouter({
    mode: "history",
    routes: [{
            name: "home",
            path: "/",
            component: ArticleList,
            alias: "/home"
        },
        {
            name: "display",
            path: "/:op(display)/:id(\\d+)",
            component: ArticleDisplay
        },
        {
            name: "login",
            path: "/login",
            component: Login
        },
        {
            name: "logout",
            path: "/logout",
            component: Logout
        },

        {
            path: "*",
            redirect: "/"
        }
    ]
})