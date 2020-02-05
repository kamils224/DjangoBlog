import Vue from 'vue'
import App from './App.vue'
import blog from './store/index'
import router from './router'
import Vuelidate from "vuelidate";
import "bootstrap/dist/css/bootstrap.min.css";
import "font-awesome/css/font-awesome.min.css";

Vue.config.productionTip = false;
Vue.use(Vuelidate);
new Vue({
  store: blog,
  router,
  components:{App},
  render: h => h(App)
}).$mount('#app');
