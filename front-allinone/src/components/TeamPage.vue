<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
    <!-- Bouton pour ajouter une nouvelle ligne -->
    <button @click="openDialog" class="btn btn-primary">Ajouter une ligne</button>
    <div class="modal modal-sm" :class="{ 'is-active': dialogVisible }">
      <div class="modal-background"></div>
      <div class="modal-content">
        <form @submit.prevent="addRow">
        <div class="form-group">
          <label for="col1">Colonne 1</label>
          <input type="text" class="form-control" id="col1" v-model="newRow.col1" required>
        </div>
        <div class="form-group">
          <label for="col2">Colonne 2</label>
          <input type="text" class="form-control" id="col2" v-model="newRow.col2" required>
        </div>
        <div class="form-group">
          <label for="col3">Colonne 3</label>
          <input type="text" class="form-control" id="col3" v-model="newRow.col3" required>
        </div>
        <!-- Vous pouvez ajouter des champs pour les autres colonnes ici -->
        <button type="submit" class="btn btn-primary">Ajouter</button>
      </form>
      </div>
      <button @click="closeDialog" class="modal-close is-large" aria-label="close"></button>
    </div>
   
    <!-- Tableau -->
    <table class="table">
      <thead class="bg-royal-blue text-white">
        <tr>
          <th>code</th>
          <th>Nom de l'equipe</th>
          <th>Description</th>
          <th>Projets</th>
          <th>Type</th>
          <th>Members</th>
          <th>Colonne 7</th>
          <th>Colonne 8</th>
        </tr>
      </thead>
      <tbody>
        <!-- Boucle sur les lignes de données -->
        <tr v-for="(row, index) in tableData" :key="index">
          <td>{{ row.col1 }}</td>
          <td>{{ row.col2 }}</td>
          <td>{{ row.col3 }}</td>
          <td>{{ row.col4 }}</td>
          <td>{{ row.col5 }}</td>
          <td>{{ row.col6 }}</td>
          <td>{{ row.col7 }}</td>
          <td>{{ row.col8 }}</td>
        </tr>
      </tbody>
    </table>

    <!-- Boîte de dialogue pour ajouter une nouvelle ligne -->
    
  </div>
</template>

<script>
export default {
  name: 'TeamPage',
  data() {
    return {
      tableData: [
        {
          col1: "T00001",
          col2: "Team1",
          col3: "Like you",
          col4: "Like you",
          col5: "Like you",
          col6: "Like you",
          col7: "Like you",
          col8: "Like you",
        },
        {
          col1: "T00002",
          col2: "Team2",
          col3: "Like me",
          col4: "Like me",
          col5: "Like me",
          col6: "Like me",
          col7: "Like me",
          col8: "Like me",
        },
      ], // Les données du tableau
      newRow: {
        col1: "",
        col2: "",
        col3: "",
      },
      dialogVisible: false, // Contrôle l'affichage de la boîte de dialogue
    };
  },
  methods: {
    openDialog() {
      this.dialogVisible = true;
    },
    closeDialog() {
      this.dialogVisible = false;
    },
    addRow() {
      // Ajoute la nouvelle ligne aux données du tableau
      this.tableData.push({ ...this.newRow });

      // Réinitialise le formulaire
      this.newRow = {
        col1: "",
        col2: "",
        col3: "",
        // Réinitialisez les autres colonnes ici
      };

      // Ferme la boîte de dialogue
      this.dialogVisible = false;
    },
  },
  created() {
    // Initialise la première ligne
   // this.newRow.col1 = "1"+ this.tableData[-1].col1;

  },
};
</script>
<style src="../style.css"></style>