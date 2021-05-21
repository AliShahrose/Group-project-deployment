<template>
    <md-app>
        <md-app-drawer md-permanent="clipped">
            <NavMenuComp />
        </md-app-drawer>
        <md-app-content>
            <span class="md-display-3"> About </span>
            <p class="md-subheading">
                The Generic Quiz (TM) was created by:
                <br> Frontend: Jacob and Robin
                <br> Rest: Other dudes
            </p>
        </md-app-content>
    </md-app>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";

export default {
    name: "About",
    components: {
        NavMenuComp,
    },
};
</script>

