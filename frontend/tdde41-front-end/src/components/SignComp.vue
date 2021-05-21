<template>
    <form novalidate class="md-layout" @submit.prevent="validateInput">
        <md-card class="md-layout-item md-size-100 md-small-size-100">
            <md-card-header>
                <div class="md-title">{{'Sign ' + (signIn ? 'in' : 'up')}}</div>
            </md-card-header>

            <md-card-content>
                <InputComp
                    :id="'user-name-' + (signIn ? 'in' : 'up')"
                    name="user name"
                    title="User Name"
                    dataName="userName"
                    :v="$v"
                    :validationClass="getValidationClass('userName')"
                    :maxLen="20"
                    :creating="creating"
                    @valueChanged="updateUserName"
                />

                <div class="md-layout md-gutter">
                    <InputComp
                        :id="'password-' + (signIn ? 'in' : 'up')"
                        name="password"
                        title="Password"
                        dataName="password"
                        :v="$v"
                        :validationClass="getValidationClass('password')"
                        type="password"
                        :maxLen="30"
                        :creating="creating"
                        @valueChanged="updatePassword"
                    />

                    <InputComp
                        v-if="!signIn"
                        id="password-conf"
                        name="password confirmation must match and"
                        title="Confirm password"
                        dataName="passwordConf"
                        :v="$v"
                        :validationClass="getValidationClass('passwordConf')"
                        type="password"
                        :maxLen="30"
                        :creating="creating"
                        @valueChanged="updatePasswordConf"
                    />
                </div>
            </md-card-content>

            <md-progress-bar md-mode="indeterminate" v-if="creating" />

            <md-card-actions>
                <md-button type="submit" class="md-primary" :disabled="creating"
                    >{{'Sign ' + (signIn ? 'in' : 'up')}}</md-button
                >
            </md-card-actions>
        </md-card>
    </form>
</template>

<script>
import axios from 'axios';
import { validationMixin } from "vuelidate";
import { required, minLength, maxLength, sameAs, alphaNum } from "vuelidate/lib/validators";
import InputComp from "../components/InputComp";

export default {
    name: "SignComp",
    mixins: [validationMixin],
    components: { InputComp },
    props: {
        signIn: Boolean
    },
    data: () => ({
        form: {
            userName: null,
            password: null,
            passwordConf: null,
        },
        creating: false,
    }),
    validations: {
        form: {
            userName: {
                required,
                alphaNum,
                minLength: minLength(3),
                maxLength: maxLength(20),
            },
            password: {
                required,
                alphaNum,
                minLength: minLength(7),
                maxLength: maxLength(30),
                checkStrength(password) {
                    return (
                        /[a-zA-Z0-9]/.test(password)
                    )
                }
            },
            passwordConf: {
                sameAs: sameAs('password')
            },
        },
    },
    methods: {
        
        updateUserName(name) {
            this.form.userName = name;
        },

        updatePassword(pass) {
            this.form.password = pass;
            if (this.signIn) {
                this.form.passwordConf = pass;
            }
        },

        updatePasswordConf(pass) {
            this.form.passwordConf = pass;
        },

        getValidationClass(fieldName) {
            const field = this.$v.form[fieldName];

            if (field) {
                return {
                    "md-invalid": field.$invalid && field.$dirty,
                };
            }
        },
        login() {
            console.log("This login");
            this.creating = true;

            let url = process.env.VUE_APP_BACKEND_URL;

            if (this.signIn) {
                url += "login"
            } else {
                url += "register"
            }

            // TODO encrypt password before sending?
            axios.post(url, {
                name: this.form.userName,
                password: this.form.password
            },{
                withCredentials: true,
            }).then((resp) => {
                this.creating = false;
                if (resp.status == 200) {
                    this.$emit("login");
                }
            }).catch((error) => {
                this.creating = false;
                console.log("Error");
            });
            
        },
        validateInput() {
            this.$v.$touch();
            console.log(this.$v);

            if (!this.$v.$invalid) {
                this.login();
            }
        },
    }
};
</script>

<style scoped>
</style>
