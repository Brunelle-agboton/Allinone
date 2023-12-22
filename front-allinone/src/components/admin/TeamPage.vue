<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
    <div class="table-row">
      <div class="table-cell">
      <button type="button" class="btn-icon" @click="openDialog" data-test="mod"><i class="bi bi-plus"></i>Ajouter</button>
      <div class="modal modal-sm" :class="{ 'is-active': dialogVisible }">
        <div class="modal-background"></div>
        <div class="modal-content">
          <form @submit.prevent="addRow">
          <div class="form-group">
            <label for="ident">Code</label>
            <input type="text" class="form-control" id="ident" v-model="newRow.idteam" required>
          </div>
          <div class="form-group">
            <label for="team_name">Nom de l'équipe</label>
            <input type="text" class="form-control" id="team_name" v-model="newRow.team_name" required>
          </div>
          <div class="form-group">
            <label for="desc">Description </label>
            <input type="text" class="form-control" id="desc" v-model="newRow.description" required>
          </div>
          <!-- Vous pouvez ajouter des champs pour les autres colonnes ici -->
          <button type="submit" class="btn btn-primary">Enregistrer</button>
          <button @click="closeDialog" class="modal-close is-large" aria-label="close">Fermer</button>

        </form>
        </div>
      </div>
                </div>
      <div class="table-cell">
          <button class="btn-icon"><i class="bi bi-filetype-csv"></i></button>
      </div> 
      <div class="table-cell fill">
                  <i class="bi bi-funnel-fill"></i>
                  <input type="text" class="col-lg-4 fill1" placeholder="Filtrer">
            </div>
      <div class="table-cell col-lg-4 search">
          <input type="text" placeholder="Rechercher..." class="col-lg-10">
          <button class="btn-icon"><i class="bi bi-search"></i></button>
      </div>
      <div class="table-cell">
          <label for="itemsPerPage">Afficher </label>
          <select id="itemsPerPage">
              <option value="10">10</option>
              <option value="20">20</option>
              <option value="50">50</option>
          </select>
      </div>
      <div class="table-cell">
          <button class="btn-icon imprimer"><i class="bi bi-printer"></i></button>
      </div>
      <div class="table-cell pagination">
          <span>elements</span>
          <button class="btn-icon"><i class="bi bi-chevron-double-left"></i></button>
          <button class="btn-icon"><i class="bi bi-chevron-left"></i></button>
          <span class="page-number">1</span>
          <span class="page-number">2</span>
          <button class="btn-icon"><i class="bi bi-chevron-right"></i></button>
          <button class="btn-icon"><i class="bi bi-chevron-double-right"></i></button>
      </div>
    </div>
   
    <table class="table">
      
      <thead>
        <tr>
          <th>code</th>
          <th>Nom de l'equipe</th>
          <th>Description</th>
          <th>Cree le </th>
        </tr>
      </thead>
      <tbody >
        <!--<tr v-for="(row, index) in tableData" :key="index">
      <router-link :to="'/teamdetail/' + row.idteam">
        <td>{{ row.idteam }}</td>
        <td>{{ row.name }}</td>
        <td>{{ row.description }}</td>
        <td>{{ row.created_at }}</td>
      </router-link>
    </tr>-->
        <tr v-for="(row, index) in tableData"
      :to="'/teamdetail/' + row.idteam" 
      :key="index"  >
          
      <td>{{ row.idteam }}</td>
          <td>{{ row.name }}</td>
          <td>{{ row.description }}</td>
          <td>{{ row.created_at }}</td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import {addTeam, getTeams} from '@/services/adminServices';

export default {
  name: 'TeamPage',
  data() {
    return {
      tableData: [ ], 
      newRow: {
        team_name: "",
        team_description: "",
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
    openDialog() {
      this.dialogVisible = true;
    },
    closeDialog() {
      this.dialogVisible = false;
      this.resetForm(); 
    },
    resetForm() {
        this.team_name = '';
        this.desc = '';
    },

    addRow() {
      addTeam(this.newRow)
      .then(response => {
                    if (response.status == 200)
                      alert("L'equipe a été ajoutée avec succès");
                    const idp =response.data;
                    console.log(idp);

                    this.resetForm(); 
                    this.closeDialog(); 
                })
                .catch(error => {
                    console.error('Erreur lors de l\'ajout de lequipe:', error);
                });

      // Ajoute la nouvelle ligne aux données du tableau
      //this.tableData.push({ ...this.newRow });
    },

    fetchData() {
      getTeams()
        .then((response) => {
          this.tableData = [...response.data]
        })
        .catch((error) => {
          console.error(error)
        });
    },
  },
  mounted() {
    // Appelle fetchData pour charger la liste des equipe au chargement de la page
    this.fetchData();
  },
  created() {
    // Initialise la première ligne
   // this.newRow.col1 = "1"+ this.tableData[-1].col1;

  },
};
</script>
<style src="../../style.css"></style>