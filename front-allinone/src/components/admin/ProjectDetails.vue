<template>
  <div>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
    <div class="row">
      <div class="col-md-6">
        <div class="row">
          <div class="card mr-4">
          <div class="card-header" style="margin-top: 5% !important;">Détails du Projet</div>
          <div class="card-body">
            <!-- Formulaire de modification des champs -->
            <form>
              <div class="mb-3">
                <label for="identif" class="form-label">Identifiant du Projet</label>
                <input type="text" class="form-control" id="identif" v-model="dynamicModel">
              </div>
              <div class="mb-3">
                <label for="name" class="form-label">Nom du Projet</label>
                <input type="text" class="form-control" id="name" v-model="project.project_name">
              </div>
              <div class="mb-3">
                <label for="desc" class="form-label">Description du Projet</label>
                <input type="text" class="form-control" id="desc" v-model="project.description">
              </div>
              <div class="mb-3">
                <label for="equipe" class="form-label">Équipe de Gestion</label>
                <select class="form-select" id="equipe" value="Sélectionnez une équipe" v-model="project.team">
                    <option  selected disabled>Sélectionnez une équipe</option>
                    <option v-for="t in teams" :key="t.idproject_team" :value="t.name">{{ t.name }}</option>
                </select>
                {{ project.team ? project.team.team_name : '' }}
                </div>
                          <div class="mb-3">
                <label for="commentaire" class="form-label">Commentaire</label><textarea v-if="Array.isArray(project.comments)" class="form-control" id="commentaire" v-model="project.comments[0]"></textarea>
    <textarea v-else class="form-control" id="commentaire" v-model="project.comments"></textarea>
</div>
              <div class="mb-3">
                <label for="avancement" class="form-label">Avancement</label>
                <input type="text" class="form-control" id="avancement" v-model="project.progress">
              </div>
              <div class="mb-3">
                <label for="req" class="form-label">Outils exterieurs</label>
                <input type="text" class="form-control" id="req" v-model="project.requirement">
              </div>
              <div class="mb-3">
                <label for="debut" class="form-label">Debuter le</label>
                <input type="text" class="form-control" id="debut" v-model="project.created_at">
              </div>
              <div class="mb-3">
                <label for="fin" class="form-label">Fin estimer a </label>
                <input type="text" class="form-control" id="fin" v-model="project.expired_at">
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

      <!-- Deuxième colonne pour les prochaines réunions, les rapports et les tâches -->
      <div class="col-md-6">
       <div class="row detail-row">
        <div class="card">
          <div class="card-header">Informations Complémentaires</div>
          <div class="card-body">
            <!-- Prochaines réunions -->
            <h5>Prochaines Réunions</h5>
            <ul>
              <li v-for="reunion in prochainesReunions" :key="reunion.idreunion">{{ reunion }}</li>
            </ul>

            <!-- Liste des rapports du projet -->
            <h5>Rapports du Projet</h5>
            <ul>
              <li v-for="rapport in rapportsDuProjet" :key="rapport.idrapport">{{ rapport }}</li>
            </ul>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
          
            <h5>Dernières Tâches Effectuées</h5>
            <ul>
              <router-link style="text-decoration: none; color: #002060;"
                v-for="tache in dernieresTachesEffectuees"
                :to="'/team/' + cuser"
                :key="tache.idtache"
              >
                <li>{{ tache }}</li>
              </router-link>
            </ul>
          </div>
        </div>
       </div>
      </div>
    </div>
    <div class="modal detail-mod" v-if="showSuccessModal">
      <div class="modal-content detail-cont">
        <span class="close" @click="showSuccessModal = false">&times;</span>
        <h2>Modification réussie</h2>
        <p>Les modifications ont été enregistrées avec succès.</p>
      </div>
    </div>
  </main>
  </div>
</template>

<script>
import {getProject, editProject, delProject, getTeams} from '@/services/adminServices';
import { mapState, mapGetters } from 'vuex';


export default {
  name: 'ProjectDetails',
  data() {
    return {
      cuser: 0,
      project: {
        team: {
        idproject_team: 0,
        team_name: ""
      },
      },
      teams: [],
      prochainesReunions: ['Réunion 1', 'Réunion 2'],
      rapportsDuProjet: ['Rapport 1', 'Rapport 2'],
      dernieresTachesEffectuees: ['Tâche 1', 'Tâche 2'],
      showSuccessModal: false,
    };
  },
  computed: {
    ...mapState(['modifications']),
    ...mapGetters(['currentUser']),

    dynamicModel: {
    get() {
      return "000" + this.project.idproject;
    },
    set(value) {
      console.log("Nouvelle valeur :", value);
    },
  },
  },
  methods: {
    
    confirmerSuppressionProjet() {
    if (window.confirm("Voulez-vous vraiment supprimer ce projet ?")) {
      // Logique de suppression du projet ici
      this.supprimerProjet();
    }
    },

    supprimerProjet() {
      delProject(this.project.idproject)
      .then(response => {
        if(response.status == 200){
          alert('Le projet a bien été supprimé');
        }
      })
    },

    enregistrerModifications() {
      editProject(this.project.idproject, this.project)
      .then(response => {
        if (response.status == 200) {
          this.$showSuccessModal = true; // Affiche le modal de succès
        }
      })
      .catch(error => {
        console.error('Erreur ', error);
    });
    },
  },
  mounted() {
    const idproject = this.$route.params.id;
    getProject(idproject)
    .then(response => {
      if (response.status == 200)
        this.project = response.data
        this.cuser=this.project.iduser;
         // console.log(this.project.team);
    })
    .catch(error => {
      console.error('Erreur ', error);
    });
  
    getTeams()
      .then(response => {
        if (response.status === 200) {
          this.teams = response.data;
        } else {
          console.error('Erreur', response);
        }
      })
      .catch(error => {
        console.error('Erreur', error);
      });
  },
};
</script>
<style src="../../style.css"> </style>
