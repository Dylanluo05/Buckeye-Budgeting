<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Home from "./Home.vue"
import Transactions from "./Transactions.vue"
import Visuals from "./Visuals.vue"

import { ref } from "vue"
var homeComponentEnabled = ref(true)
var transactionsComponentEnabled = ref(false)
var visualsComponentEnabled = ref(false)

function toggleComponent(id) {
  if (id == 1) {
    homeComponentEnabled.value = true;
    transactionsComponentEnabled.value = false;
    visualsComponentEnabled.value = false;
  } else if (id == 2) {
    homeComponentEnabled.value = false;
    transactionsComponentEnabled.value = true;
    visualsComponentEnabled.value = false;
  } else if (id == 3) {
    homeComponentEnabled.value = false;
    transactionsComponentEnabled.value = false;
    visualsComponentEnabled.value = true;
  }
}
</script>

<template>
   <div id="navbar-container">
    <img src="/src/assets/Buckeye-Budgeting-logos.png" id="buckeye-budgeting-logo" />
    <a class="navbar-link" @click = "toggleComponent(1)">Budgeting Home</a>
    <a class="navbar-link" @click = "toggleComponent(2)">Transactions</a>
    <a class="navbar-link" @click = "toggleComponent(3)">Visuals</a>
  </div>
  <Home v-if="homeComponentEnabled" />
  <Transactions v-if="transactionsComponentEnabled" />
  <Visuals v-if="visualsComponentEnabled" />
</template>

<style scoped>
  html,
body {
  font-family: 'Montserrat', sans-serif;
  overflow: hidden;
}

#navbar-container {
  height: 80px;
  width: 100%;
  background-color: #c10435;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  color: white;
}

#buckeye-budgeting-logo {
  height: 100px;
  width: 100px;
}
.navbar-link {
  font-size: 20px;
  color: white;
  margin-left: 35px;
  cursor: pointer;
  text-decoration: none;
}
</style>
