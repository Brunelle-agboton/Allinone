<template>
    <div>
      <div class="container">
          <div class="row">
            <div v-for="(group, status) in groupedProjects" :key="status" class="card border rounded">
              <h2>{{ status }}</h2>
              <div class="card-body">
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
                      ></button>
                    </div>
                    <div class="carousel-inner ">
                      <div
                        v-for="(project, projectIndex) in group"
                        :key="projectIndex"
                        class="carousel-item"
                        :class="{ active: projectIndex === 0 }"
                      >
                        <img :src="require(`@/assets/${project.image}`)" alt="Project Slide" class="card-img">
                        <div class="carousel-caption d-none d-md-block card-body mt-20">
                          <h5>{{ project.title }}  {{ group.length }}</h5>
                          <h6>{{ project.text }}</h6>
                        </div>
                      </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                      <span class="carousel-control-next-icon" aria-hidden="true"></span>
                      <span class="visually-hidden">Next</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'DashboardPage',
  data() {
    return {
      projects: [
      {
        id: 1,
        title: 'Projet 1',
        status: 'En cours',
        text:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.',
        image: 'test.jpeg',
      },
      {
        id: 2,
        title: 'Projet 2',
        status: 'Terminé',
        text:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.',
        image: 'test.jpeg',
      },
      {
        id: 3,
        title: 'Projet 3',
        status: 'closed',
        text:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.',
        image: 'test.jpeg',
      },
      {
        id: 4,
        title: 'Projet 4',
        status: 'En cours',
        text:'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.',
        image: 'test.jpeg',
      },    
      ],
      groupedProjects: {}, 
    }
  },
  created() {
    // Regroupez les projets par statut au moment de la création du composant
    this.groupProjectsByStatus();
  },
  mounted() {
  },
  
  methods: {
    groupProjectsByStatus() {
      // Regroupez les projets par statut
      this.groupedProjects = this.projects.reduce((groups, project) => {
        const status = project.status;
        if (!groups[status]) {
          groups[status] = [];
        }
        groups[status].push(project);
        return groups;
      }, {});
    },
  }
};
</script>

<style scoped>
.card {
  border: 10 solid #002060 !important;
  width:20rem;
  height: 70vh;
  margin-left: 50px;
  margin-top: 50px;
  margin-bottom: 50px;
  justify-content: right;
  background: #002060;

}
.container .row {
  margin-left: 10em;
  justify-content: center;
}
</style>