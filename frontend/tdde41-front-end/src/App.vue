<template>
    <div id="app">
        <md-toolbar class="md-dense md-primary">
            <router-link
                style="flex: 1; text-align: left"
                to="/home"
                class="md-title"
                >Generic Quiz</router-link
            >
            <md-button
                class="md-icon-button"
                v-if="$route.name !== 'Login'"
                v-on:click.native="logout"
            >
                <md-icon>logout</md-icon>
            </md-button>
        </md-toolbar>

        <router-view />
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "App",
    methods: {
        logout() {
            this.$router.push("login");
            axios.post(process.env.VUE_APP_BACKEND_URL + "logout", null, {
                withCredentials: true,
            });
        },
    },
};
</script>


<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}

#nav {
    padding: 30px;
}

#nav a {
    font-weight: bold;
    color: #2c3e50;
}

#nav a.router-link-exact-active {
    color: #42b983;
}
</style>
