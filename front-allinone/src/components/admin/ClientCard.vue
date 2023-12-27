<template>
    <div class="client-card card">
        <div class="card-header">
            <img :src="require(`@/assets/${client.logo}`)" class="client-logo col-lg-6" alt="Client Logo" />
            <div class="client-name">{{ client.name }}</div>
        </div>
        <div class="card-body">
            <div class="card-text">{{ client.activity }}</div>
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
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
    methods: {
    },
  };
  </script>
  
  <style scoped src="../../style.css"> </style>  