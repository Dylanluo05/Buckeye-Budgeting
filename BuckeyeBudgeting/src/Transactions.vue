<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<template>
  <Navbar />
  <div id="home-background-1">
    <div class="home-background-1-image"></div>
    <div class="home-background-1-overlay"></div>
    <div class="home-background-1-content">
      <h1 id="home-page-title">Welcome, Buckeye!</h1>
    </div>
  </div>
  <div id="home-background-2">
    <div class="account-row">
      <div id="account-balance-section">
        <h2 class="section-title">Account Balance</h2>
        <p class="section-value">$100,000</p>
      </div>
      <div id="monthly-budget-section">
        <h2 class="section-title">Monthly Allowance</h2>
        <p class="section-value">$2,000</p>
      </div>
    </div>
    <div id="budget-envelopes-section">
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <div class="budget-envelope">
        <div class="envelope-label">Groceries</div>
        <div class="envelope-amount-left">
          Amount Left: <bold style="margin-left: 3px">$200</bold>
        </div>
        <div class="envelope-monthly-allowance">
          Monthly Allowance: <bold style="margin-left: 3px">$300</bold>
        </div>
        <div class="envelope-edit-container">
          <button class="edit-button">&#9998;</button>
          <button class="delete-button">&#128465;</button>
        </div>
      </div>
      <button id="add-budget-envelope">+</button>
    </div>
  </div>

  <RouterView />
</template>

<style scoped>
#home-background-1 {
  position: relative;
  background-repeat: no-repeat;
}

.home-background-1-image,
.home-background-1-overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.home-background-1-image {
  height: 500px;
  width: 100%;
  background-image: url('https://images.pexels.com/photos/53621/calculator-calculation-insurance-finance-53621.jpeg?auto=compress&cs=tinysrgb&w=1500');
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
  background-position: center center;
  z-index: 1;
}

.home-background-1-overlay {
  height: 500px;
  width: 100%;
  background-color: #a8adb4;
  opacity: 0.7;
  z-index: 2;
}

.home-background-1-content {
  height: 500px;
  width: 100%;
  position: relative;
  z-index: 3;
}

#home-page-title {
  margin: 0;
  color: white;
  font-size: 50px;
  text-align: center;
  position: relative;
  top: 200px;
}

#home-background-2 {
  height: 1200px;
  width: 100%;
  background-color: whitesmoke;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.account-row {
  height: 350px;
  width: 85%;
  background-color: transparent;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: transparent;
}

#account-balance-section,
#monthly-budget-section {
  height: 70%;
  width: 40%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: #e8e8e8;
  border-radius: 10px;
  margin-left: 50px;
  margin-right: 50px;
}

.section-title {
  font-size: 35px;
  color: #c10435;
  margin-left: 25px;
}

.section-value {
  font-size: 25px;
  color: black;
  margin-left: 25px;
}

#budget-envelopes-section {
  width: 90%;
  display: flex;
  flex-direction: row;
  align-items: center;
  background-color: #e8e8e8;
  border-radius: 20px;
  flex-wrap: wrap;
  padding-bottom: 30px;
  overflow: auto;
}

.budget-envelope {
  height: 300px;
  width: 15%;
  background-color: whitesmoke;
  overflow: hidden;
  border-radius: 15px;
  margin-left: 55px;
  margin-top: 30px;
}

#add-budget-envelope {
  height: 300px;
  width: 15%;
  background-color: #de3163;
  border-radius: 15px;
  margin-left: 55px;
  margin-top: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  cursor: pointer;
  font-size: 50px;
  color: white;
}

.envelope-label {
  height: 17%;
  width: 100%;
  background-color: #c10435;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 20px;
}

.envelope-amount-left,
.envelope-monthly-allowance {
  height: 15%;
  width: 100%;
  background-color: whitesmoke;
  font-size: 16px;
  color: darkblue;
  display: flex;
  align-items: center;
  padding-left: 15px;
}

.envelope-edit-container {
  height: 25%;
  width: 100%;
  background-color: whitesmoke;
  display: flex;
  justify-content: center;
  align-items: center;
}

.edit-button {
  height: 30px;
  width: 30px;
  border-radius: 10px;
  background-color: #3454d1;
  color: white;
  border: none;
  margin-right: 20px;
  cursor: pointer;
  transition-duration: 0.5s;
}

.edit-button:hover {
  background-color: dodgerblue;
}

.delete-button {
  height: 30px;
  width: 30px;
  border-radius: 10px;
  background-color: crimson;
  color: white;
  border: none;
  margin-left: 20px;
  cursor: pointer;
  transition-duration: 0.5s;
}

.delete-button:hover {
  background-color: orangered;
}
</style>
