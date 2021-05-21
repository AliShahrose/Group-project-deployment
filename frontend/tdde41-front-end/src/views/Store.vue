<template>
    <md-app>
        <md-app-drawer md-permanent="clipped">
            <NavMenuComp />
        </md-app-drawer>
        <md-app-content>
            <div class="top-bar">
                <span class="md-headline">
                    Account balance:
                </span>
                <md-icon class="money-icon">attach_money</md-icon>
                <span class="md-headline money">
                    {{ playerMoney }}
                </span>
            </div>
            <div class="md-layout">
                <md-card
                    class="buy-item"
                    md-with-hover
                    v-for="item in items"
                    :key="`item-${item.id}`"
                >
                    <md-card-header>
                        <div class="md-title">{{ item.title }}</div>
                    </md-card-header>

                    <md-card-content>
                        {{ item.desc }}
                    </md-card-content>

                    <div style="margin-left: 20px">
                        <span class="md-headline">{{ `$${item.price}` }}</span>
                    </div>

                    <md-card-actions>
                        <md-button v-on:click.native="buyItem(item.id, item.price)">Buy</md-button>
                    </md-card-actions>
                </md-card>
            </div>
        </md-app-content>
    </md-app>
</template>

<script>
import NavMenuComp from "@/components/NavMenuComp.vue";
import axios from "axios";

export default {
    name: "Store",
    components: {
        NavMenuComp,
    },
    methods: {
        buyItem(id, price) {
            if (this.playerMoney < price) {
                console.log("No item for you");
                return;
            }

            axios
                .post(process.env.VUE_APP_BACKEND_URL + "purchase", {itemnr:id},{
                    withCredentials: true,
                })
                .then((resp) => {
                    if (resp.status == 200) { // Purchase went trough
                        this.playerMoney = resp.data.money;
                    } else {
                        console.log("Denied by backend");
                    }
                });
        },
    },
    data() {
        return {
            items: [],
            playerMoney: "-"
        };
    },
    created() {
        // Request shop items
        axios
            .get(process.env.VUE_APP_BACKEND_URL + "listitems", {
                withCredentials: true,
            })
            .then((resp) => {
                this.items = resp.data;
            });

        // Check money balance
        axios
            .get(process.env.VUE_APP_BACKEND_URL + "userinfo/userid", {
                withCredentials: true,
            })
            .then((resp) => {
                console.log(resp);
                this.playerMoney = resp.data.money;
            });
    },
};
</script>

<style>
.buy-item {
    max-width: 300px;
    min-width: 200px;
    text-align: left;
    margin-bottom: 30px;
}

.top-bar {
    margin-bottom: 50px;
    text-align: left;
    border-bottom: 2px solid black;
}

.money {
    margin-left: -10px;
}

.money-icon {
    position: relative;
    bottom: 4px;
}

</style>