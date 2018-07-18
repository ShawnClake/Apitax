import Vue from "vue";

// Setting Vue Configuration Options
Vue.config.devtools = true;
//Vue.config.debug = true;

// Component Imports
import LandingApp from "../components/apps/LandingApp.vue";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";

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

// Custom CSS
import '../../src/css/main.css'

// Vue Confirmation
import VuejsDialog from "vuejs-dialog"
Vue.use(VuejsDialog)

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
        useScript(state, payload) {
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
export var router = new VueRouter({
    routes: [
        {path: '*', redirect: '/home'},
        {path: '/home', component: Home},
        {path: '/login', component: Login},
    ],
});

// Vuex Router Sync - Provides a route module in the store
import {sync} from 'vuex-router-sync'

const unsync = sync(store, router)

// Creating the Application
const app = new Vue({
    router,
    store,
    render: h => h(LandingApp)
}).$mount('#app');

