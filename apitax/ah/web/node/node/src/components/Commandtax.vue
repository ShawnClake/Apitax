<template>
    <div>
        <h2>Commandtax</h2>
        <p class="mb-2 text-muted">API Usage and Data Gathering/Manipulating.</p>
        <p class="lead">For more help, please see the Apitax <a
                href="https://github.com/ShawnClake/Apitax/blob/master/README.md">documentation</a>.</p>

        <hr>

        <section>
            <div class="row">
                <div class="col">
                    <p class="lead">Using Account: <b><span id="accountSlot">{{username}}</span></b></p>
                    <p class="mb-2 text-muted">This utility prints the complete response to the browser dev-tools console in JSON format. Press F12
                        in chrome to view</p>
                    <div class="form-group">
                        <label class="lead" for="command">Command</label>
                        <input type="text" v-on:keyup="commandTextChange" placeholder="Type a command here. e.g. (custom, script, shell)"
                               class="form-control"
                               id="command" v-model="command">
                    </div>
                    <hr>
                    <div class="row">
                        <div class="col">
                            <!-- Endpoint Helper -->
                            <div class="form-group">
                                <label class="lead" for="endpointPicker">Base Endpoint</label>
                                <select id="endpointPicker" v-on:change="endpointChange" class="custom-select"
                                        v-model="endpointPicker.selected">
                                    <option v-for="option in endpointPicker.endpoints"
                                            :value="option.value">
                                        {{option.label}}
                                    </option>
                                </select>
                                <br>
                                <div v-if="endpointPicker.selected == 'custom'" style="margin-top:15px;">
                                    <label class="lead" for="custom_endpoint">Custom Endpoint</label>
                                    <input id="custom_endpoint" v-model="endpoint" v-on:keyup="customEndpointChange"
                                           placeholder="Type a custom endpoint here" type="text" class="form-control">
                                </div>
                                <!--<select id="endpointPicker" v-on:change="commandChange" class="custom-select"
                                        v-html="endpoints"
                                        v-model="endpointPicker">

                                </select>-->
                            </div>
                            
                             <div class="form-group">
                                <label class="lead" for="endpointPicker">Request Type</label>
                                <select id="requestTypePicker" v-on:change="requestTypeChange" class="custom-select"
                                        v-model="requestTypePicker.selected">
                                    <option v-for="option in requestTypePicker.requestTypes"
                                            :value="option.value">
                                        {{option.label}}
                                    </option>
                                </select>
                            </div>
                            
                            
                        </div>
                        <div class="col">
                        <p class="lead">Flags</p>
                            <div class="form-group" style="padding-left:15px;">
                                <input type="checkbox" id="debug" value="Debug" v-on:change="commandChange" v-model="commandtaxParams">
                                <label for="debug">Debug</label>
                                <small id="debugHelp" class="form-text text-muted">Outputs verbose, detailed information
                                    about the request.
                                </small>
                                <br>
                                <input type="checkbox" id="sensitive" value="Sensitive" v-on:change="commandChange" v-model="commandtaxParams">
                                <label for="sensitive">Sensitive</label>
                                <small id="sensitiveHelp" class="form-text text-muted">Prevents post data sent with the
                                    request from being output/logged.
                                </small>
                                <br>
                                <input type="checkbox" id="escape" value="Escape" v-on:change="commandChange" v-model="commandtaxParams">
                                <label for="escape">Escape</label>
                                <small id="escapeHelp" class="form-text text-muted">Escapes double quotes. Useful when generating commands for Scriptax
                                </small>
                            </div>
                        </div>
                    </div>
                    <hr>
                    <div class="row">
                    <div class="col">
                   			<p class="lead">Data</p>
                   			<div v-if="(dataMakers.includes('Post') || dataMakers.includes('Query') || dataMakers.includes('Path'))"><p class="mb-2 text-muted">The generated command does not automatically update after each keystroke for data fields due to latency issues.</p></div>
                   	
                   			<div class="form-group">
                   			<div class="form-check form-check-inline">
                   			<input class="form-check-input" type="checkbox" id="post" value="Post" v-model="dataMakers">
                        <label class="form-check-label" for="post">Post</label>
                   			</div>
                   			<div class="form-check form-check-inline">
                   			<input class="form-check-input" type="checkbox" id="query" value="Query" v-model="dataMakers">
                        <label class="form-check-label" for="query">Query Param</label>
                   			</div>
                   			<div class="form-check form-check-inline">
                   			<input class="form-check-input" type="checkbox" id="path" value="Path" v-model="dataMakers">
                        <label class="form-check-label" for="path">Path Injection <span v-if="(totalPaths > 0)" class="badge badge-pill badge-danger">{{totalPaths}}</span></label>
                   			</div>
                   			</div>
                   			
                   					
                   			<div v-if="(dataMakers.includes('Post'))">
                   					<div class="row">
                   					<div class="col">
		                   				  <div class="form-group">
															   	 <label class="lead" for="postDataText">POST JSON</label>
															   	 <p class="mb-2 text-muted">Use double quotes i.e " not '</p>
															   	 <textarea class="form-control" id="postDataText" rows="3" v-on:change="commandChange" v-model="data.post"></textarea>
															  </div>
                   					</div>
                   					</div>
                   			</div>
                   			
                   			<div v-if="(dataMakers.includes('Query'))">                   					
                   					<div class="row">
                   					<div class="col">
		                   				  <div class="form-group">
															   	 <label class="lead" for="queryDataText">Query Params (?query=data&under=stand)</label>
															   	 <p class="mb-2 text-muted">Use double quotes i.e " not '</p>
															   	 <textarea class="form-control" id="queryDataText" rows="3" v-on:change="commandChange" v-model="data.query"></textarea>
															  </div>
                   					</div>
                   					</div>
                   			</div>
                   			
                   			<div v-if="(dataMakers.includes('Path'))">                   					
                   					<div class="row">
                   					<div class="col">
                   							<label class="lead">Path Injection (endpoint/{test} <= {test}: users)</label>
                   					       <div v-for="pathparam in data.path" class="row" style="margin-top:15px;">
                                      
                                      <div class="col-2">
									                        <label class="lead" :for="pathparam.id"><strong>{{pathparam.label}}:</strong></label>
									                        </div>
									                        <div class="col-10">
									                        <input type="text" v-model="pathparam.value" v-on:change="commandTextChange" placeholder="Type a value here"
									                               class="form-control"
									                               :id="pathparam.id">

									                    </div>
                                   </div>
                   					</div>
                   					</div>
                   			</div>
                   			
                    </div>
                    </div>
                    <hr>
                    <div class="row">
                        <div class="col">
                            <p class="lead">Generated Commandtax:</p>
                            
                            <div class="row" style="border-left: 6px solid #ccc!important; color: #000!important; background-color: #ddffff!important; border-color: #2196F3!important;">
                            
                            <div class="col-1 col-xs-1 text-center"  style="flex: 0 0 2.333333% !important; max-width: 2.333333% !important;"
                                    
                            >
                            
                            <span style="font-family: 'Courier New';font-size:12pt;">></span>
                            
                            </div>
                            <div class="col-11 col-xs-11">
                            <span style="font-family: 'Courier New';font-size:12pt;" v-html="generatedCommandtax"> </span>
                            </div>
                            
                            </div>
                        </div>
                    </div>
                    <div class="row" style="margin-top:15px">
                        <div class="col align-self-center">
                            <div class="form-group ">
                                <button v-on:click="commandChange" class="btn btn-primary float-left">Regenerate Command
                                </button>
                            </div>
                        </div>
                        <div class="col align-self-center">
                            <div class="form-group ">
                                <button v-on:click="doCommand" class="btn btn-success float-right">Execute Command
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <hr>

        <section v-if="response!=''"  style="//background-color:rgba(0,0,0,0.02)">
            <div class="row">
                <div class="col">
                    <p class="lead">Response: </p>
                    <p><tree-view :options="{maxDepth: 1, rootObjectKey: 'response'}" :data="response"></tree-view></p>
                </div>
            </div>
        </section>



    </div>
