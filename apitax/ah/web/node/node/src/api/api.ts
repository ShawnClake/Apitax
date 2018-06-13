//const API_URL = 'http://localhost:3001/'
//const LOGIN_URL = API_URL + 'sessions/create/'
//const SIGNUP_URL = API_URL + 'users/'

const SYSTEM_URL = '/apitax/system/status'
const CATALOG_URL = '/apitax/system/catalog'
const SCRIPTS_URL = '/apitax/system/scripts'
const API_URL = '/apitax/command/'
const AUTH_URL = '/apitax/auth/'

import {router} from '../index'
import axios from 'axios';
// user, pass, command, debug
export default class Api {
    static authenticated: boolean = false;
    static username: string = "";
    static status: any;

    constructor() {
        this.systemStatus();
        this.checkAuth();

    }

    login(context: any, credentials: {}) {
        //alert(JSON.stringify(credentials));
        var self = this;
        axios.post(AUTH_URL, credentials)
            .then(function (response) {
                console.log(response);
                localStorage.setItem('token', (response as any).token as any);
                console.log((response as any).request.responseText)
                Api.authenticated = true;
            })
            .catch(function (error) {
                console.log(error);
            });
    }


    request(context: any, callback: any, data: any, redirect: string) {
        //alert(JSON.stringify(data));
        var self = this;
        axios.post(API_URL, data)
            .then(function (response) {
                console.log(response);
                //console.log(data)
                //console.log(console.log("my object: %o", self.user))
                //Api.username = data.user

                console.log((response as any).request.responseText)
                //Api.authenticated = true;
                //localStorage.setItem('username', Api.username);
                //localStorage.setItem('authenticated', String(Api.authenticated));
                if (redirect) {
                    router.push(redirect)
                }
                callback(context, response);
                //console.log("SOMETHING" + context.endpointPicker.selected)
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    
    
    catalogEndpoints(context: any, callback: any) {
        var self = this;
        axios.get(CATALOG_URL)
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }
    
    
    catalogScripts(context: any, callback: any) {
        var self = this;
        axios.get(SCRIPTS_URL + '/catalog')
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }
    
    getScriptContents(context: any, callback: any, data: any) {
        var self = this;
        axios.post(SCRIPTS_URL, data)
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }
    
    saveScript(context: any, callback: any, data: any) {
        var self = this;
        axios.post(SCRIPTS_URL + '/save', data)
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }
    
    
    renameScript(context: any, callback: any, data: any) {
        var self = this;
        axios.post(SCRIPTS_URL + '/rename', data)
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }
    
    deleteScript(context: any, callback: any, data: any) {
        var self = this;
        axios.post(SCRIPTS_URL + '/delete', data)
            .then(function (response) {
                console.log(response);

                console.log((response as any).request.responseText)

                callback(context, response);
            })
            .catch(function (error) {
                console.log(error);
            });
    
    }


    systemStatus() {
        //alert(JSON.stringify(data));
        var self = this;
        axios.get(SYSTEM_URL)
            .then(function (response) {
                console.log(response);
                console.log((response as any).request.responseText);
                //return true;
                Api.status = response;
                return response;
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    logout() {
        localStorage.removeItem('authenticated')
        Api.authenticated = false
        router.push('home')
    }

    checkAuth() {
        var storedUser = localStorage.getItem('username')
        var authenticated: boolean = Boolean(localStorage.getItem('authenticated'))
        if (authenticated && storedUser) {
            Api.username = storedUser
            Api.authenticated = authenticated
        }
        else {
            Api.authenticated = false
        }
    }


}

