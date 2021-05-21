<template>
    <md-app>
        <md-app-drawer md-permanent="clipped">
            <NavMenuComp />
        </md-app-drawer>

        <md-app-content>
            <span class="md-display-3"> Browse </span>
            <!-- md-height="100%" -->
            <md-table
                v-model="lobbies"
                md-sort="name"
                md-sort-order="asc"
                md-card
                md-height="100%"
                md-fixed-header
                @md-selected="onSelect"
            >
                <md-table-toolbar>
                    <div class="md-toolbar-section-start">
                        <h1 class="md-title">Lobbies</h1>
                    </div>
                    <md-button
                        class="md-raised md-primary"
                        v-on:click.native="onRefresh"
                        >Refresh</md-button
                    >
                </md-table-toolbar>

                <md-table-row
                    slot="md-table-row"
                    slot-scope="{ item }"
                    md-selectable="single"
                >
                    <md-table-cell
                        md-label="Lobby Name"
                        md-sort-by="lobbyName"
                        >{{ item.lobbyName }}</md-table-cell
                    >
                    <md-table-cell md-label="Host Name" md-sort-by="hostName">{{
                        item.hostName
                    }}</md-table-cell>
                    <md-table-cell
                        md-label="Players"
                        md-sort-by="nPlayers"
                        md-numeric
                        >{{
                            item.nPlayers + "/" + item.maxPlayers
                        }}</md-table-cell
                    >
                </md-table-row>
            </md-table>
        </md-app-content>
    </md-app>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";
import axios from "axios";

export default {
    name: "Browse",
    components: {
        NavMenuComp,
    },
    data: () => ({
        lobbies: [],
    }),
    methods: {
        onSelect(item) {
            if (item) {
                axios
                    .get(
                        process.env.VUE_APP_BACKEND_URL +
                            "joinroom/" +
                            item.lobbyName,
                        {
                            withCredentials: true,
                        }
                    )
                    .then((resp) => {
                        console.log(resp);
                        const lobbyId = resp.data.roomid;
                        localStorage.setItem("lobbyId", lobbyId);
                        localStorage.setItem(
                            "lobbyAddress",
                            "http://" +
                                resp.data.socketIp +
                                ":" +
                                resp.data.socketPort
                        );

                        this.$router.push({
                            name: "Lobby",
                            params: {
                                lobbyName: item.lobbyName,
                                hostName: item.hostName,
                                lobbyDesc: "Description not implemented",
                                isHost: false,
                            },
                        });
                    });
            }
        },
        onRefresh() {
            console.log("Refreshing");
        },
    },
    created() {
        axios
            .get(process.env.VUE_APP_BACKEND_URL + "listrooms", {
                headers: {
                    withCredentials: true,
                },
            })
            .then((resp) => {
                this.lobbies = resp.data;
            });
    },
};
</script>

<style scoped>
.md-table {
    margin-top: 16px;
}
</style>