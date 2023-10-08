<template>
    <div class="client-card card">
        <div class="card-header">
            <img :src="require(`@/assets/${client.logo}`)" class="client-logo col-lg-6" alt="Client Logo" />
            <div class="client-name">{{ client.name }}</div>
        </div>
        <div class="card-body">
            <div class="card-text">{{ client.description }}</div>
        </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      client: {
        type: Object,
        required: true,
      },
    },
    methods: {
      
    },
  };
  </script>
  
  <style scoped>
  /* Client Card */
  .card-header {
    margin: 0px;
    height: 70px;
    decoration: none;
    
  }
  .client-card {
    border: 1px solid #d9d9d9;
    border-right: 3px solid #77933c; /* Bordure verte à droite */
    border-bottom: 3px solid #77933c; /* Bordure verte en bas */
    margin: 10px;
    padding: 0px;
    display: flex;
    flex-direction: column;
    position: relative;
    max-width: 300px;
    background-color: #EAE1D2;
  }
  
  .client-logo {
    width: 80px;
    height: 70px;
    position: absolute;
    top: 0px;
    left: 0px;
  }
  
  .client-name {
    color: #002060;
    font-weight: bold;
  }
  
  </style>
  