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

          <table class="table  table-sm project-table">
            <thead class="head-content p-t-head">
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
              <!-- Utilisation de v-for pour afficher les projets -->
          <a v-for="project in projects" :key="project.idproject" :href="'/projet/' + project.idproject" class="p-a">

            <tr>
              <td class="checkbox-cell">
                <input type="checkbox" :id="'row' + project.idproject">
                <label :for="'row' + project.idproject"></label>
              </td>
              <td>{{ project.code }}</td>
              <td>{{ project.name }}</td>
              <td>{{ project.description }}</td>
              <td>{{ project.created_at }}</td>
              <td>{{ project.expired_at }}</td>
              <td>{{ project.progress }}</td>
              <td>{{ project.comments }}</td>
              <td>{{ project.requirement }}</td>
              <td>{{ project.status }}</td>
            </tr>
          </a>

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
  },
  mounted() {
    // Appeler fetchData pour charger la liste des projets au chargement de la page
    this.fetchData();
  },
};
</script>
<style src="../../style.css"> </style>