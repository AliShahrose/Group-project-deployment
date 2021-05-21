<template>
    <md-app>
        <md-app-content class="content">
            <span class="md-display-3"> Sign up or sign in </span>
            <span class="subheading"> <br>Welcome! Before you proceed you must sign in. If you don't have an account, sign up. </span>
            <div class="md-layout md-gutter sign-container">
                <div class="md-layout-item"><SignComp @login="onLogin" :signIn="false"/></div>
                <div class="md-layout-item"><SignComp @login="onLogin" :signIn="true"/></div>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
import SignComp from "../components/SignComp";

export default {
    name: "Login",
    components: { SignComp },
    methods: {
        onLogin() {
            // Send along to home page
            this.$router.push('home');
        }
    }
};
</script>

<style scoped>
.sign-container {
    margin-top: 20px;
    width: 80vw;
    display: inline-flex;
}
</style>