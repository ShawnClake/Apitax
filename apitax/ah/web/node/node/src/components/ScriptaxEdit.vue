<template>
		<div>
		    <h2>Scriptax Editor</h2>
		    <p class="mb-2 text-muted">Control Flow, Scoping, and Automation.</p>
		    <p class="lead">For more help, please see the Apitax <a href="https://github.com/ShawnClake/Apitax/blob/master/README.md">documentation</a>.</p>
		
		    <hr>
		
		    <section>
		        <div class="row">

                    <label class="lead col-1 " for="scriptName"><strong>Script:</strong></label>

                    <div class="col-7">
                    <input type="text" v-model="script.name" v-on:change="renameScript" placeholder="Type a name"
                           class="form-control"
                           id="scriptName">

                </div>
                
                <div class="col-4">
                
                		<button style="float:right;margin-left:10px;" v-on:click="doScript()" class="btn btn-success"><i class="fas fa-play"></i></button>
                		<button style="float:right;margin-left:10px;" v-on:click="saveScript()" class="btn btn-primary"><i class="far fa-save"></i></button>
                		<button style="float:right;" v-confirm="{loader: true,okText: 'Delete',cancelText: 'Cancel',ok: dialog => deleteScript(dialog),message: 'Are you sure you want to delete this script?'}" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
                		
                		
                
                </div>

		        </div>
		        
		        
		    </section>

		    <section>
		    		<div class="row" style="margin-top:15px;">
		    		<div class="col">
		    		<b-alert :show="alert.dismiss.countdown"
				             dismissible
				             :variant="alert.style"
				             @dismissed="alert.dismiss.countdown=0"
				             @dismiss-count-down="countDownChanged">
				      <p>{{alert.text}}</p>
				      <b-progress :variant="alert.style"
				                  :max="alert.dismiss.secs"
				                  :value="alert.dismiss.countdown"
				                  height="4px">
				      </b-progress>
				      <br>
				    </b-alert>
				    </div>
		    </div>
		    </section>
		    
		    <section>
		    
		    
		    <h4 v-if="(totalParams > 0)">Parameters</h4>
		    
		     	<div v-for="scriptparam in script.params" class="row" style="margin-top:15px;">
                                      
              <div class="col-2">
                  <label style="text-transform:capitalize;" class="lead" :for="scriptparam.id"><strong>{{scriptparam.label}}:</strong></label>
                  </div>
                  <div class="col-10">
                  <input type="text" v-model="scriptparam.value" placeholder="Type a value here"
                         class="form-control"
                         :id="scriptparam.id">

              </div>
           </div>
		    
		    
		    </section>
		    
		    
		    <section>
		    
		    <div class="row" style="margin-top:15px;">
		        <div class="col">
		        <codemirror ref="scriptCodeMirror" v-model="script.code" :options="cmOptions" @input="onCmCodeChange" @ready="onCmReady"></codemirror>
		        <button v-on:click="changeSize()" class="btn btn-sm btn-primary" style="width:100%;margin-top:5px;">{{this.editor.icon}}</button>
		    </div></div>
		    
		    </section>
		    
		    
		    <!---<section>
		    
				    <div class="row" style="margin-top:15px;">
		            <div class="col">
		                <p class="lead">Flags</p>
		                <div class="form-group" style="padding-left:15px;">
		                <div class="row">
		                <div class="col">
		                    <input type="checkbox" id="debug" value="Debug" v-on:change="optionsChange" v-model="globalOptions">
		                    <label for="debug">Debug</label>
		                    <small id="debugHelp" class="form-text text-muted">Outputs verbose, detailed information
		                            about the request.
		                        </small>
		                        </div>
		                    <div class="col">
		                    <input type="checkbox" id="sensitive" value="Sensitive" v-on:change="optionsChange" v-model="globalOptions">
		                    <label for="sensitive">Sensitive</label>
		                    <small id="sensitiveHelp" class="form-text text-muted">Prevents post data sent with the
		                            request from being output/logged.
		                        </small>
		                        
		                        </div>
		                        </div>
		                </div>
		            </div>
		        </div>--->
		        
		   <section v-if="script.response!=''" style="//background-color:rgba(0,0,0,0.02)">
		        <div class="row">
		            <div class="col">
		                <p class="lead">Response: </p>
		                <p>
		                    <tree-view :options="{maxDepth: 1, rootObjectKey: 'response'}" :data="script.response"></tree-view>
		                </p>
		            </div>
		        </div>
		    </section>
		    
		    
		    </section>
		    
		    
		    <hr>
	
		    
		</div>
</template>


