<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
    <div class="table-row">
      <div class="table-cell">
        <button type="button" class="btn-icon" @click="openDialog" @close="closeDialog" data-bs-toggle="modal" data-bs-target="#backdrop" data-test="mod"><i class="bi bi-plus"></i>Ajouter</button>
        <TeamForm1 v-show="dialogVisible" />
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
        <ul class="pagination">
                <span class="pagination">éléments</span>

    <li class="page-item lip">
      <a class="page-link lip" href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li class="page-item lip" aria-current="page"><a class="page-link pactive lip" href="#">1</a></li>
    <li class="page-item lip"><a class="page-link lip" href="#">2</a></li>
    <li class="page-item ">
      <a class="page-link lip" href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
      </div>
    </div>
   
    <table class="table">
      
      <thead>
        <tr>
          <th>Code</th>
          <th>Nom de l'équipe</th>
          <th>Description</th>
          <th>Créé le </th>
        </tr>
      </thead>
      <tbody >
        <tr v-for="(team, index) in tableData"
      :key="index"  >
          
      <td><router-link style="text-decoration: none; color: #000000;" :to="'teamdetail/' + team.idteam">{{ team.idteam }}</router-link></td>
      <td><router-link style="text-decoration: none; color: #000000;" :to="'teamdetail/' + team.idteam">{{ team.name }}</router-link></td>
      <td><router-link style="text-decoration: none; color: #000000;" :to="'teamdetail/' + team.idteam">{{ team.description }}</router-link></td>
      <td><router-link style="text-decoration: none; color: #000000;" :to="'teamdetail/' + team.idteam">{{ formatDate(team.created_at ) }}</router-link></td>
        </tr>
      </tbody>
    </table>

  </div>
</template>

<script>
import {addTeam, getTeams} from '@/services/adminServices';
import TeamForm1 from '../_Forms/TeamForm1.vue';


export default {
  name: 'TeamPage',
  data() {
    return {
      tableData: [ ], 
      newRow: {
        team_name: '',
        team_description: '',
      },
      dialogVisible: false, // Contrôle l'affichage de la boîte de dialogue
    };
  },
  components: {
  TeamForm1
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
    formatDate(dateString) {
      const options = { day: 'numeric', month: 'short', year: 'numeric' };
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', options);
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