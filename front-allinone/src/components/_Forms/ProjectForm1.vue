<template>
      <div class="modal container-fluid" id="backdrop" tabindex="-1" aria-labelledby="modalTitle" aria-hidden="true">
        <div class="modal-dialog modal-xl">
          <div class="modal-content">
          <form @submit.prevent="submitForm">
            <div class="modal-body">
              <!--<div class="form-group">
                <label for="code" class="col-form-label">Code :</label>
                <input type="text" class="form-control" id="code" v-model="code" required>
              </div>-->
              <div class="form-group">
                <label for="name" class="col-form-label">Nom Projet :</label>
                <input type="text" class="form-control" id="name" v-model="formData.project_name" required>
              </div>
              <div class="form-group">
                <label for="project_description" class="col-form-label">project_description :</label>
                <textarea class="form-control" id="project_description" v-model="formData.project_description" required></textarea>
              </div>
              <div class="form-group">
                <label for="debut" class="col-form-label">Debut :</label>
                <input type="date" class="form-control" id="debut" v-model="formData.debut" required>
              </div>
              
              <div class="form-group">
                <label for="fin" class="col-form-label">Fin estimer :</label>
                <input type="date" class="form-control" id="fin" v-model="formData.expired_at" required>
              </div>
              <div class="form-group">
                <label for="commentaire" class="col-form-label">Commentaires :</label>
                <input type="text" class="form-control" id="commentaire" v-model="formData.commentaire" >
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
import {addProject} from '@/services/adminServices';

  export default {
    data() {
      return {
        modalVisible: false,
        formData: {
        project_name: '',
        project_description: '',
        expired_at: '',
        },
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
        this.resetForm();
      },
      resetForm() {
        this.project_name = '';
        this.project_description = '';
        this.expired_at = '';
      },
      submitForm() {
        addProject(this.formData)
                .then(response => {
                    if (response.status == 201)
                      alert("Le Projet a été ajoutée avec succès");
                    const idp =response.data;
                    console.log(idp);

                    this.resetForm(); 
                    this.hideModal(); 
                })
                .catch(error => {
                    // Gérez les erreurs ici, par exemple, affichez un message d'erreur à l'utilisateur
                    console.error('Erreur lors de l\'ajout du projet:', error);
                });
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
</style>