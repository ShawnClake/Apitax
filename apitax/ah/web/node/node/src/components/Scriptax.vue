<template>
		<div>
		    <h2>Scriptax</h2>
		    <p class="mb-2 text-muted">Control Flow, Scoping, and Automation.</p>
		    <p class="lead">For more help, please see the Apitax <a href="https://github.com/ShawnClake/Apitax/blob/master/README.md">documentation</a>.</p>
		
		    <hr>
		
		    <section>
		        <div class="row">
		            <div class="col">
		                <p class="lead">Using Account: <b><span id="accountSlot">{{username}}</span></b></p>
		                <p class="mb-2 text-muted">This utility prints the complete response to the browser dev-tools console in JSON format. Press F12 in chrome to view</p>
		                <hr>
		                <div class="row">
		
		                    <div class="col">
		                        <p class="lead">Flags</p>
		                        <div class="form-group" style="padding-left:15px;">
		                        <div class="row">
		                        <div class="col">
		                            <input type="checkbox" id="debug" value="Debug" v-on:change="commandChange" v-model="commandtaxParams">
		                            <label for="debug">Debug</label>
		                            <small id="debugHelp" class="form-text text-muted">Outputs verbose, detailed information
		                                    about the request.
		                                </small>
		                                </div>
		                            <div class="col">
		                            <input type="checkbox" id="sensitive" value="Sensitive" v-on:change="commandChange" v-model="commandtaxParams">
		                            <label for="sensitive">Sensitive</label>
		                            <small id="sensitiveHelp" class="form-text text-muted">Prevents post data sent with the
		                                    request from being output/logged.
		                                </small>
		                                
		                                </div>
		                                </div>
		                        </div>
		                    </div>
		                </div>
		            </div>
		        </div>
		    </section>
		
		    <hr>
		    
		    <section>
		    		<p class="lead">Available Scripts</p>
		    		<div class="row" style="padding-left:15px;padding-right:15px;">
		    		<div class="col" >
		    		  <b-table hover striped small :fields="fields" :sort-by.sync="sortBy" :sort-desc.sync="sortDesc" :items="scripts">
					       <!---<span slot="options" slot-scope="data" v-html="data.value"> -->
					       <template slot="options" slot-scope="data">
					       <b-btn size="sm" @click.stop="doScript(data.value,$event.target)" class="btn-success">Run</b-btn>  
					       </template>  
					     <!--- </span>--->
					    </b-table>
					   </div>
					   </div>
		    
		    
		    </section>
		    
		    <hr>
		
		    <section v-if="response!=''" style="//background-color:rgba(0,0,0,0.02)">
		        <div class="row">
		            <div class="col">
		                <p class="lead">Response: </p>
		                <p>
		                    <tree-view :options="{maxDepth: 1, rootObjectKey: 'response'}" :data="response"></tree-view>
		                </p>
		            </div>
		        </div>
		    </section>
		
		</div>
</template>


<script>
    import Api from '../api/api'

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    var api = new Api();
    export default {
        data: function () {
            return {
            		sortBy: 'label',
            		sortDesc: false,
                errors: [],
                authenticated: Api.authenticated,
                response: '',
                scripts: [],
                fields: [{key: 'options',label: '',tdClass:'align-middle'},{key: 'label',label: 'Script Name',tdClass:'align-middle',sortable:true},{key: 'relative-path',label: 'Script File',tdClass:'align-middle'},],
                scriptstemp: [{text: 'This is <i>escaped</i> content',html: 'This is <i>raw <strong>HTML</strong></i> <span style="color:red">content</span>'}],

            }
        },

        methods: {
        		doScript: function(scriptName, event)
        		{
        				let command = 'script ' + scriptName;
        				api.request(this, function(context, response) { console.log(response); context.response = response.data }, {
                    'token': '',
                    'debug': true,
                    'sensitive': false,
                    'command': command
                }, null);
        		},

				},
        mounted() {
		        api.catalogScripts(this, function(context, response) { 
		        		console.log(response); 
		        		//context.endpointPicker.endpoints = {...context.endpointPicker.endpoints, ...response.data.endpoints};
		        		
		        		let catalog = response.data.scripts; 
		        		
								var arrayLength = catalog.length;
								for (var i = 0; i < arrayLength; i++) {
										let optionsHtml = ''
										optionsHtml = catalog[i].path
								    catalog[i] = {...{options: optionsHtml}, ...catalog[i]};
								}
										        		
		        		context.scripts = catalog;
		        });
        }
    }
</script>

