import axios from 'axios';

let BASE_URL = '/apitax/2/';
let SYSTEM_URL = BASE_URL + 'system/status';
let CATALOG_URL = BASE_URL + 'system/catalog';
let SCRIPTS_URL = BASE_URL + 'system/script';
let API_URL = BASE_URL + 'command';
let AUTH_URL = BASE_URL + 'auth';

var auth = {
	'auth': false
};

export {auth, BASE_URL};

export function login(username, password, context, callback, successRedirect)
{
	var self = this;
	axios.post(`/apitax/2/auth`, {
  			"username": username,
  			"password": password,
  		})
      .then(response => {
          if(response.data.status == 201)
          {
          	localStorage.setItem('access_token', response.data.access_token);
          	localStorage.setItem('refresh_token', response.data.refresh_token);
          	localStorage.setItem('api_token', response.data.auth.api_token);
          	localStorage.setItem('username', response.data.auth.username);
          	auth['auth'] = true
          	callback(context, response.data);
          	if(successRedirect)
          		window.location.href = successRedirect;
          	//window.location.href = '/apitax/2/dashboard';
          } else {
          	callback(context, response.data);
          }
      })
      .catch(e => {
          callback(context, e);
  })
}

export function getApiToken()
{
	return localStorage.getItem('api_token');
}

export function logout(successRedirect)
{
	localStorage.removeItem('refresh_token');
	localStorage.removeItem('access_token');
	localStorage.removeItem('api_token');
	localStorage.removeItem('username');
	auth['auth'] = false
	if(successRedirect)
		window.location.href = successRedirect;
}

export function redirectIfUnauthenticated(redirect)
{
		if(localStorage.getItem('access_token'))
		context['auth'] = true
	
	if(!renewToken(auth, function(context, response) {
		if(response.status == 201)
		{
			context['auth'] = true
		} else {
			context['auth'] = false
			logout(redirect)
		}
	}))
	{
		context['auth'] = false
		logout(redirect)
	}
}

export function isAuthenticated(context, callback)
{
	if(localStorage.getItem('access_token'))
	{
		context['auth'] = true
		callback(context, true); 
	}
	
	if(!renewToken(auth, function(context, response) {
		if(response.status == 201)
		{
			context['auth'] = true
			callback(context, true); 
		} else {
			context['auth'] = false
			logout(null)
			callback(context, false); 
		}
	}))
	{
		context['auth'] = false
		logout(null)
		callback(context, false); 
	}
}

export function checkAuthenticated()
{
	if(localStorage.getItem('access_token'))
		context['auth'] = true
	
	if(!renewToken(auth, function(context, response) {
		if(response.status == 201)
		{
			context['auth'] = true
		} else {
			context['auth'] = false
			logout(null)
		}
	}))
	{
		context['auth'] = false
		logout(null)
	}
}

export function renewToken(context, callback)
{
	var self = this;
	let config = getRefreshHeaders()
	if(config === null)
	{
		return false
	}
	
	axios.post(`/apitax/2/token/refresh`, {}, config)
			.then(response => {
          if(response.data.status == 201)
          {
          	localStorage.setItem('access_token', response.data.access_token);
          }
          	
          callback(context, response.data);  
      })
      .catch(e => {
      	callback(context, e); 
      })
      
  return true
}

export function getRefreshHeaders()
{
		let token = localStorage.getItem('refresh_token');
		if(token === null)
			return null;
			
		let config = {
	    headers: {
	      'Authorization': 'Bearer ' + localStorage.getItem('refresh_token')
	    }
	  }
	  
	  return config
}

export function getAuthHeaders()
{
		let token = localStorage.getItem('access_token');
		if(token === null)
			return null;
			
		let config = {
	    headers: {
	      'Authorization': 'Bearer ' + localStorage.getItem('access_token')
	    }
	  }
	  
	  return config
}

export function command(command, context, callback)
{
	var self = this;
	
}


// BREAK POINT - UPDATE CODE BELOW


export function request(context, callback, data, redirect) {
    var self = this;
    axios.post(API_URL, data, getAuthHeaders())
        .then(function (response) {
            if (redirect) {
                //router.push(redirect)
            }
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });
}


export function catalogEndpoints(context, callback) {
    var self = this;
    axios.get(CATALOG_URL, getAuthHeaders())
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}


export function catalogScripts(context, callback) {
    var self = this;
    axios.get(SCRIPTS_URL + '/catalog', getAuthHeaders())
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}

export function getScriptContents(context, callback, data) {
    var self = this;
    axios.get(SCRIPTS_URL, {...{
        params: {
            name: data.name
        }
    }, ...getAuthHeaders()})
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}

export function createScript(context, callback, data) {
    var self = this;
    axios.post(SCRIPTS_URL, data, getAuthHeaders())
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}

export function saveScript(context, callback, data) {
    var self = this;
    axios.put(SCRIPTS_URL, data, getAuthHeaders())
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}


export function renameScript(context, callback, data) {
    var self = this;
    axios.patch(SCRIPTS_URL, data, getAuthHeaders())
        .then(function (response) {
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}

export function deleteScript(context, callback, data) {
    var self = this;
    var setup  = {data: data};
    axios.delete(SCRIPTS_URL, {...setup, ...getAuthHeaders()})
        .then(function (response) {
            console.log(response)
            callback(context, response);
        })
        .catch(function (error) {
            console.log(error);
        });

}


