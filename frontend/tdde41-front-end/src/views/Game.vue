<template>
    <div class="game-view">

        <div class="md-layout md-gutter">
            <div class="md-layout-item md-size-15 side-menu">
                <md-toolbar class="md-primary" :md-elevation="1">
                  <span class="md-title md-display-1">{{"Round " + (round + 1)}}</span>
                </md-toolbar>
                <md-list class="md-double-line">


                    <md-list-item v-for="(player, index) in players" :key="`player-${index}`">
                        <md-avatar class="md-avatar-icon md-primary">{{player.name[0]}}</md-avatar>

                        <div class="md-list-item-text">
                            <span>{{player.name}}</span>
                            <span>{{player.score}}</span>
                        </div>
                    </md-list-item>

                </md-list>
            </div>


            <div class="md-layout-item">
              <GameComp :questionStruct="questionStruct" :correctAns="correctAns" @madeGuess="onMadeGuess" />
            </div>
        </div>
    </div>
</template>

<script>
// ヽ(=´▽`=)ﾉ　Stordåd (๑•̀ㅂ•́)و✧ 

// @ is an alias to /src
import GameComp from "@/components/GameComp.vue";

export default {
    name: "GameView",
    components: {
        GameComp,
    },
    props: {
      socket: Object,
      initialQuestion: Object
    },
    data() {
      return {
        questionStruct: {
          question: "",
          answers: [],
        },
        players: [
          {
            name: "Bengan",
            score: 1337
          },
          {
            name: "GenericPlayer123",
            score: 123
          }
        ],
        round: 0,
        correctAns: -1,
      }
    },
    created() {
      this.questionStruct = this.initialQuestion;

      this.socket.on('game ended', (data) => {
        this.$router.push({name:"Home"});
      });

      this.socket.on('next question', (data) => {

        this.correctAns = data.answer;
        console.log("Next question received");
        
        const _this = this;
        setTimeout(function() {
          // Display the new question after 1s
          _this.correctAns = -1;
          _this.questionStruct = data.question;
          _this.round += 1;
        }, 1000);
      });
    },
    methods: {

      onMadeGuess(buttonId) {
        console.log("User guessed on answer", buttonId);
        // Send ping to backend that we are done
        this.socket.emit("answer", {"answer": buttonId});
      }
    },
    beforeRouteLeave(to, from, next) {
        if (this.socket) {
            console.log("Socket go bye bye");
            this.socket.disconnect();
        }
        next();
    }
};
</script>

<style scoped>

.side-menu {
  min-width: 350px !important;
}

.game-view {
  margin: 0 40px;
  margin-top: 40px;
}

</style>
