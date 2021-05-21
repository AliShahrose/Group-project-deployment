<template>
    <div class="game-comp">
        <h1>{{ questionStruct.question }}</h1>

        <div class="image-container">
            <img class="question-image" src="images/default.png" />
        </div>

        <div class="md-layout md-alignment-center">
            <md-card
                v-for="(ans, index) in questionStruct.answers"
                :key="`ans-${index}`"
                class="md-layout-item md-medium-size-33 md-small-size-50 md-xsmall-size-100"
                v-bind:class="{
                    'answer-lock': answerLock && (selectedAns != index) && (correctAns != index),
                    'md-primary': (selectedAns == index) && (correctAns == -1),
                    'md-accent': (selectedAns == index) && (correctAns != -1 && correctAns != index),
                    'correct-ans' : correctAns == index,
                }"
            >
                <div v-on:click="madeGuess(index)">
                    <md-card-header>
                        <div class="no-select md-title">{{ ans }}</div>
                    </md-card-header>
                </div>
            </md-card>
        </div>
    </div>
</template>

<script>
export default {
    name: "GameComp",
    data() {
        return {
            answerLock: false,
            selectedAns: -1,
        };
    },
    props: {
        questionStruct: {
            question: String,
            answers: Array,
        },
        correctAns: Number
    },
    watch: {
        questionStruct: function(newVal) {
            this.selectedAns = -1;
            this.answerLock = false;
        }
    },
    methods: {
        madeGuess: function (buttonId) {
            if (!this.answerLock) {
                this.selectedAns = buttonId;
                this.answerLock = true;
                this.$emit("madeGuess", buttonId);
            }
        },
    },
    mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.answer-container {
    margin-right: 20px;
}

.md-layout-item {
    height: 100px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-left: 10px;
    margin-right: 10px;
}

.question-image {
    width: auto;
    height: 100%;
    max-height: 50vh;
    margin: auto;
}

.image-container {
    margin: 40px;
}

.answer-lock {
    background: grey !important;
}

.correct-ans {
    background: green !important;
}

.no-select {
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
</style>
