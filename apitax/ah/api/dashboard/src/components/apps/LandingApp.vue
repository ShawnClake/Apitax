<!-- src/components/App.vue -->

<template>
    <div>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
            <div class="container-fluid">
                <router-link class="navbar-brand js-scroll-trigger" to="/home">Apitax</router-link>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive"
                        aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active">
                            <router-link class="nav-link" to="/home">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/login" v-if="!authenticated">Login</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link class="nav-link" to="/dashboard" v-if="authenticated">Dashboard</router-link>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" v-if="authenticated" @click="logout()">Logout</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>


        <header class="bg-primary text-white">
            <div class="container-fluid">
                <br><br><br>
                <h1 class="text-center">Apitax</h1>
                <p class="lead text-center">Combining the power of Scriptax and Commandtax into one neat little
                    package</p>
            </div>
        </header>

        <section id="viewsection" class="bg-light" style="padding-top:15px;padding-bottom:15px">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-8 mx-auto">
                        <router-view></router-view>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="py-5 bg-dark">
            <div class="container-fluid">
                <p class="m-0 text-center text-white"><a href="https://github.com/ShawnClake/Apitax">Apitax </a>2018</p>
            </div>
            <!-- /.container -->
        </footer>
    </div>
    
</template>

<script>
    export default {
        data: function () {
            return {
                errors: [],
                system_status: false,
                driver_status: false,

            }
        },

        methods: {

        },
       
    }
</script>