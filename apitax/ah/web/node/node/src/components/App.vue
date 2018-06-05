
<!-- src/components/App.vue -->

<template>
	<div>
		
			<!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="#page-top">Apitax</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
		      <li class="nav-item active">
		        <router-link class="nav-link" to="/home">Home</router-link>
		      </li>
		      <li class="nav-item">
		        <router-link class="nav-link" to="/login" v-if="!authenticated">Login</router-link>
		      </li>
		      <li class="nav-item">
		        <router-link class="nav-link" to="/dashboard" v-if="authenticated">Dashboard</router-link>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" v-if="authenticated" @click="logout()">Logout</a>
		      </li>
          </ul>
        </div>
      </div>
    </nav>
		
		
		<!---<nav class="navbar navbar-expand-lg navbar-light bg-light">
		  <a class="navbar-brand" href="#">Navbar</a>
		  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
		    <span class="navbar-toggler-icon"></span>
		  </button>
		  <div class="collapse navbar-collapse" id="navbarNav">
		    <ul class="navbar-nav">
		      <li class="nav-item active">
		        <router-link class="nav-link" to="/home">Home</router-link>
		      </li>
		      <li class="nav-item">
		        <router-link class="nav-link" to="/login" v-if="!authenticated">Login</router-link>
		      </li>
		      <li class="nav-item">
		        <router-link class="nav-link" to="/dashboard" v-if="authenticated">Dashboard</router-link>
		      </li>
		      <li class="nav-item">
		        <a class="nav-link" v-if="authenticated" @click="logout()">Logout</a>
		      </li>
		    </ul>
		  </div>
		</nav>-->


	<section id="viewsection" class="bg-light" style="padding-top:15px;padding-bottom:15px">
    <div class="container">
    	<div class="row">
          <div class="col-lg-8 mx-auto">
	  <router-view></router-view>
    </div>
  </div>
    </div>
    </section>



        <section id="services" style="padding-top:15px;padding-bottom:15px">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <h2>Services</h2>
            <div class="row">
            	<div class="col">
            	
            	<div class="card mx-auto" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Commandtax</h5>
    <h6 class="card-subtitle mb-2 text-muted">API Usage and Data Gathering/Manipulating</h6>
    <p class="card-text">Execute one line commands on an API in order to return some data or preform some action. Major components of RESTful API's are currently supported.</p>
    <router-link class="card-link" to="/commandtax">Commandtax</router-link>
    <!---<a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>-->
  </div>
</div>
            	
            	</div>
            	<div class="col">
            	
            	<div class="card mx-auto" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Scriptax</h5>
    <h6 class="card-subtitle mb-2 text-muted">Automation, Control Flow, and Scoping </h6>
    <p class="card-text">Automate your commandtax by adding in control flow, variables, scopes, and more!.</p>
    <router-link class="card-link" to="/scriptax">Scriptax</router-link>
    <!---<a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>-->
  </div>
</div>
            	
            	</div>
            	
            	</div>
            	<br>
            	<div class="row">
            	
            	<div class="col">
            	
            	<div class="card mx-auto" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Accounts</h5>
    <h6 class="card-subtitle mb-2 text-muted">Switch Accounts</h6>
    <p class="card-text">Switch your authentication credentials to preform an action as another user. This is useful for debugging and testing purposes.</p>
    <router-link class="card-link" to="/accounts">Accounts</router-link>
    <!---<a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>-->
  </div>
</div>
            	
            	</div>
            	
            	<div class="col">
            	
            	<div class="card mx-auto" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">History and Logs</h5>
    <h6 class="card-subtitle mb-2 text-muted">View logs and see commandtax/scriptax history</h6>
    <p class="card-text">View the logs and the history of commandtax/scriptax which has been executed.</p>
    <router-link class="card-link" to="/history">History and Logs</router-link>
    <!---<a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>-->
  </div>
</div>
            	
            	</div>
            	
            	
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="system_status" class="bg-light" style="padding-top:15px;padding-bottom:15px">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <h2>System Status</h2>
            
              <div v-if="system_status" class="row">
              	<div class="col">
              	  <p class="lead">Loaded Driver: 
              		<strong>{{system_status.driver}}</strong>
              		</p>
              	</div>
              	<div class="col">
              	  <p class="lead">Debug: 
              		<span v-if="system_status.debug" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
									</p>
              		<p class="lead">Sensitive: 
              		<span v-if="system_status.sensitive" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              	</div>
              	<div class="col">
              		<p class="lead">Logging: 
              		<span v-if="system_status.logging" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              		<p class="lead">Log Filepath: 
              		<strong>{{system_status['log-file']}}</strong>
              		</p>
              		<p class="lead">Colorize CLI: 
              		<span v-if="system_status.logColorize" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              	</div>
              	
              </div>
            
          </div>
        </div>
      </div>
    </section>


	</div>
</template>

<script>
  import Api from '../api/api'
  import axios from 'axios';
  var api = new Api();
  export default {
    data: function () {
    //var api = new Api();
        return {
        		errors: [],
        		system_status: {},
        		driver: "ApitaxTests",
        		debug: true,
        		sensitive: false,
        		logging: true,
        		logFilepath: "some/file/path/log.txt",
        		logColorize: true,
            authenticated: Api.authenticated
            
        }
    },
    
    methods: {
      logout() {
        api.logout()
      }
    },
      created() {
    axios.get(`/apitax/system/status`)
    .then(response => {
      // JSON responses are automatically parsed.
      this.system_status = response.data;
    })
    .catch(e => {
      this.errors.push(e);
    })}
  }
</script>