</template>


<script>
    import Api from '../api/api'

		function encodeHTML(s) {
		    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
		}
		
	  function decodeHTML(s) {
		    return s.replace('&amp;', /&/g).replace('&lt;', /</g).replace('&quot;', /"/g);
		}

    function commandMaker(command, endpointPicker, commandtaxParams, data, requestTypePicker) {
        command += " ";
        let returner = ""; 
        if (endpointPicker != '' && endpointPicker != 'custom') {
            let temp = command.split('--url ');
            returner = temp[0] + '--url ' + endpointPicker;
            if(endpointPicker.slice(-1) != '/')
            {
            		returner += "/";
            }
            if (temp.length > 1) {
                returner += temp[1]
            }
        } else {
            returner = command;
        }
        
        returner = returner.split(" ")

        if (requestTypePicker != '' && requestTypePicker != 'custom') {
        		returner.splice(1, 0, "--"+requestTypePicker);
        }

        if (commandtaxParams.includes('Sensitive'))
            returner.splice(1, 0, "--sensitive");
        if (commandtaxParams.includes('Debug'))
            returner.splice(1, 0, "--debug");
            
        if(data.post != '')
        {
        		returner.push('--data-post \''+data.post+'\'');
        }
        
        if(data.query != '')
        {
        		returner.push('--data-query \''+data.query+'\'');
        }
        
        if(!(Object.keys(data.path).length === 0 && data.path.constructor === Object))
        {

        		let newPath = {}
        		
        		Object.keys(data.path).forEach(key => {
							newPath[data.path[key]['label']] = data.path[key]['value'];
						});
						returner.push('--data-path \'' + JSON.stringify(newPath) + '\'');
        }
        
        var reg = /{[A-z0-9]{1,}}/g;
				var result;
				var previous = data.path;
				data.path = {};
				//console.log(returner[returner.indexOf('--url')+1])
				while((result = reg.exec(returner[returner.indexOf('--url')+1])) !== null) {
				    //console.log(result);
				    var label = result[0].slice(1,-1);
				    
				    var value = ""
				    //console.log(previous)
				    if (label in previous)
				    {
				        value = previous[label]['value']
				    }
				    data.path[label] = {"label": label, "value": value, "id": "id_path_"+label}
				}
        
        returner = returner.join(" ");
        
        if (commandtaxParams.includes('Escape'))
            returner = returner.split('"').join('\\"');
        
        return returner
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    var api = new Api();
    export default {
        data: function () {
            //var api = new Api();
            return {
                errors: [],
                command: '',
                generatedCommandtax: 'Awaiting command',
                commandtaxParams: [],
                dataMakers: [],
                data: {post: '', query: '', path: {}}, //"981":{label:"981", value: "", id: "id_path_981"}
                endpointPicker: {
                    endpoints: {
                        custom: {label: "Custom", value: "custom"},
                    }, selected: "custom"
                },
                endpoint: '',
                requestTypePicker: {
                    requestTypes: {
                        custom: {label: "Custom", value: "custom"},
                        get: {label: "Get", value: "get"},
                        post: {label: "Post", value: "post"},
                        patch: {label: "Patch", value: "patch"},
                        put: {label: "Put", value: "put"},
                        delete: {label: "Delete", value: "delete"}
                    }, selected: "get"
                },
                requestType: 'get',
                username: '',
                response: '',
                globals: {debug:false, sensitive:false},
                authenticated: Api.authenticated

            }
        },

        methods: {
            doCommand: function () {
                //app.requestFeedback = "Executing command";
                let debug = false;
                let sensitive = false;
                if (this.commandtaxParams.includes('Debug'))
                    debug = true;
                if (this.commandtaxParams.includes('Sensitive'))
                    sensitive = true;

                var something = api.request(this, function(context, response) { console.log(response); context.response = response.data }, {
                    'token': '',
                    'debug': this.globals.debug,
                    'sensitive': this.globals.sensitive,
                    'command': this.generatedCommandtax
                }, null);
                
                //console.log("something:"+something)


                //app.requestFeedback = "<small id='responseHelp' class='form-text text-muted'>Response returned at " + new Date().toLocaleString() + "</small>Command: " + commandMaker();

                //var newCmd = '';
                //newCmd += "<button class='btn btn-sm btn-success float-left'><</button>";
                //newCmd += "<li><span style='margin-left:10px;'>" + commandMaker() + "</span></li>";
                //newCmd += "<br>"

                //app.cHistory = newCmd + app.cHistory;
            },
            customEndpointChange: function (evt) {
                this.commandChange();
            },
            endpointChange: function (evt) {

                if (this.endpointPicker.selected == "custom") {
                    this.endpoint = '';
                } else {
                    this.endpoint = this.endpointPicker.selected;
                }

                this.commandChange();

            },
            requestTypeChange: function (evt) {

                if (this.requestTypePicker.selected == "custom") {
                    this.requestType = '';
                } else {
                    this.requestType = this.requestTypePicker.selected;
                }

                this.commandChange();

            },
            commandTextChange: function(evt) {
            

            
            		this.commandChange();
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

                this.generatedCommandtax = commandMaker(this.command, this.endpoint, this.commandtaxParams, this.data, this.requestType)
            }
        },
        computed: {
            totalPaths: function () {
            		
            		return Object.keys(this.data.path).length;
            
            }
        
        },
        mounted() {
						api.catalogEndpoints(this, function(context, response) { console.log(response); context.endpointPicker.endpoints = {...context.endpointPicker.endpoints, ...response.data.endpoints}; context.endpointPicker.selected = response.data.selected; context.endpoint = response.data.selected;});
            //api.catalogScripts(this, function(context, response) { console.log(response); });
        }
    }
</script>

