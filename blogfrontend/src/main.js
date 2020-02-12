import Vue from 'vue'
import App from './App.vue'
import blog from './store/index'
import router from './router'
import Vuelidate from "vuelidate";
import "bootstrap/dist/css/bootstrap.min.css";
import "font-awesome/css/font-awesome.min.css";

import {Pagination, Carousel, Rate} from "ant-design-vue";
import 'ant-design-vue/dist/antd.css';

Vue.config.productionTip = false;

Vue.use(Vuelidate);
Vue.use(Pagination);
Vue.use(Carousel);
Vue.use(Rate);

new Vue({
  store: blog,
  router,
  components:{App},
  render: h => h(App)
}).$mount('#app');
