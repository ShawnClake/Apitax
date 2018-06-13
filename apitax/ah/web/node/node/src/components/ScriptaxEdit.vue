<template>
		<div>
		    <h2>Scriptax Editor</h2>
		    <p class="mb-2 text-muted">Control Flow, Scoping, and Automation.</p>
		    <p class="lead">For more help, please see the Apitax <a href="https://github.com/ShawnClake/Apitax/blob/master/README.md">documentation</a>.</p>
		
		    <hr>
		
		    <section>
		        <div class="row">
		            <div class="col">
		                <p class="lead">Script: <b><span id="accountSlot">{{script.name}}</span></b></p>
		            </div>
		        </div>
		    </section>
		
		    <hr>
		    
		    <!---<section>
		    		
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
				    </b-alert>
		    
		    </section>-->
		    
		    
		    <!---<section>
		    
				    <div class="row">
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
            		
            }
        },

        methods: {
        		

				},
				
				computed: {
						script: function() {
								
								return {name: this.$store.state.scriptax.script}
						
						},
			
				},
						
				
        mounted() {

        },
        created() {
					//this.timer = setInterval(this.codeChange, 250)
        },
    }
</script>

