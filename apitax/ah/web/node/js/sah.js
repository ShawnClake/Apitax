var token;

function commandMaker()
{
    	if(app.endpointPicker != '' && app.endpointPicker != 'custom')
    	{
    		var temp = app.command.split('--url ');
    		return temp[0] + '--url ' + app.endpointPicker + temp[1];
    	} else 
    		{
    			return app.command;
    		}
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

/*
Vue.JS Application
*/
var app = new Vue({
  el: '#app',
  data: {
    command: '',
    loggedin: false,
    requestFeedback: 'Awaiting command',
    apiParams: [],
    endpointPicker: '',
    catalogPoints: '',
    username: '',
    cHistory: '',
  },
  methods: {
    doCommand: function () {
      app.requestFeedback = "Executing command";
      var debug = false;
      var sensitive = false;
      if(this.apiParams.includes('Debug'))
      	debug = true;
      if(this.apiParams.includes('Sensitive'))
      	sensitive = true;
      api(commandMaker(), debug, sensitive);
      app.requestFeedback = "<small id='responseHelp' class='form-text text-muted'>Response returned at " + new Date().toLocaleString() + "</small>Command: " + commandMaker();
      
      var newCmd = '';
      //newCmd += "<button class='btn btn-sm btn-success float-left'><</button>";
      newCmd += "<li><span style='margin-left:10px;'>"+commandMaker() +"</span></li>";
      //newCmd += "<br>"
      
      app.cHistory = newCmd + app.cHistory;
      

      
    },
    
    injectCmd: function(cmd, endpoint) {
    	alert(cmd + endpoint);
    },
    
    commandChange: function (evt) {
    	/*if(this.endpointPicker != '' && this.endpointPicker != 'custom')
    	{
    		var temp = this.command.split('--url ');
    		app.requestFeedback = temp[0] + '--url ' + this.endpointPicker + temp[1];
    	} else 
    		{
    			app.requestFeedback = this.command;
    		}*/
    		
    		app.requestFeedback = "Command: " + commandMaker()
    }
  }
})



/*
Used to make API calls
*/
function api(command, debug, sensitive) {

    

    $.ajax({
        type: "POST",
        //the url where you want to sent the userName and password to
        url: 'http://172.25.190.4:5080/api/command/',
        dataType: 'json',
        contentType: 'application/json',
        async: false,
        //json object to sent to the authentication url
        data: JSON.stringify({
            "token": token,
            "command": command,
            "debug": debug,
            "sensitive": sensitive
        }),

    }).done(function(somedata) {
        console.log("Data Loaded: " + JSON.stringify(somedata));
        
    });
}

/*
Used to complete authentication
*/
function login()
{

    $.ajax({
        type: "POST",
        //the url where you want to sent the userName and password to
        url: 'http://172.25.190.4:5080/api/auth/',
        dataType: 'json',
        contentType: 'application/json',
        async: false,
        //json object to sent to the authentication url
        data: JSON.stringify({
            "user": $('#username').val(),
            "pass": $('#password').val(),
            "catalog": $('#catalog').prop('checked'),
        }),

    }).done(function(somedata) {
        console.log("Data Loaded: " + JSON.stringify(somedata));
        token = somedata['token'];
        console.log(token)
        if(token)
        {
           app.username = $('#username').val();
        }

				//var response = JSON.parse(somedata);

				

				if(somedata['body']['token']['catalog'])
				{
					var cPoints = '';
					var catalog = somedata['body']['token']['catalog'];
					cPoints += '<option value="custom" selected="selected">Custom</option>';
					$.each(catalog, function(i, item) {
						var catName = item['name'];
						var catPoints = item['endpoints'];
						var catPoint = '';
    				$.each(catPoints, function(i, point) {
    					if(point['interface'] === 'public')
    					{
    						catPoint = point;
    					}
    				});
    				
    				if(catPoint)
    				{
    					//cPoints += '<p>test</p>';
    					//alert(catName + '@' + catPoint['url']);
    					//cPoints += '<input type="radio" id="endp'+catName+'" value="'+capitalizeFirstLetter(catName)+'" v-model="endpointPicker">';
    					//cPoints += '<label for="endp'+catName+'">'+capitalizeFirstLetter(catName)+'</label>';
    					//cPoints += '<small id="endp'+catName+'help" class="form-text text-muted">'+capitalizeFirstLetter(item['type'])+'</small>';
    					//cPoints += '<br>';
    					
    					
    					cPoints += '<option value="'+catPoint['url']+'">'+capitalizeFirstLetter(catName)+'</option>';
    					
    					
    				
    				}
    				
					});
					app.catalogPoints = cPoints;
					// This means a catalog object has been returned
				}

        app.loggedin = true;
        
        //api("domain list all", true, false);
        //api("project list all", true, false);
        //api("project list", true, false);
        //api("script scripts/script.ah", true, false);

    });


}

/*
Doesn't do anything yet
*/
$(document).ready(function() {
    //var client = new $.RestClient('http://172.25.190.4:5080/api/');
    //client.add('command');
    //client.command.create({u:"api_admin",p:"apiadmin123",c:"domain list all"}).done(function(data) {
    //  alert(data);  
    //});

    //$.ajaxSetup({
    //   headers:{
    //      'Content-Type': "application/json"
    //   }
    //});

    //$.post( "http://172.25.190.4:5080/api/command/", {u:"api_admin",p:"apiadmin123",c:"domain list all"}).done(function( data ) {
    //  console.log( "Data Loaded: " + data );
    //});






});