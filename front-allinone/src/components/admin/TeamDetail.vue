<template>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
      <div class="row">
      <div class="col-md-6">
        <div class="row">
          <div class="card mr-4">
          <div class="card-header">Détails de l'equipe</div>
          <div class="card-body">
            <form>
              <div class="mb-3">
                <label for="identif" class="form-label">identifiant de l'equipe</label>
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
                <label for="membre" class="col">Les membres de l'équipe :</label>
                    <ul>
                      <li v-for="(member, index) in team.members" :key="member.idmember">
                        {{ member.username }}
                        <span @click="supprimerMembre(index)" style="cursor: pointer;">
                          <i class="bi bi-x-circle"></i>
                        </span>
                      </li>
                    </ul>
                <select class="form-control" id="membre" v-model="selectedMember">
                  <option value="">Sélectionnez un membre</option>
                  <option v-for="member in membres" :key="member.idmember" :value="member.idmember">{{ member.username }}</option>
                </select> 
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
  import {getTeam, editTeam, delTeam, getMembers, delMemberOfTeam} from '@/services/adminServices';
  import { mapState } from 'vuex';

  export default {
    name: 'TeamDetail',
    data() {
      return {
        team: {
          members: [{
            idmember: "",
            username: "",
          }
        ],
        },
        projet: [{
          id: "",
          project_name: "",
        }
        ],
        membres: [
          {
            idmember: "",
            username: "",
          }
        ],
        selectedMember: null,
        prochainesReunions: [],
      }
    },
    computed: {
    ...mapState(['modifications']),

  },
  methods: {
    
    confirmerSuppressionTeam() {
    if (window.confirm("Voulez-vous vraiment supprimer ce projet ?")) {
      // Logique de suppression de la team ici
      this.supprimerProjet();
    }
    },

    supprimerTeam() {
      delTeam(this.team.idproject_team)
      .then(response => {
        if(response.status == 200){
          alert('La team a bien été supprimée');
        }
      })
    },
    supprimerMembre(index) {
    if (window.confirm("Voulez-vous vraiment supprimer ce membre de l'équipe ?")) {
      console.log(this.team.members[0].idmember);

      delMemberOfTeam(this.team.idproject_team,this.team.members[index].idmember)
      .then(response => {
        console.log(response.data);
        if(response.status == 201){
          this.team.members.splice(index, 1); // Supprime le membre à l'index spécifié
          alert('Le membre a bien été ajouté à cette équipe');
        }
      })
      .catch(error => {
        console.error('Erreur ', error);
      });

    }
    },
 
    enregistrerModifications() {
      this.team.members.push({ idmember: this.selectedMember });
      console.log(this.team);

      editTeam(this.team.idproject_team, this.team,{
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        if (response.status == 200) {
          console.log(response);
        }
      })
      .catch(error => {
        console.error('Erreur ', error);
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
        console.log(this.team);
      
    })
    .catch(error => {
      console.error('Erreur ', error);
    });
    getMembers()
      .then(response => {
        if (response.status === 200) {
          if (this.team.members && this.team.members.length > 0) {
            this.membres = response.data.filter(member => !this.team.members.includes(member));
          } else {
            // Si team_members n'est pas défini ou est vide, alors tous les membres sont disponibles
            this.membres = response.data;
          }        } 
      else {
          console.error('Erreur', response);
        }
      })
      .catch(error => {
        console.error('Erreur', error);
      });
  },
  }
  </script>
  <style src="../../style.css"></style>