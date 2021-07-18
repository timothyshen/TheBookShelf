import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
// import store from '../store/index'

const routes = createRouter({
  history: createWebHistory(),
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/registration.vue')
    },
    {
      path: '/payment/success',
      name: 'Payment_success',
      component: () => import('../views/Plan_success.vue'),
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/plan/',
      name: 'Payment',
      component: () => import('../views/plan.vue'),
      meta: {
        requireLogin: true
      }
    }
  ]
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
