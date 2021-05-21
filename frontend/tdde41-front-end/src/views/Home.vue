<template>
    <div>
        <md-app>
            <md-app-drawer md-permanent="clipped">
                <NavMenuComp />
            </md-app-drawer>
            <md-app-content>
                <span class="md-display-3"> Generic Quiz </span>
                <p class="md-subheading">
                    Welcome to the Generic Quiz (TM). Use the navigation buttons
                    on the left to navigate the application.
                    <br />
                    <b>"New quiz"</b> to start hosting a new quiz. <br />
                    <b>"Browse"</b> to find games hosted by other players.
                    <br />
                    <b>"Shop"</b> allows you to buy and sell {Insert something}.
                </p>
            </md-app-content>
        </md-app>
    </div>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";

export default {
    name: "Home",
    components: {
        NavMenuComp,
    },
};
</script>

<style scoped>

</style>