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
                    <p class="mb-2 text-muted">This utility prints the response JSON to the browser console. Press F12
                        in chrome to view</p>
                    <div class="form-group">
                        <label class="lead" for="command">Command</label>
                        <input type="text" v-on:keyup="commandChange" placeholder="Type a command here"
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
                        </div>
                        <div class="col align-self-center">
                            <div class="form-group">
                                <input type="checkbox" id="debug" value="Debug" v-model="commandtaxParams">
                                <label for="debug">Debug</label>
                                <small id="debugHelp" class="form-text text-muted">Outputs verbose, detailed information
                                    about the request.
                                </small>
                                <br>
                                <input type="checkbox" id="sensitive" value="Sensitive" v-model="commandtaxParams">
                                <label for="sensitive">Sensitive</label>
                                <small id="sensitiveHelp" class="form-text text-muted">Prevents post data sent with the
                                    request from being output/logged.
                                </small>
                            </div>
                        </div>
                    </div>
                    <hr>
                    <div class="row">
                        <div class="col">
                            <p class="lead">Generated Commandtax: <br> <span
                                    style="font-family: 'Courier New';font-size:12pt;"
                            >> <span v-html="generatedCommandtax"> </span></span></p>
                        </div>
                    </div>
                    <div class="row">
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

        <section style="//background-color:rgba(0,0,0,0.02)">
            <div class="row">
                <div class="col">
                    <p class="lead">Output: </p>
                    <p>{{response}}</p>
                </div>
            </div>
        </section>


    </div>
</template>


<script>
    import Api from '../api/api'

    function commandMaker(command, endpointPicker) {
        if (endpointPicker != '' && endpointPicker != 'custom') {
            let temp = command.split('--url ');
            let returner = temp[0] + '--url ' + endpointPicker;
            if (temp.length > 1) {
                returner += temp[1]
            }
            return returner;
        } else {
            return command;
        }
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
                endpointPicker: {
                    endpoints: {
                        custom: {label: "Custom", value: "custom"},
                        temp: {label: "Test", value: "https://jsonplaceholder.typicode.com"}
                    }, selected: "custom"
                },
                endpoint: '',
                username: '',
                response: '',
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

                api.request({
                    'token': '',
                    'debug': debug,
                    'sensitive': sensitive,
                    'command': this.generatedCommandtax
                }, null);


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
            commandChange: function (evt) {
                /*if(this.endpointPicker != '' && this.endpointPicker != 'custom')
                {
                    var temp = this.command.split('--url ');
                    app.requestFeedback = temp[0] + '--url ' + this.endpointPicker + temp[1];
                } else
                    {
                        app.requestFeedback = this.command;
                    }*/

                this.generatedCommandtax = commandMaker(this.command, this.endpoint)
            }
        },
        created() {

        }
    }
</script>

