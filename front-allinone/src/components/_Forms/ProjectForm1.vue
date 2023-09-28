<template>
      <div class="modal container-fluid" id="backdrop" tabindex="-1" aria-labelledby="modalTitle" aria-hidden="true">
        <div class="modal-dialog modal-xl">
          <div class="modal-content">
          <form @submit.prevent="submitForm">
            <div class="modal-body">
              <div class="form-group">
                <label for="code" class="col-form-label">Code :</label>
                <input type="text" class="form-control" id="code" v-model="code" required>
              </div>
              <div class="form-group">
                <label for="name" class="col-form-label">Nom Projet :</label>
                <input type="text" class="form-control" id="name" v-model="name" required>
              </div>
              <div class="form-group">
                <label for="description" class="col-form-label">Description :</label>
                <textarea class="form-control" id="description" v-model="description" required></textarea>
              </div>
              <div class="form-group">
                <label for="debut" class="col-form-label">Debut :</label>
                <input type="text" class="form-control" id="debut" v-model="debut" required>
              </div>
              <div class="form-group">
                <label for="nom" class="col-form-label">Nom :</label>
                <input type="text" class="form-control" id="nom" v-model="nom" required>
              </div>
              <div class="form-group">
                <label for="fin" class="col-form-label">Fin estimer :</label>
                <input type="text" class="form-control" id="fin" v-model="fin" required>
              </div>
              <div class="form-group">
                <label for="commentaire" class="col-form-label">Commentaires :</label>
                <input type="text" class="form-control" id="commentaire" v-model="commentaire" >
              </div>
             
            </div>
          
            <div class="modal-footer">
              <button @click="close" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Fermer</button>
              <button type="submit" class="btn btn-primary">Ajouter</button>
            </div>
      </form>
        </div>
        </div>
        
      </div>
      
  </template>
  
  <script>
  export default {
    data() {
      return {
        modalVisible: false,
        nom: '',
        description: '',
      };
    },
    methods: {
      close() {
        this.$emit('close');
      },
      showModal() {
        console.log(this.modalVisible);
        this.modalVisible = true; // Afficher la modal
      },
      hideModal() {
        this.modalVisible = false; // Cacher la modal
        // Réinitialisez les champs du formulaire si nécessaire
        this.nom = '';
        this.description = '';
      },
      submitForm() {
        // Gérez la soumission du formulaire ici
        // Vous pouvez envoyer les données au backend ou effectuer d'autres opérations nécessaires
        // Une fois terminé, vous pouvez cacher la modal
        this.hideModal();
      },
    },
  };
</script>
<style>
.modal {
    width: 100% !important;
    box-shadow: 2px 2px 20px 1px;
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
  }

  .modal-body {

    padding: 20px 10px;
  }


  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }
</style>