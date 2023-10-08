<template>
    <div>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
          <div class="table-row">
            <div class="table-cell">
                <button type="button" class="btn-icon" @click="showModal" data-bs-toggle="modal" data-bs-target="#backdrop"><i class="bi bi-plus"></i>Ajouter</button>
                <ProjectForm1 v-show="isModalVisible" @close="closeModal" />
              </div>
            <div class="table-cell">
                <button class="btn-icon"><i class="bi bi-filetype-csv"></i></button>
            </div>
            <div class="table-cell">
                <button class="btn-icon"><i class="bi bi-funnel-fill"></i> Filtrer</button>
                <input type="text" class="col-lg-4">
            </div>
            <div class="table-cell col-lg-4 search">
                <input type="text" placeholder="Rechercher..." class="col-lg-8">
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
        <div class="table-responsive">
          <table class="table table-striped table-sm">
            <thead class="head-content">
              <tr>
                <th class="checkbox-cell">
                    <input type="checkbox" id="selectAll">
                    <label for="selectAll"></label>
                </th>
                <th scope="col">Code</th>
                <th scope="col">Nom Projet</th>
                <th scope="col">Description</th>
                <th scope="col">Debut</th>
                <th scope="col">Fin estimer</th>
                <th scope="col">Avancement</th>
                <th scope="col">Commentaires</th>
                <th scope="col">External requirement</th>
                <th scope="col">Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <a href="/projectdetails"> 
                  <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                  </td>
                  <td>1,001</td>
                  <td>random</td>
                  <td>data</td>
                  <td>placeholder</td>
                  <td>text</td>
                  <td>text</td>
                  <td>text</td>
                  <td>text</td>
                  <td>text</td>
                </a>
                
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
              <tr>
                <td class="checkbox-cell">
                    <input type="checkbox" id="row1">
                    <label for="row1"></label>
                </td>
                <td>1,001</td>
                <td>random</td>
                <td>data</td>
                <td>placeholder</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
                <td>text</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div>
</template>
<script>
import ProjectForm1 from './_Forms/ProjectForm1.vue';

export default {
  name: 'ProjectPage',
  components: {
    ProjectForm1
  },
  data() {
    return {
      isModalVisible: false,
    }
  },
  methods: {
    // Afficher le modal
    showModal() {
        this.isModalVisible = true;
      },
    closeModal() {
        this.isModalVisible = false;
      }
  },
};
</script>
<style>
/** Options de la table**/
.table-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ffffff;
    border-bottom: 2px solid #ddd;
    padding: 10px;
    margin-bottom: 5%;
}

.table-cell {
    display: inline-block;
}
.btn-icon {
    background: none;
    border: 1px solid #EAE1D2;
    cursor: pointer;
    font-size: 16px;
    align-items: center;
}

.search {
    display: flex;
    align-items: center;
}

.search input {
    border: 1px solid #ddd;
    padding: 5px;
    border-radius: 3px;
    background-color: #EAE1D2;
}

.search .btn-icon {
    background-color: #002060;
    color: #EAE1D2;
    border: none;
    padding: 5px;
    border-radius: 3px;
    cursor: pointer;
}

#itemsPerPage {
    border: 1px solid #ddd;
    padding: 5px;
    border-radius: 3px;
}

.pagination .page-number {
    margin: 0 10px;
}
/** Table**/

table {
  border: 4px solid #002060;
  border-collapse: collapse;
  width: 100%;
}

/* Ajouter une couleur de fond à l'en-tête du tableau */
.head-content {
background-color: #002060;
color: #002060;
text-align: left;
padding: 8px;
}
/* Ajouter des séparateurs entre les cellules du tableau */
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  color: #002060;
}

/* Ajouter un style pour les lignes lorsque vous survolez */
tr:hover {
  background-color: #002060;
}

/* Ajouter des cases à cocher à chaque ligne */
.checkbox-cell {
  width:2%;
  margin-top: 0px;

  text-align: center;
}

/* Ajouter une option pour supprimer lorsque la case est cochée */
.checkbox-cell input[type="checkbox"] {
  display: none;
}
.checkbox-cell label {
            cursor: pointer;
            position: relative;
            padding-left: 25px;
        }

.checkbox-cell label:before {
  content: "";
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 1px solid #ddd;
  position: absolute;
  left: 0;
  top: 1px;
}

.checkbox-cell input[type="checkbox"]:checked + label:before {
  background-color: #002060;
  border: 1px solid #002060;
}
</style>