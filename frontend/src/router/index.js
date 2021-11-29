import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/ransele',
    name: 'Ransele',
    component: () => import('../views/Ransele.vue')
  },
  {
    path: '/comp',
    name: 'Comp',
    component: () => import('../views/Comp.vue')
  },
  {
    path: '/selected',
    name: 'Selected',
    component: () => import('../views/Selected.vue')
  },
  {
    path: '/result',
    name: 'Result',
    component: () => import('../views/Result.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
