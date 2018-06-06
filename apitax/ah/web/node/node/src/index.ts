import Vue from "vue";

import VueRouter from 'vue-router'

import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import App from "./components/App.vue";
import Home from "./components/Home.vue";
import Commandtax from "./components/Commandtax.vue";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.config.devtools = true;
//Vue.config.debug = true;

Vue.use(VueRouter);
export var router:any = new VueRouter({
  routes: [
    {path:'*', redirect: '/home'},
    {path:'/home', component: Home},
    {path:'/login', component: Login},
    {path:'/dashboard', component: Dashboard},
    {path:'/commandtax', component: Commandtax},
  ],
});

const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
