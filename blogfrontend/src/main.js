import Vue from 'vue'
import App from './App.vue'
import blog from './blog/index'
import "bootstrap/dist/css/bootstrap.min.css";
import "font-awesome/css/font-awesome.min.css";

Vue.config.productionTip = false;

new Vue({
  store: blog,
  render: h => h(App)
}).$mount('#app');