<script>
    import Api from '../api/api'
    var api = new Api();
    
    export default {
        data: function () {
            return {
		            cmOptions: {
							        tabSize: 4,
							        mode: 'text/javascript',
							        lineNumbers: true,
							        line: true,
							  },
							  script: {
							  		path: "",
							  		name: "",
							  		code: "",
							  		params: {},
							  		response: "",
							  },
							  editor: {
							  		default: 300,
							  		icon: 'v',
										expanded: false,
							  },
							  codeMirror: {},
							  alert: {text: '', style: 'success', dismiss: {secs:10, countdown:0}},
		        }
        },

        methods: {
        		onCmReady(cm) {
				      this.codeMirror = cm;
				      this.codeMirror.setSize('100%', this.editor.default);
				    },
				    
				    onCmCodeChange(newCode) {
				      this.debouncedRenderParams();
				      //this.code = newCode
				    },
				    
				    renderParams() {
						    var scriptContents = this.script.code.replace(/\s/g, "").replace(/\n/g, "").replace(/\r/g, "");
        				
        				var reg = /options{[A-z0-9":\[\]{},]{0,}};/g;
								var result;
								var detected = false;
								
								while((result = reg.exec(scriptContents)) !== null) {
										detected = true;
								    var params = JSON.parse(result[0].slice(7, -1))['params'];
								    if(params)
								    {
								    		var newParams = {};
										    for (var i = 0; i < params.length; i++) {
										    		var label = params[i];
														newParams[label] = {"label": label, "value": "", "id": "id_param_"+label};
												}
												this.script.params = newParams;
								    } 

								}
								
								if(!detected)
								{
										this.script.params = {};
								}
				    
				    },
				    
				    changeSize() {
				    		
				    		if(this.editor.expanded)
				    		{
				    				this.codeMirror.setSize('100%', this.editor.default);
				    				this.editor.icon = 'v';
				    		} else {
				    				this.codeMirror.setSize('100%', 'auto');
				    				this.editor.icon = '^';
				    		}
				    		
				    		this.editor.expanded = !this.editor.expanded;
				    
				    },
				    
				    renameScript() {
				    		
				    		var newName = this.$store.state.scriptax.script.split("/");
				    		newName.pop();
				    		newName = newName.join("/") + '/' + this.script.name + '.ah';
				    		
				    		console.log(newName);
				    		
		        		api.renameScript(this, function(context, response) { 
		        		
		        						if(response.data.status == 500)
		        						{
		            						context.showAlert(response.data.message, 'danger');
				        				} else {
				        						context.$store.commit('useScript', {script: response.data['file-name']});
				        						context.updateScript();
				        						context.showAlert("Script was renamed successfully", 'success');
				        				}
		        		
		    				    },
		    				    {'file-name-original': this.script.path, 'file-name-new': newName}
		    				);
				    
				    },
				    
				    doScript() {
				    		var params = []
        		
        		    if(!(Object.keys(this.script.params).length === 0 && this.script.params.constructor === Object))
				        {
				        		Object.keys(this.script.params).forEach(key => {
											params.push(this.script.params[key]['value']);
										});
				        }
        		
        		    let command = 'script ' + this.script.path;
        				api.request(this, function(context, response) { 
		        				context.script.response = response.data 
		        				if(response.data.status == 500)
		        				{
		        						context.showAlert(response.data.body.flow.error.message, 'danger');
		        				} else {
		        						context.showAlert("Request was executed successfully", 'success');
		        				}
		        				
        				}, {
                    'token': '',
                    'debug': true,
                    'sensitive': false,
                    'command': command,
                    'parameters': params,
                }, null);
				    },
				    
				    deleteScript(dialog) {
            		api.deleteScript(this, function(context, response) { 
		        				    context.showAlert("Script was deleted.", 'success');
		        				    dialog.close();
		        				    context.$store.commit('useScript', {script: ''});
		        				    context.$router.push('/scriptax');
		    				    },
		    				    {'file-name': this.script.path}
		    				);

				    },
				    
				    saveScript() {
				   			api.saveScript(this, function(context, response) { 
		        				context.showAlert('The script was saved.', 'success');
        				},
        				{'file-name': this.script.path, 'file':this.script.code});
				    },
				    
				    countDownChanged (dismissCountDown) {
				      this.alert.dismiss.countdown = dismissCountDown;
				    },
				    showAlert (message, style) {
				    	this.alert.text = message;
				    	this.alert.style = style;
				      this.alert.dismiss.countdown = this.alert.dismiss.secs;
				    },
				    
				    updateScript()
				    {
				    		var path = this.$store.state.scriptax.script;
						    this.script.path = path;
		        		this.script.name = path.split("/").slice(-1)[0].split('.')[0];
				    },

				},
				
        computed: {
            totalParams: function () {
            		
            		return Object.keys(this.script.params).length;
            
            }
        
        },
						
				
        mounted() {
        		this.updateScript();
        		//this.updateScript(this.$store.state.scriptax.script);
        		//this.script.path = this.$store.state.scriptax.script;
        		//this.script.name = this.$store.state.scriptax.script.split("/").slice(-1)[0].split('.')[0];
        		
        		api.getScriptContents(this, function(context, response) { 
        				    context.script.code = response.data.contents
        				    context.renderParams();
    				    },
    				    {'file-name': this.script.path}
    				);
        		
        },
        created() {
					this.debouncedRenderParams = _.debounce(this.renderParams, 1000)
					//this.timer = setInterval(this.renderParams, 1500)
        },
    }
</script>

