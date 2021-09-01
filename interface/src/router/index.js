import {createRouter, createWebHistory} from 'vue-router'


// import store from '../store/index'

const routes = createRouter({
    history: createWebHistory(),
    routes: []
})

// routes.beforeEach((to, from, next) => {
//     if (to.meta.requireLogin && !store.state.isAuthenticated) {
//         console.log('login please')
//         next('/login')
//     } else {
//         next()
//     }
// })
export default routes;
