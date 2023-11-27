<template>
    <div>
        <main class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
          <div class="table-row">
            <div class="table-cell">
                <button type="button" class="btn-icon" @click="showModal"  @close="closeModal" data-bs-toggle="modal" data-bs-target="#backdrop" data-test="mod"><i class="bi bi-plus"></i>Ajouter</button>
                <ProjectForm1 v-show="isModalVisible" />
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

          <table class="table project-table">
            <thead class="p-t-head">
              <tr>
                <th class="checkbox-cell">
                    <input type="checkbox" id="selectAll">
                    <label for="selectAll"></label>
                </th>
                <th>Code</th>
                <th>Nom Projet</th>
                <th>Description</th>
                <th>Debut</th>
                <th>Fin estimer</th>
                <th>Avancement</th>
                <th>Commentaires</th>
                <th>External requirement</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <!-- Utilisation de v-for pour afficher les projets -->
            <tr v-for="project in projects" :key="project.idproject" :href="'/projet/' + project.idproject" class="p-a">

              <td class="checkbox-cell">
                <input type="checkbox" :id="'row' + project.idproject">
                <label :for="'row' + project.idproject"></label>
              </td>
              <td><router-link :to="'projet/' + project.idproject" style="text-decoration: none !important;">{{ project.idproject }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.name }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.description }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.created_at }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.expired_at }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.progress }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.comments }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.requirement }}</router-link></td>
              <td><router-link :to="'projet/' + project.idproject">{{ project.status }}</router-link></td>
            </tr>

            </tbody>
          </table>
        </div>
      </main>
    </div>
</template>
<script>
import ProjectForm1 from '../_Forms/ProjectForm1.vue';
import {getListProject} from '@/services/adminServices';


export default {
  name: 'ProjectPage',
  components: {
    ProjectForm1
  },
  data() {
    return {
      projects: [],
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
      },
      fetchData() {
      getListProject()
        .then((response) => {
          this.projects = response.data
        })
        .catch((error) => {
          console.error(error)
        });
    },
    formatDate(dateString) {
      const options = { day: 'numeric', month: 'short', year: 'numeric' };
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', options);
      },
  },
  mounted() {
    // Appeler fetchData pour charger la liste des projets au chargement de la page
    this.fetchData();
  },
};
</script>
<style src="../../style.css"> </style>