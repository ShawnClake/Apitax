<template>
<div class="row">
	<div class="col">
		<h4>API Login</h4>
		<div class="form-group">
  		<label for="username">Username</label>
  		<input v-model="credentials.username" type="text" class="form-control" id="username" aria-describedby="usernameHelp" placeholder="Enter username">
  		<small id="usernameHelp" class="form-text text-muted">Your OpenStack username.</small>
		</div>
		<div class="form-group">
  		<label for="password">Password</label>
  		<input v-model="credentials.password" type="password" class="form-control" id="password" placeholder="Password">
  		<br>
  		<input type="checkbox" id="catalog" value="Catalog" checked>
  		<label for="catalog">Catalog</label>
  		<small id="catalogHelp" class="form-text text-muted">Returns the catalog. Usually it is best to leave this on.</small>
		</div>
		<button @click="submit()" class="btn btn-primary">Login</button>
	</div>
</div>
</template>

<script>

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Api from '../api/api';

export default {
   data() {
      return {
        // We need to initialize the component with any
        // properties that will be used in it
        credentials: {
          username: '',
          password: ''
        },
        error: ''
      }
    },
    methods: {
      submit() {
        var credentials = {
          user: this.credentials.username,
          pass: this.credentials.password,
          debug: true,
          command: "custom --get --url http://sdibcportal.ims.tsisd.ca/com.broadsoft.xsi-actions/v2.0/user/3067190005@imstas.stb1.com/services?format=json"
        }
        // We need to pass the component's this context
        // to properly make use of http in the auth service
        var api = new Api()
        api.request(this, null, credentials, 'dashboard')
      }
    }
}


</script>