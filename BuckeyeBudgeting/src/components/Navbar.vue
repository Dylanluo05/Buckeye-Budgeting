<template>
  <div id = "navbar-container">
    <img src = "/src/assets/Buckeye-Budgeting-logos.png" id = "buckeye-budgeting-logo">
    <a class = "navbar-link">Budgeting Home</a>
    <a class = "navbar-link">Transactions</a>
    <a class = "navbar-link">Visuals</a>
  </div>
</template>

<style scoped>
  html, body {
      font-family: "Montserrat", sans-serif;
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

<script>
  export default {
    name: "Navbar"
  };
</script>
