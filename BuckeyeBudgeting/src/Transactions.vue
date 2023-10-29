<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="transactions-background-1">
    <h1>Account Balance</h1>
    <div style="width: 100%; display: flex; flex-direction: row; justify-content: center">
      <div id="account-balance-card-label" style="margin: 0;">Account Cash</div>
      <div id="account-balance-dining-dollars-label" style="margin-left: 50px;">Dining Dollars</div>
      <div id="account-balance-buck-id-label">BuckID cash</div>
      
    </div>
    <div style="width: 100%; display: flex; flex-direction: row; justify-content: center">
      <div id="account-balance-card">$500</div>
      <div id="account-balance-dining-dollars">$700</div>
      <div id="account-balance-buck-id">$600</div>
    </div>
    <h1 style="margin-top: 80px">Make a Transaction</h1>
    <form id="make-transaction-form">
      <div
        style="
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
        "
      >
        <label class="transaction-label">Envelope Type:</label>
        <select id="envelope-type-input">
          <option>Groceries</option>
          <option>Clothing</option>
          <option>Food</option>
        </select>
      </div>
      <div
        style="
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
          margin-top: 70px;
        "
      >
        <label class="transaction-label">Transaction Type:</label>
        <select id="transaction-type-input">
          <option>Withdrawel</option>
          <option>Deposit</option>
        </select>
      </div>
      <div
        style="
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
          margin-top: 70px;
        "
      >
        <label class="transaction-label">Card Type:</label>
        <select id="card-type-input">
          <option>Debit Card</option>
          <option>Dining Dollars Card</option>
          <option>Buck ID Card</option>
        </select>
      </div>
      <div
        style="
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
          margin-top: 70px;
        "
      >
        <label class="transaction-label">Dollar Amount:</label>
        <input type="text" id="dollar-amount-input" placeholder="Transaction Dollar Amount" />
      </div>
      <div
        style="
          width: 100%;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
          margin-top: 70px;
        "
      >
        <label class="transaction-label">Transaction Description:</label>
        <textarea id="description-input" placeholder="Transaction Description"></textarea>
      </div>
      <input type="submit" id="transaction-submit-button" />
    </form>
  </div>
  <div id="transactions-background-2">
    <h1 style="color: white">Transaction History</h1>
    <div class="transaction-history-container">
      <p class="transaction-history-date-time">10/28/2023 - 8:00 PM</p>
      <p class="transaction-history-summary">Clothing - Withdrawel - Debit Card - $70.00</p>
    </div>
    <div class="transaction-history-container">
      <p class="transaction-history-date-time">10/28/2023 - 8:00 PM</p>
      <p class="transaction-history-summary">Clothing - Withdrawel - Debit Card - $70.00</p>
    </div>
    <div class="transaction-history-container">
      <p class="transaction-history-date-time">10/28/2023 - 8:00 PM</p>
      <p class="transaction-history-summary">Clothing - Withdrawel - Debit Card - $70.00</p>
    </div>
    <div class="transaction-history-container">
      <p class="transaction-history-date-time">10/28/2023 - 8:00 PM</p>
      <p class="transaction-history-summary">Clothing - Withdrawel - Debit Card - $70.00</p>
    </div>
    <div class="transaction-history-container">
      <p class="transaction-history-date-time">10/28/2023 - 8:00 PM</p>
      <p class="transaction-history-summary">Clothing - Withdrawel - Debit Card - $70.00</p>
    </div>
  </div>
</template>

<style scoped>
#transactions-background-1 {
  width: 100%;
  background-color: whitesmoke;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-bottom: 50px;
}

h1 {
  font-size: 50px;
}

#account-balance-card {
  height: 100px;
  width: 250px;
  border: 3px solid #c10435;
  border-radius: 20px;
  background-color: #e0babc;
  margin-right: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #c10435;
  font-weight: bold;
  font-size: 30px;
}
#account-balance-card-label {
  height: 40px;
  width: 250px;
  border: 3px solid #c10435;
  border-radius: 20px;
  background-color: #e0babc;
  margin-right: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #c10435;
  font-weight: bold;
  font-size: 30px;
}

#account-balance-dining-dollars {
  height: 100px;
  width: 250px;
  border: 3px solid #01b4bc;
  border-radius: 20px;
  background-color: #badae0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #01b4bc;
  font-weight: bold;
  font-size: 30px;
}
#account-balance-dining-dollars-label {
  height: 40px;
  width: 250px;
  border: 3px solid #01b4bc;
  border-radius: 20px;
  background-color: #badae0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #01b4bc;
  font-weight: bold;
  font-size: 30px;
}

#account-balance-buck-id {
  height: 100px;
  width: 250px;
  border: 3px solid #5fa55a;
  border-radius: 20px;
  background-color: #bdd9c8;
  margin-left: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #5fa55a;
  font-weight: bold;
  font-size: 30px;
}
#account-balance-buck-id-label
{
  height: 40px;
  width: 250px;
  border: 3px solid #5fa55a;
  border-radius: 20px;
  background-color: #bdd9c8;
  margin-left: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #5fa55a;
  font-weight: bold;
  font-size: 30px;
}
#make-transaction-form {
  height: 700px;
  width: 50%;
  background-color: crimson;
  border-radius: 20px;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.transaction-label {
  font-size: 20px;
  color: white;
}

#envelope-type-input,
#transaction-type-input,
#card-type-input,
#dollar-amount-input {
  height: 40px;
  width: 200px;
  background-color: white;
  border: none;
  border-radius: 5px;
  margin-left: 30px;
  font-size: 15px;
  padding-left: 10px;
}

#description-input {
  height: 80px;
  width: 225px;
  background-color: white;
  border: none;
  border-radius: 5px;
  margin-left: 30px;
  font-size: 15px;
  padding-left: 7px;
}

#transaction-submit-button {
  height: 45px;
  width: 225px;
  border: 3px solid dodgerblue;
  color: dodgerblue;
  background-color: white;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition-duration: 0.7s;
  margin-top: 30px;
}

#transaction-submit-button:hover {
  background-color: dodgerblue;
  color: white;
}

#transactions-background-2 {
  width: 100%;
  background-color: lightgray;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-bottom: 50px;
}

.transaction-history-container {
  height: 175px;
  width: 70%;
  border-radius: 20px;
  background-color: #c10435;
  margin-top: 30px;
  color: white;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.transaction-history-date-time {
  font-size: 25px;
  color: white;
  font-weight: bold;
}

.transaction-history-summary {
  font-size: 25px;
  color: white;
  margin-left: 40px;
}
</style>
