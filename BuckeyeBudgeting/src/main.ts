import axios from 'axios';
import { VueElement, createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
App.prototype.$http = axios;
const app = createApp(App)


app.use(createPinia())
app.use(router)

app.mount('#app')
