// src/index.ts

import Vue from "vue";

import VueRouter from 'vue-router'

import axios, { AxiosResponse } from 'axios';

//import Hello from "./components/Hello.vue";
import Login from "./components/Login.vue";
import Dashboard from "./components/Dashboard.vue";
import App from "./components/App.vue";
import Home from "./components/Home.vue";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.use(VueRouter)
export var router:any = new VueRouter({
  routes: [
    {path:'*', redirect: '/home'},
    {path:'/home', component: Home},
    {path:'/login', component: Login},
    {path:'/dashboard', component: Dashboard},
  ],
});

const app = new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

// Set up routing and match routes to components
/*router.map({
  '/home': {
    
  },
  '/login': {
    component: Login
  },
  '/dashboard': {
    component: Dashboard
  },
})*/

// Redirect to the home route if any routes are unmatched
/*router.redirect({
  '*': '/home'
})*/

// Start the app on the #app div
//router.start(App, '#app')

/*let app = new Vue({
    el: "#app",
    template: `
    <div>
        <!---Name: <input v-model="name" type="text">-->
        <h1>Login Component</h1>
        <!---:username="username" :password="password"-->
        <login-component  />
        </div>
    `,
    data: { 
      name: "World",
      username: "",
      password: "" 
    },
    components: {
        HelloComponent,
        LoginComponent
    },
    methods: {
      login: function() {
    	  alert(app.username + " " + app.password);
      },
    }
});*/