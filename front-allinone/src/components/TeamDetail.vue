<template>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
      <div class="row">
      <div class="col-md-6">
        <div class="row">
          <div class="card mr-4">
          <div class="card-header">Détails du Projet</div>
          <div class="card-body">
            <form>
              <div class="mb-3">
                <label for="identif" class="form-label">Client du Projet</label>
                <input type="text" class="form-control" id="identif" v-model="team.idproject_team">
              </div>
              <div class="mb-3">
                <label for="name" class="form-label">Nom du Projet</label>
                <input type="text" class="form-control" id="name" v-model="team.team_name">
              </div>
              <div class="mb-3">
                <label for="desc" class="form-label">Description du Projet</label>
                <input type="text" class="form-control" id="desc" v-model="team.team_description">
              </div>
              <div class="mb-3">
                <label for="members">Sélectionnez des valeurs :</label>
                <select
                  id="members"
                  v-model="team.idmember"
                  multiple
                  @change="updateDisplayValues"
                >
                  <option v-for="member in membres" :key="member.idmember" :value="member.member_name">
                    {{ member.member_name }}
                  </option>
                </select>

                <div>
                  <label for="displayedValues">Les membres de l'equipe :</label>
                  <div id="displayedValues">
                    {{ displayedValues.join(', ') }}
                  </div>
                </div>
              </div>
              <div class="mb-3">
                <label for="debut" class="form-label">Debuter le</label>
                <input type="text" class="form-control" id="debut" v-model="team.created_at">
              </div>
              <div class="mb-3">
                <label for="fin" class="form-label">Fin estimer a </label>
                <input type="text" class="form-control" id="fin" v-model="team.updated_at">
              </div>
              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <button class="btn btn-outline-danger" @click="confirmerSuppressionProjet">Supprimer</button>
                <button class="btn btn-primary" @click="enregistrerModifications">Enregistrer</button>

              </div>
            </form>
          </div>
        </div>
        </div>
      </div>

      <div class="col-md-6">
       <div class="row detail-row">
        <div class="card">
          <div class="card-header">Projets de l'équipe</div>
          <div class="card-body">
            <h5>Prochaines Réunions</h5>
            <ul>
              <li v-for="project in projet" :key="project.id">{{ project.name }}</li>
            </ul>
          </div>
        </div>
       </div>
      </div>
    </div>
    </main>
  </template>
  
  <script>
  import {getTeam, editTeam, delTeam} from '@/services/adminServices';
  import { mapState } from 'vuex';

  export default {
    name: 'TeamDetail',
    data() {
      return {
        team: {},
        projet: [{
          id: "",
          project_name: "",
        }
        ],
        membres: [
          {
            idmember: "",
            member_name: "",
          }
        ],
        selectedValues: [],
        displayedValues: [],
        prochainesReunions: [],
      }
    },
    computed: {
    ...mapState(['modifications']),

  },
  methods: {
    
    confirmerSuppressionProjet() {
    if (window.confirm("Voulez-vous vraiment supprimer ce projet ?")) {
      // Logique de suppression de la team ici
      this.supprimerProjet();
    }
    },

    supprimerProjet() {
      delTeam(this.project.idproject)
      .then(response => {
        if(response.status == 200){
          alert('La team a bien été supprimée');
        }
      })
    },

    enregistrerModifications() {
      editTeam(this.team.idproject_team, this.team)
      .then(response => {
        if (response.status == 200) {
          this.$showSuccessModal = true; // Affiche le modal de succès
        }
      })
      .catch(error => {
        console.error('Erreur ', error);
    });
    },
    updateDisplayValues() {
      // Mettez à jour les valeurs affichées chaque fois que la sélection change
      this.displayedValues = this.selectedValues.map((member_name) => {
        const selectedOption = this.membres.find((member) => member.member_name === member_name);
        return selectedOption ? selectedOption.member_name : '';
      });
    },
  },
  mounted() {
    const idproject_team = this.$route.params.id;
    getTeam(idproject_team)
    .then(response => {
      if (response.status == 200)
        this.team = response.data;
        this.projet = this.team.projets;
        this.membres = this.team.members
        console.log(this.team.members);
    })
    .catch(error => {
      console.error('Erreur ', error);
    });
  },
  }
  </script>
  <style src="../style.css"></style>