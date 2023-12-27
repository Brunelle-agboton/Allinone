<template>
      <div class="modal" id="backdrop" tabindex="-1" aria-labelledby="modalTitle" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            <form @submit.prevent="addRow">
            <div class="row">
                <div class="form-group">
                <label for="ident">Code</label>
                <input type="text" class="form-control" id="ident" value="Code" readonly>
            </div>
            <div class="form-group">
                <label for="team_name">Nom de l'équipe</label>
                <input type="text" class="form-control" id="team_name" v-model="newRow.team_name" required>
            </div>
            <div class="form-group">
                <label for="desc">Description </label>
                <input type="text" class="form-control" id="desc" v-model="newRow.team_description" required>
            </div>

            <div class="row" style="margin-top: 5%; justify-content:end;">
                <button type="submit" class="btn btn-primary col-3" style="background-color:#EC7D2C; !important">Enregistrer</button>
                <button  @click="close" type="button"  class="btn btn-secondary col-3" aria-label="close">Fermer</button>
            </div>
            </div>

            </form>
            </div>
        </div>
      </div>
</template>
<script>
import {addTeam} from '@/services/adminServices';


export default {
  name: 'TeamForm1',
  data() {
    return {
      newRow: {
        team_name: '',
        team_description: '',
      },
      dialogVisible: false, // Contrôle l'affichage de la boîte de dialogue
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  methods: {
    close() {
        this.$emit('close');
      },
    openDialog() {
      this.dialogVisible = true;
    },
    closeDialog() {
      this.dialogVisible = false;
      this.resetForm(); 
    },
    resetForm() {
        this.team_name = '';
        this.team_description = '';
    },

    addRow() {
      console.log(this.newRow);
      addTeam(this.newRow)
      .then(response => {
        if (response.status == 200)
          alert("L'equipe a été ajoutée avec succès");
        this.resetForm(); 
        this.closeDialog(); 
    })
    .catch(error => {
        console.error('Erreur lors de l\'ajout de lequipe:', error);
    });
    },
  },
  mounted() {
  },
  created() {

  },
};
</script>
<style src="../../style.css"></style>