<template>
    <div class="custom-prev-arrow" @click="goToPrevSlide">
      <!-- Personnalisez votre flèche "précédent" ici -->
      <i class="fas fa-chevron-left"></i>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goToPrevSlide() {
        this.$emit("prev");
      },
    },
  };
  </script>
  
  <style scoped>
  /* Styles personnalisés pour la flèche "précédent" */
  .custom-prev-arrow {
    color: #002060;
  }
  </style>
  