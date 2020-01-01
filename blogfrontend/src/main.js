import Vue from 'vue'
import App from './App.vue'

import blog from './blog'
import "bootstrap/dist/css/bootstrap.min.css";
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  blog
}).$mount('#app');
