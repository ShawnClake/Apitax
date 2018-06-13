import Vue from "vue";

// Setting Vue Configuration Options
Vue.config.devtools = true;
//Vue.config.debug = true;

// Component Imports
import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import App from "./components/App.vue";
import Home from "./components/Home.vue";
import Commandtax from "./components/Commandtax.vue";
import Scriptax from "./components/Scriptax.vue";
import ScriptaxEdit from "./components/ScriptaxEdit.vue";

// Bootstrap
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.min.css';
Vue.use(BootstrapVue);

// Font Awesome
import fontawesome from '@fortawesome/fontawesome'
import solid from '@fortawesome/fontawesome-free-solid'
import regular from '@fortawesome/fontawesome-free-regular'
import brands from '@fortawesome/fontawesome-free-brands'
fontawesome.library.add(solid)
fontawesome.library.add(regular)
fontawesome.library.add(brands)

// Vue Confirmation
import VuejsDialog from "vuejs-dialog"
Vue.use(VuejsDialog)

// JSON Tree View
import TreeView from "vue-json-tree-view"
Vue.use(TreeView)
import '../src/css/vue-json-tree-view.css'

// Code Mirror
import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'
import 'codemirror/addon/display/autorefresh.js'
Vue.use(VueCodemirror, { 
  options: { theme: 'Paraiso-Light', autoRefresh: true},
} )

// Persist Vuex Store
import createPersistedState from 'vuex-persistedstate'

// Vuex Store
import Vuex from 'vuex'
Vue.use(Vuex)
const store = new Vuex.Store({
  state: {
    scriptax: {
    		script: ""
    },
  },
  mutations: {
    useScript (state, payload) {
      state.scriptax.script = payload.script;
    }
  },
  plugins: [
  		createPersistedState(),
  ],
})

// Vue Router
import VueRouter from 'vue-router'
Vue.use(VueRouter);
export var router:any = new VueRouter({
  routes: [
    {path:'*', redirect: '/home'},
    {path:'/home', component: Home},
    {path:'/login', component: Login},
    {path:'/dashboard', component: Dashboard},
    {path:'/commandtax', component: Commandtax},
    {path:'/scriptax', component: Scriptax},
    {path:'/scriptax/edit', component: ScriptaxEdit},
  ],
});

// Vuex Router Sync - Provides a route module in the store
import { sync } from 'vuex-router-sync'
const unsync = sync(store, router)

// Creating the Application
const app = new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');

