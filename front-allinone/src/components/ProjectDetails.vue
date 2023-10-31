<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1" style="margin-top: 20px;">
    <div class="row">
      <div class="col-md-6">
        <div class="row">
          <div class="card mr-4">
          <div class="card-header">Détails du Projet</div>
          <div class="card-body">
            <!-- Formulaire de modification des champs -->
            <form>
              <div class="mb-3">
                <label for="client" class="form-label">Client du Projet</label>
                <input type="text" class="form-control" id="client" v-model="project.client">
              </div>
              <div class="mb-3">
                <label for="equipe" class="form-label">Équipe de Gestion</label>
                <input type="text" class="form-control" id="equipe" v-model="project.equipe">
              </div>
              <div class="mb-3">
                <label for="commentaire" class="form-label">Commentaire</label>
                <textarea class="form-control" id="commentaire" v-model="project.commentaire"></textarea>
              </div>
              <div class="mb-3">
                <label for="avancement" class="form-label">Avancement</label>
                <input type="text" class="form-control" id="avancement" v-model="project.avancement">
              </div>
              <div class="mb-3">
                <label for="dates" class="form-label">Dates</label>
                <input type="text" class="form-control" id="dates" v-model="project.dates">
              </div>
              <!-- Autres champs de modification -->
              <!-- Ajoutez des boutons pour supprimer et enregistrer -->
              <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                <button class="btn btn-danger me-md-2" @click="supprimerProjet">Supprimer</button>
                <button class="btn btn-primary" @click="enregistrerModifications">Enregistrer</button>
              </div>
            </form>
          </div>
        </div>
        </div>
      </div>

      <!-- Deuxième colonne pour les prochaines réunions, les rapports et les tâches -->
      <div class="col-md-6">
       <div class="row">
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
  </div>
</template>

<script>
export default {
  name: 'ProjectDetails',
  data() {
    return {
      project: {
        client: 'Nom du client',
        equipe: 'Équipe de gestion',
        commentaire: 'Commentaire du projet',
        avancement: 'Avancement du projet',
        dates: 'Dates du projet',
        // Autres champs du projet
      },
      prochainesReunions: ['Réunion 1', 'Réunion 2'],
      rapportsDuProjet: ['Rapport 1', 'Rapport 2'],
      dernieresTachesEffectuees: ['Tâche 1', 'Tâche 2'],
    };
  },
  methods: {
    supprimerProjet() {
      // Logique pour supprimer le projet
    },
    enregistrerModifications() {
      // Logique pour enregistrer les modifications du projet
    },
  },
};
</script>
<style src="../style.css"> </style>
