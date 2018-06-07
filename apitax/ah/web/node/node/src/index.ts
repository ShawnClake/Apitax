import Vue from "vue";

import VueRouter from 'vue-router'

import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import App from "./components/App.vue";
import Home from "./components/Home.vue";
import Commandtax from "./components/Commandtax.vue";
import Scriptax from "./components/Scriptax.vue";

import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.min.css';
Vue.use(BootstrapVue);

import fontawesome from '@fortawesome/fontawesome'
import solid from '@fortawesome/fontawesome-free-solid'
import regular from '@fortawesome/fontawesome-free-regular'
import brands from '@fortawesome/fontawesome-free-brands'

fontawesome.library.add(solid)
fontawesome.library.add(regular)
fontawesome.library.add(brands)


import TreeView from "vue-json-tree-view"
Vue.use(TreeView)
import '../src/css/vue-json-tree-view.css'

import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import 'codemirror/addon/display/autorefresh.js'
Vue.use(VueCodemirror, { 
  options: { theme: 'Paraiso-Light', autoRefresh: true},
} )

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
    {path:'/scriptax', component: Scriptax},
  ],
});

const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app');

