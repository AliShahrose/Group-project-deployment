import Vue from 'vue'
import VueRouter from 'vue-router'
import GameView from '../views/Game.vue'
import Home from '../views/Home.vue'
import Browse from '../views/Browse.vue'
import Lobby from '../views/Lobby.vue'
import Store from '../views/Store.vue'
import NewGame from '../views/NewGame.vue'
import Login from '../views/Login.vue'

import "@/assets/global.css"

Vue.use(VueRouter)

const routes = [
  {
    path: '/', redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/store',
    name: 'Store',
    component: Store
  },
  {
    path: '/browse',
    name: 'Browse',
    component: Browse
  },
  {
    path: '/lobby',
    name: 'Lobby',
    component: Lobby,
    props: true
  },
  {
    path: '/newGame',
    name: 'NewGame',
    component: NewGame
  },
  {
    path: '/game',
    name: 'Game',
    component: GameView,
    props: true
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
