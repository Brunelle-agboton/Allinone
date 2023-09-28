<template>
    <div class="custom-next-arrow" @click="goToNextSlide">
      <!-- Personnalisez votre flèche "suivant" ici -->
      <i class="fas fa-chevron-right"></i>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToNextSlide() {
        this.$emit("next");
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles personnalisés pour la flèche "suivant" */
  .custom-next-arrow {
    color: #002060;

  }
  </style>
  