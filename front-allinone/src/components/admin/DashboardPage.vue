<template>
   <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2">
    <div class="container">
      <div class="row dash-row">
          <div v-for="(group, status) in groupedProjects" :key="status" class="dash-card col-3">
            <div class="card my-card">
              <div class="status">{{ status }}</div>
                <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
                  <div class="carousel-indicators">
                    <button
                      type="button"
                      v-for="(project, projectIndex) in  group"
                      :key="projectIndex"
                      data-bs-target="#carouselExampleCaptions"
                      :data-bs-project-to="projectIndex"
                      :class="{ active: projectIndex === 0 }"
                      aria-label="project"
                      class="cap"
                    ></button>
                  </div>
                  <div class="carousel-inner project-card">
                    <div
                      v-for="(project, projectIndex) in group"
                      :key="projectIndex"
                      class="carousel-item"
                      :class="{ active: projectIndex === 0 }"
                    >
                      <img :src="require(`@/assets/${project.image}`)" alt="Project Slide" class="card-img-top" >
                      <div class="card-body mt-20" style="margin-bottom: 20px;">
                        <h5 class="card-title c-t">{{ project.name }}  {{ group.length }}</h5>
                        <h6 class="card-text">{{truncateDescription(project.description, 60) }}</h6>
                      </div>
                    </div>
                  </div>
                </div>
            </div>
            </div>
            <!--<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                  </button>
                  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                  </button>-->
          </div>    
    </div>
  </div>
</template>
<script>
import {getListProject} from '@/services/adminServices';

export default {
  name: 'DashboardPage',
  data() {
    return {
      projects: [],
      groupedProjects: {}, 
    }
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  methods: {
    truncateDescription(description, maxLength) {
      if (description.length > maxLength) {
        return description.substring(0, maxLength) + '...';
      }
      return description;
    },
    groupProjectsByStatus() {
      
      // Regrouper les projets par statut
      this.groupedProjects = this.projects.reduce((groups, project) => {
        let status = '';
        if (project.status == 1){
         status = 'A faire';
        } else if (project.status == 2){
         status = 'Fait';
        } else if (project.status == 3){
         status = 'Terminé';
        }
        if (!groups[status]) {
          groups[status] = [];
        }
        project.image = 'logos.png';
        groups[status].push(project);
        return groups;
      }, {});
    },
    fetchData() {
      getListProject()
        .then((response) => {
          //console.log(response);
          this.projects = response.data
          this.groupProjectsByStatus();

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

<style src="../../style.css"></style>