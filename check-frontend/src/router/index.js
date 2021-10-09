import Vue from 'vue'
import VueRouter from 'vue-router'
import checkPage from '../components/checkPage.vue'

Vue.use(VueRouter)

const routes = [
{
    path: '/',
    component: checkPage
}
]

const router = new VueRouter({
    routes
})

export default router
