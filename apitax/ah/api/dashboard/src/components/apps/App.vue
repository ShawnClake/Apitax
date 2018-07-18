<!-- src/components/App.vue -->

<template>
    <div>

        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
            <div class="container-fluid">
                <router-link class="navbar-brand js-scroll-trigger" to="/home">Apitax</router-link>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                        aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active">
                            <router-link class="nav-link" to="/home">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" @click="gotoLogin()" v-if="!auth">Login</a>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/dashboard" v-if="auth">Dashboard</router-link>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" v-if="auth" @click="logout()">Logout</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


        <header class="bg-primary text-white">
            <div class="container-fluid">
                <br><br><br>
                <h1 class="text-center">Apitax</h1>
                <p class="lead text-center">Combining the power of Scriptax and Commandtax into one neat little
                    package</p>
            </div>
        </header>
        
        <div v-if="auth">

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
		                                        <h6 class="card-subtitle mb-2 text-muted">API Usage and Data
		                                            Gathering/Manipulating</h6>
		                                        <p class="card-text">Execute one line commands on an API in order to return some
		                                            data or preform some action. Major components of RESTful API's are currently
		                                            supported.</p>
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
		                                        <h6 class="card-subtitle mb-2 text-muted">Automation, Control Flow, and
		                                            Scoping </h6>
		                                        <p class="card-text">Automate your commandtax by adding in control flow,
		                                            variables, scopes, and more!.</p>
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
		                                        <p class="card-text">Switch your authentication credentials to preform an action
		                                            as another user. This is useful for debugging and testing purposes.</p>
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
		                                        <h6 class="card-subtitle mb-2 text-muted">View logs and see commandtax/scriptax
		                                            history</h6>
		                                        <p class="card-text">View the logs and the history of commandtax/scriptax which
		                                            has been executed.</p>
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
		                            <div v-if="driver_status" class="col">
		                                <p class="lead">Loaded Driver:
		                                    <strong>{{driver_status.name}}</strong>
		                                </p>
		                                <p v-if="driver_status" class="lead">Authenticated:
		                                    <span v-if="driver_status.authenticated" style="color:green;">True</span>
		                                    <span v-else style="color:red;">False</span>
		                                </p>
		                                <p v-if="driver_status" class="lead">Tokenable:
		                                    <span v-if="driver_status['auth-tokens']" style="color:green;">True</span>
		                                    <span v-else style="color:red;">False</span>
		                                </p>
		                            </div>
		                        </div>
		
		                    </div>
		                </div>
		            </div>
		        </section>

				</div>
				<div v-else>
					<section>
						<p>You need to be logged in to access these pages.</p>
					</section>
				</div>

        <!-- Footer -->
        <footer class="py-5 bg-dark">
            <div class="container-fluid">
                <p class="m-0 text-center text-white"><a href="https://github.com/ShawnClake/Apitax">Apitax </a>2018</p>
            </div>
        </footer>


    </div>
</template>

<script>
    import axios from 'axios';
		import * as apitax from 'apitax'
		
    export default {
        data: function () {
            return {
            		auth: false,
                errors: [],
                system_status: false,
                driver_status: false,

            }
        },

        methods: {
            logout() {
                apitax.logout('/apitax/2/login');
            },
            gotoLogin() {
            	window.location.href = '/apitax/2/login';
            },
        },
        created() {
        		apitax.isAuthenticated(this, function(context, response) {
							context.auth = response;
						});
        
	          /*let config = {
					    headers: {
					      'Authorization': 'Bearer ' + localStorage.getItem('refresh_token')
					    }
					  }
        
						axios.post(`/apitax/2/token/refresh`, {}, config)
								.then(response => {
										console.log(response);
                    console.log(response.data);
                    
                })
                .catch(e => {
                    this.errors.push(e);
                })*/


				    /*if (!this.auth && this.route.path !== '/user/login') {
				      store.dispatch('router/ROUTE_CHANGED', {path: '/user/login'})
				    }*/
					  
        
            /*axios.get(`/apitax/2/system/status`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.system_status = response.data.body;
                })
                .catch(e => {
                    this.errors.push(e);
                })

            axios.get(`/apitax/2/system/driver/defaultbase/status`)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.driver_status = response.data.body;
                    console.log(response)
                })
                .catch(e => {
                    this.errors.push(e);
                })*/
        }
    }
</script>