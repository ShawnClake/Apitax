
<!-- src/components/App.vue -->

<template>
	<div>


    <!---<section id="about">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <h2>About this page</h2>
            <p class="lead">This is a great place to talk about your webpage. This template is purposefully unstyled so you can use it as a boilerplate or starting point for you own landing page designs! This template features:</p>
            <ul>
              <li>Clickable nav links that smooth scroll to page sections</li>
              <li>Responsive behavior when clicking nav links perfect for a one page website</li>
              <li>Bootstrap's scrollspy feature which highlights which section of the page you're on in the navbar</li>
              <li>Minimal custom CSS so you are free to explore your own unique design options</li>
            </ul>
          </div>
        </div>
      </div>
    </section>-->
		
		
		
			<!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <div class="container-fluid">
      <router-link class="navbar-brand js-scroll-trigger" to="/home">Apitax</router-link>
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
		
		
				
		
    <header class="bg-primary text-white">
      <div class="container-fluid">
      	<br><br><br>
      		<h1 class="text-center">Apitax</h1>
          <p class="lead text-center">Combining the power of Scriptax and Commandtax into one neat little package</p>
      </div>
    </header>
		
		
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
    <div class="container-fluid">
    	<div class="row">
          <div class="col-lg-8 mx-auto">
	  <router-view></router-view>
    </div>
  </div>
    </div>
    </section>



        <section id="services" style="padding-top:15px;padding-bottom:15px">
      <div class="container-fluid">
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
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <h2>System Status</h2>
            
              <div v-if="system_status" class="row">
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
              		<span v-if="system_status.log" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              		<p class="lead">Log Filepath: 
              		<strong>{{system_status['log-file']}}</strong>
              		</p>
              		<p class="lead">Colorize CLI: 
              		<span v-if="system_status['log-colorize']" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              	</div>
              	<div v-if="driver_status.driver" class="col">
              	  <p class="lead">Loaded Driver: 
              		<strong>{{system_status.driver}}</strong>
              		</p>
              		<p v-if="driver_status" class="lead">Authenticated: 
              		<span v-if="driver_status.driver.authenticated" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              		<p v-if="driver_status" class="lead">Tokenable: 
              		<span v-if="driver_status.driver['auth-tokens']" style="color:green;">True</span>
									<span v-else style="color:red;">False</span>
              		</p>
              	</div>
              </div>
            
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container-fluid">
        <p class="m-0 text-center text-white"><a href="https://github.com/ShawnClake/Apitax">Apitax </a>2018</p>
      </div>
      <!-- /.container -->
    </footer>


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
        		driver_status: {},
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
			    })
			    
			   axios.get(`/apitax/system/driver/status`)
			    .then(response => {
			      // JSON responses are automatically parsed.
			      this.driver_status = response.data;
			      console.log(response)
			    })
			    .catch(e => {
			      this.errors.push(e);
			    })
    }
  }
</script>