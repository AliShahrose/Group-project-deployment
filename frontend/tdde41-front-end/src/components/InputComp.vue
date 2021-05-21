<template>
    <div class="md-layout-item md-small-size-100">
        <md-field :class="validationClass">
            <label :for="id">{{title}}</label>
            <md-input
                :type="type"
                :name="id"
                :id="id"
                v-model="value"
                :disabled="creating"
                :md-counter="type=='number' ? 'none' : maxLen"
            />
            <span class="md-error" v-if="!v.form[dataName].required"
                >{{`The ${name} is required`}}</span
            >
            <span class="md-error" v-else-if="!v.form[dataName].minlength"
                >{{`Invalid ${name}`}}</span
            >
        </md-field>
    </div>
</template>

<script>
export default {
    name: "InputComp",

    data() {
        return {
            value: null
        }
    },

    watch: {
        value: function(val) {
            this.$emit("valueChanged", val);
        }
    },

    props: {
        id: String,
        name: String,
        title: String,
        dataName: String,
        v: Object,
        validationClass: Object,
        type: String,
        maxLen: Number,
        creating: Boolean,
        initValue: String,
    },

    created() {
        this.value = this.initValue ? this.initValue : "";
    }
};
</script>

<style scoped>
</style>