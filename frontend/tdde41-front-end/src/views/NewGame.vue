<template>
    <md-app>
        <md-app-drawer md-permanent="clipped">
            <NavMenuComp />
        </md-app-drawer>
        <md-app-content style="text-align: center">
            <span class="md-display-3"> New Quiz </span>
            <form novalidate class="md-layout" @submit.prevent="validateInput">
                <md-card class="md-layout-item md-size-50 md-small-size-100">
                    <md-card-header>
                        <div class="md-title">Create new quiz lobby</div>
                    </md-card-header>

                    <md-card-content>
                        <InputComp
                            id="lobby-name"
                            name="lobby name"
                            title="Lobby Name"
                            dataName="lobbyName"
                            :v="$v"
                            :validationClass="getValidationClass('lobbyName')"
                            :maxLen="30"
                            :creating="creating"
                            @valueChanged="updateLobbyName"
                        />

                        <div class="md-layout-item md-small-size-100">
                            <md-field :class="getValidationClass('lobbyDesc')">
                                <label for="lobby-desc"
                                    >Lobby description</label
                                >
                                <md-textarea
                                    name="lobby-desc"
                                    id="lobby-desc"
                                    v-model="form.lobbyDesc"
                                    :disabled="creating"
                                    md-counter="200"
                                />
                            </md-field>
                        </div>

                        <div class="md-layout-item md-small-size-100">
                            <md-field :class="getValidationClass('nrPlayers')">
                                <label for="nr-players"
                                    >Nr Players (max 30)</label
                                >
                                <md-input
                                    type="number"
                                    id="nr-players"
                                    name="nr-players"
                                    v-model="form.nrPlayers"
                                    :disabled="creating"
                                />
                                <span
                                    class="md-error"
                                    v-if="!$v.form.nrPlayers.required"
                                    >The number of players must be a
                                    number</span
                                >
                                <span
                                    class="md-error"
                                    v-else-if="!$v.form.nrPlayers.maxlength"
                                    >Invalid number of players</span
                                >
                            </md-field>
                        </div>
                    </md-card-content>

                    <md-card-actions>
                        <md-button
                            type="submit"
                            class="md-primary"
                            :disabled="creating"
                            >Sign Up</md-button
                        >
                    </md-card-actions>
                </md-card>
            </form>
        </md-app-content>
    </md-app>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";
import InputComp from "../components/InputComp";
import { validationMixin } from "vuelidate";
import {
    required,
    minLength,
    minValue,
    maxValue,
} from "vuelidate/lib/validators";

import axios from 'axios';

export default {
    name: "NewGame",
    components: {
        NavMenuComp,
        InputComp,
    },
    mixins: [validationMixin],
    data: () => ({
        form: {
            lobbyName: null,
            nrPlayers: 5,
            lobbyDesc: null,
        },
        creating: false,
    }),
    validations: {
        form: {
            lobbyName: {
                required,
                minLength: minLength(3),
            },
            lobbyDesc: {},
            nrPlayers: {
                required,
                minValue: minValue(1),
                maxValue: maxValue(30),
            },
        },
    },
    methods: {
        updateLobbyName(value) {
            this.form.lobbyName = value;
        },
        getValidationClass(fieldName) {
            const field = this.$v.form[fieldName];

            if (field) {
                return {
                    "md-invalid": field.$invalid && field.$dirty,
                };
            }
        },
        createGame() {
            this.creating = true;

            // TODO Call API
            axios
                .post(
                    process.env.VUE_APP_BACKEND_URL + "createroom",
                    {
                        roomname: this.form.lobbyName,
                        roomdesc: this.form.lobbyDesc,
                        maxplayers: this.form.nrPlayers,
                        owner: "TODO",
                    }, {
                        withCredentials: true,
                    }
                )
                .then((resp) => {
                    console.log(resp);
                    const lobbyId = resp.data.roomid;
                    localStorage.setItem("lobbyId", lobbyId);
                    localStorage.setItem("lobbyAddress", "http://" + resp.data.socketIp + ":" + resp.data.socketPort);

                    this.$router.push({
                        name: "Lobby",
                        params: {
                            lobbyName: this.form.lobbyName,
                            lobbyDesc: this.form.lobbyDesc,
                            hostName: "You are the host",
                            isHost: true,
                        },
                    });
                });
        },
        validateInput() {
            this.$v.$touch();

            if (!this.$v.$invalid) {
                this.createGame();
            }
        },
    },
};
</script>

<style scoped>
.md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
}

form {
    display: block ruby;
    margin-top: 20px;
}
</style>