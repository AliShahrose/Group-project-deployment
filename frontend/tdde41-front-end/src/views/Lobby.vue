<template>
    <md-app>
        <md-app-drawer md-permanent="clipped">
            <NavMenuComp />
        </md-app-drawer>
        <md-app-content>
            <span class="md-display-3">{{
                lobbyName ? lobbyName : "Lobby Name"
            }}</span>
            <div class="md-layout md-gutter">
                <md-card class="lobby-info md-layout-item">
                    <md-card-header>
                        <div class="md-title">
                            {{ "Host: " + (hostName ? hostName : "HostName") }}
                        </div>
                    </md-card-header>

                    <md-card-content>
                        {{
                            lobbyDesc
                                ? lobbyDesc
                                : "This is the lobby description. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non."
                        }}
                    </md-card-content>
                </md-card>

                <md-table class="md-layout-item" v-model="players" md-card>
                    <md-table-toolbar>
                        <h1 class="md-title">Players</h1>
                    </md-table-toolbar>

                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                        <md-table-cell md-label="Name">{{
                            item.name
                        }}</md-table-cell>
                    </md-table-row>
                </md-table>
            </div>
            <md-button
                id="lobby-start-btn"
                class="md-raised md-primary"
                @click="sendStart"
                v-if="isHost"
                >Start</md-button
            >
        </md-app-content>
    </md-app>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";
import { io } from "socket.io-client";
import axios from 'axios';

export default {
    name: "Lobby",
    components: {
        NavMenuComp,
    },
    data() {
        return {
            players: [
                // Should be received via socket
                {
                    id: 1,
                    name: "Player1",
                },
                {
                    id: 2,
                    name: "Player2",
                },
                {
                    id: 3,
                    name: "Player3",
                },
            ],
            socket: null,
        };
    },
    created() {
        const lobbyId = localStorage.getItem("lobbyId");
        const lobbyAddress = localStorage.getItem("lobbyAddress");
        
        console.log("Creating socket")
        this.socket = io(lobbyAddress, {
          withCredentials: true
        });

        this.socket.on("connect", (data) => {
            console.log("Joining room");
            console.log(this.socket.emit("join room", {'roomname':lobbyId}));
        });

        this.socket.on("player joined", (data) => {
            console.log("TODO player joined -> update player list");
        });

        this.socket.on('start', (data) => {
            console.log("Starting game", data);
            this.$router.push({
                name: "Game",
                params: {
                    socket: this.socket,
                    initialQuestion: data,
                },
            });
        });
        
    },
    methods: {
        sendStart() {
            if (this.socket) {
                this.socket.emit("start");
            }
        },
    },
    props: {
        lobbyName: String,
        hostName: String,
        lobbyDesc: String,
        // players: Array,
        isHost: Boolean,
    },
    beforeRouteLeave(to, from, next) {
        if (to.name !== "Game") { 
            if (this.socket) {
                console.log("Socket go bye bye");
                this.socket.disconnect();
            }
        }
        next();
    }
};
</script>

<style scoped>
.md-gutter {
    margin-top: 16px;
}

.md-table {
    max-width: 30vw;
}

.lobby-info {
    text-align: left;
}

#lobby-start-btn {
    float: right;
}
</style>