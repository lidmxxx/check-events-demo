import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import "./assets/css/global.css"
import axios from 'axios'
import router from './router/index.js'

Vue.config.productionTip = false
Vue.use(ElementUI);

axios.defaults.baseURL = 'http://127.0.0.1:1234/'
Vue.prototype.$http = axios

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');

