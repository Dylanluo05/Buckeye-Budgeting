import { createRouter, createWebHistory } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import App from '../App.vue'
import Transactions from '../Transactions.vue'
import Visuals from '../Visuals.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/navbar',
      name: 'navbar',
      component: Navbar
    },
     {
      path: '/app',
      name: 'app', 
      component: App
    },
    {
      path: '/transactions',
      name: 'tpp', 
      component: Transactions
    },
    {
      path: '/visuals',
      name: 'visuals', 
      component: Visuals
    }
    /*{
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }*/
  ]
})

export default router
