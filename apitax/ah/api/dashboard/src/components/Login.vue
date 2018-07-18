<template>
    <div class="row">
        <div class="col">
        <div v-if="response" class="row">
        <div class="col">
        <b-alert variant="danger" show>{{response.message}}</b-alert>
        </div>
        </div>
        <div class="row">
        <div class="col">
            <h4>Apitax Login</h4>
            <div class="form-group">
                <label for="username">Username</label>
                <input v-model="credentials.username" type="text" class="form-control" id="username"
                       aria-describedby="usernameHelp" placeholder="Enter username">
                <small id="usernameHelp" class="form-text text-muted">Your OpenStack username.</small>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input v-model="credentials.password" type="password" class="form-control" id="password"
                       placeholder="Password">
            </div>
            <button @click="login()" class="btn btn-primary">Login</button>
        </div>
    </div>
    </div>
    </div>
</template>

<script>
    import * as apitax from 'apitax'
    export default {
        data: function () {
            return {
                credentials: {
                    username: '',
                    password: ''
                },
                response: null,
            }
        },

        methods: {
					login() {
						apitax.login(this.credentials.username, this.credentials.password, this, function(context, response) {
							context.response = response;
						}, '/apitax/2/dashboard');
						
					   /*axios.post(`/apitax/2/auth`, {
            			"username": this.credentials.username,
            			"password": this.credentials.password,
            		})
	              .then(response => {
	                  this.response = response.data;
	                  if(response.data.status == 201)
	                  {
	                  	localStorage.setItem('access_token', response.data.access_token);
	                  	localStorage.setItem('refresh_token', response.data.refresh_token);
	                  	localStorage.setItem('api_token', response.data.auth.api_token);
	                  	localStorage.setItem('username', response.data.auth.username);
	                  	window.location.href = '/apitax/2/dashboard';
	                  }
	              })
	              .catch(e => {
	                  this.response = e;
	          })*/
					},
        },
        created() {

        }
    }
</script>