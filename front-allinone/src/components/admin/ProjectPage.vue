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
            <div class="table-cell fill">
                  <i class="bi bi-funnel-fill"></i>
                  <input type="text" class="col-lg-4 fill1" placeholder="Filtrer">
            </div>
            <div class="table-cell col-lg-4 search">
                  <input type="text" placeholder="Rechercher..." class="col-lg-10">
                  <button class="btn-icon"><i class="bi bi-search"></i></button>
            </div>
            <div class="table-cell">
                <label for="itemsPerPage" class="col-6">Afficher </label>
                <select id="itemsPerPage">
                    <option value="10">10</option>
                    <option value="20">20</option>
                    <option value="50">50</option>
                </select>
            </div>
            <div class="table-cell">
                <button class="btn-icon imprimer"><i class="bi bi-printer"></i></button>
            </div>
            <div class="table-cell">
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
        <div class="table-responsive">

          <table class="table table-hover project-table" >
            <thead class="p-t-head">
              <tr>
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
            <tr v-for="project in projects" :key="project.idproject" href="#" class="p-a">

              <!--<td class="checkbox-cell">
                <input type="checkbox" :id="'row' + project.idproject">
                <label :for="'row' + project.idproject"></label>
              </td>-->
              <td><router-link style="text-decoration: none; color: #000000;" :to="'projet/' + project.idproject">{{ project.idproject }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ project.name }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ project.description }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ formatDate(project.created_at) }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ formatDate(project.expired_at) }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ project.progress }}</router-link></td>
              <td><router-link v-if="project.comments && project.comments.length > 0"
                       style="text-decoration: none; color: #002060;"
                       :to="'projet/' + project.idproject">
                        {{ project.comments[0] }}
              </router-link>
              <span v-else></span>
              </td>              
            <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ project.requirement }}</router-link></td>
              <td><router-link style="text-decoration: none; color: #002060;" :to="'projet/' + project.idproject">{{ project.status }}</router-link></td>
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
      userConnected: null,
    }
  },
  computed: {
    currentUser() {
      const user = this.$store.state.auth.user;
      console.log('Username:', user);
      return user;
    },
    
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
          //console.log(response);
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