<template>
    <md-list>
        <md-list-item to="/home">
            <md-icon>home</md-icon>
            <span class="md-list-item-text">Home</span>
        </md-list-item>

        <md-list-item to="/newGame">
            <md-icon>quiz</md-icon>
            <span class="md-list-item-text">New Quiz</span>
        </md-list-item>

        <md-list-item to="/browse">
            <md-icon>manage_search</md-icon>
            <span class="md-list-item-text">Browse</span>
        </md-list-item>

        <md-list-item to="/store">
            <md-icon>local_grocery_store</md-icon>
            <span class="md-list-item-text">Store</span>
        </md-list-item>

        <md-list-item to="/about">
            <md-icon>error</md-icon>
            <span class="md-list-item-text">About</span>
        </md-list-item>
    </md-list>
</template>

<script>
export default {
    name: "NavMenuComp",
};
</script>

<style>
.md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
}
</style>