<template>
  <div>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
    <div class="row">
      <div class="col-md-6">
        <div class="row">
          <div class="card mr-4">
          <div class="card-header">Détails du Projet</div>
          <div class="card-body">
            <!-- Formulaire de modification des champs -->
            <form>
              <div class="mb-3">
                <label for="identif" class="form-label">Client du Projet</label>
                <input type="text" class="form-control" id="identif" v-model="client.idclient">
              </div>
              <div class="mb-3">
                <label for="name" class="form-label">Nom du Projet</label>
                <input type="text" class="form-control" id="name" v-model="client.client_name">
              </div>
              <div class="mb-3">
                <label for="desc" class="form-label">Description du Projet</label>
                <input type="text" class="form-control" id="desc" v-model="client.description">
              </div>
              <div class="mb-3">
                <label for="equipe" class="form-label">Équipe de Gestion</label>
                <input type="text" class="form-control" id="equipe" v-model="client.team">
              </div>
              <div class="mb-3">
                <label for="commentaire" class="form-label">Commentaire</label>
                <textarea class="form-control" id="commentaire" v-model="client.comments"></textarea>
              </div>
              <div class="mb-3">
                <label for="avancement" class="form-label">Avancement</label>
                <input type="text" class="form-control" id="avancement" v-model="client.progress">
              </div>
              <div class="mb-3">
                <label for="req" class="form-label">Outils exterieurs</label>
                <input type="text" class="form-control" id="req" v-model="client.requirement">
              </div>
              <div class="mb-3">
                <label for="debut" class="form-label">Debuter le</label>
                <input type="text" class="form-control" id="debut" v-model="client.created_at">
              </div>
              <div class="mb-3">
                <label for="fin" class="form-label">Fin estimer a </label>
                <input type="text" class="form-control" id="fin" v-model="client.expired_at">
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
              <li v-for="tache in dernieresTachesEffectuees" :key="tache.idtache">{{ tache }}</li>
            </ul>
          </div>
        </div>
       </div>
      </div>
    </div>
  </main>
  </div>
</template>

<script>
/* import {getClient, editClient} from '@/services/adminServices';*/

export default {
  name: 'ClientsDetail',
  data() {
    return {
      client: {},
      prochainesReunions: ['Réunion 1', 'Réunion 2'],
      rapportsDuProjet: ['Rapport 1', 'Rapport 2'],
      dernieresTachesEffectuees: ['Tâche 1', 'Tâche 2'],
    };
  },/*
  methods: {
    confirmerSuppressionProjet() {
    if (window.confirm("Voulez-vous vraiment supprimer ce projet ?")) {
      // Logique de suppression du projet ici
      this.supprimerProjet();
    }
    },

    supprimerProjet() {
    },

    enregistrerModifications() {
      editclient(this.client)
      .then(response => {
        if (response.status == 200)
          alert("Modification enregistree");
          console.log('Le projet a bien été modifié');
      })
    },
  },
  mounted() {
    const idclient = this.$route.params.id;
    getclient(idclient)
    .then(response => {
      if (response.status == 200)
        this.client = response.data
        // console.log(this.client);
    })
    .catch(error => {
      // Gérez les erreurs ici, par exemple, affichez un message d'erreur à l'utilisateur
      console.error('Erreur ', error);
    });
  },*/
};
</script>
<style src="../../style.css"> </style>
