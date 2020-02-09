import Vue from "vue";
import VueRouter from "vue-router";
import ArticleDisplay from "../components/ArticleDisplay";
import ArticleList from "../components/ArticleList";
import Login from "../components/Login"
import Logout from "../components/Logout";
import Register from "../components/Register";
import store from '../store';
Vue.use(VueRouter);

 const router = new VueRouter({
    mode: "history",
    routes: [{
            name: "home",
            path: "/:page(\\d?)",
            component: ArticleList,
            alias: "/home/:page(\\d?)"
        },
        {
            name: "search",
            path: "/search/:id",
            component: ArticleList,
        },
        {
            name: "display",
            path: "/:op(display)/:id(\\d+)",
            component: ArticleDisplay
        },
        {
            name: "login",
            path: "/login",
            component: Login,
            meta:{
                requiresVisitor: true,
            }
        },
        {
            name: "logout",
            path: "/logout",
            component: Logout
        },
        {
            name: "register",
            path: "/register",
            component: Register,
            meta:{
                requiresVisitor: true,
            }
        },
        {
            path: "*",
            redirect: "/"
        }
    ],
});

 router.beforeEach((to, from, next)=>{
    if(to.matched.some(record => record.meta.requiresAuth)){
        if(!store.getters.loggedIn){
            next({
                path: 'login',
                query: {redirect: to.fullPath}
            })
        }else{
            next()
        }
    }
    if(to.matched.some(record => record.meta.requiresVisitor)){

        if(store.getters.loggedIn){
            next({
                path: 'home',
                query: {redirect: to.fullPath}
            })
        }else{
            next()
        }
    }else{
        next();
     }
});


 export default router