<template>
    <div class="modal" id="backdrop" tabindex="-1" aria-labelledby="modalTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <form @submit.prevent="submitForm">
                    <div class="row">
                        <div class="form-group">
                            <label for="client_name" class="col-form-label">Nom du client</label>
                            <input type="text" class="form-control" id="client_name" v-model="formData.client_name" required />
                        </div>

                        <div class="form-group">
                            <label for="client_email" class="col-form-label">Email du client</label>
                            <input type="email" class="form-control" id="client_email" v-model="formData.client_email" required />
                        </div>

                        <div class="form-group">
                            <label for="client_activity" class="col-form-label">Activité du client</label>
                            <input type="text" class="form-control" id="client_activity" v-model="formData.client_activity" required />
                        </div>

                        <div class="form-group">
                            <label for="client_tel" class="col-form-label">Téléphone du client</label>
                            <input type="tel" class="form-control" id="client_tel" v-model="formData.client_tel" required />
                        </div>

                        <div class="row">
                            <div class="col-8">
                            <label for="street" class="col-form-label">Rue</label>
                            <input type="text" class="form-control" id="street" v-model="formData.street" required />
                        </div>

                        <div class="col-4">
                            <label for="city" class="col-form-label">Ville</label>
                            <input type="text" class="form-control" id="city" v-model="formData.city" required />
                        </div>
                        </div>

                        <div class="row">
                            <div class="col-6">
                            <label for="postal_code" class="col-form-label">Code postal</label>
                            <input type="text" class="form-control" id="postal_code" v-model="formData.postal_code" required />
                        </div>

                        <div class="col-6">
                            <label for="country" class="col-form-label">Pays</label>
                            <input type="text" class="form-control" id="country" v-model="formData.country" required />
                        </div>
                        </div>

                    </div>

                    <div class="row" style="margin-top: 5%; justify-content:end;">
                        <button @click="close" type="button" class="btn btn-secondary col-3"
                            data-bs-dismiss="modal">Fermer</button>
                        <button type="submit" class="btn btn-primary col-3">Ajouter</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</template>

<script>
import {addClient} from '@/services/adminServices';

export default {
    name: 'ClientForm1',
    data() {
        return {
            modalVisible: false,
            formData: {
                client_name: '',
                client_email: '',
                client_activity: '',
                client_tel: '',
                street: '',
                city: '',
                postal_code: '',
                country: '',
            },
        };
    },
    methods: {
        close() {
            this.$emit('close');
        },
        showModal() {
            this.modalVisible = true; // Afficher la modal
        },
        hideModal() {
            this.modalVisible = false; // Cacher la modal
            this.resetForm();
        },
        resetForm() {
            // Réinitialiser les champs du formulaire
            this.formData.client_name = '';
            this.formData.client_email = '';
            this.formData.client_activity = '';
            this.formData.client_tel = '';
            this.formData.street = '';
            this.formData.city = '';
            this.formData.postal_code = '';
            this.formData.country = '';
        },
        submitForm() {
            addClient(this.formData)
                .then(response => {
                    if (response.status == 201)
                      alert("Le Client a été ajouté avec succès");

                    this.resetForm(); 
                    this.hideModal(); 
                })
                .catch(error => {
                    // Gérez les erreurs ici, par exemple, affichez un message d'erreur à l'utilisateur
                    console.error('Erreur lors de l\'ajout du client:', error);
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


.btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
}
</style>