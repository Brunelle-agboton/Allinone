<template>
    <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="row">
      <ListItem v-for="list in lists" :key="list.id" :list="list" class="col-md-3" />
    </div>
    </div>
  </template>
  
  <script>
  import ListItem from "@/components/equipe/List-item.vue";
  import {getProjectsTeam} from '@/services/adminServices'

  export default {
    data() {
      return {
        lists: [
          { id: 3, title: "A faire", tasks: [] },
          { id: 1, title: "En Cours", tasks: [] },
          { id: 2, title: "Termine", tasks: [] },
          { id: 4, title: "Archive", tasks: [] },
        ],
      };
    },
    components: {
      ListItem,
    },
    mounted() {
      const idp = this.router.params.id;
      getProjectsTeam(idp).then((response) => {
        if (response.data == null || response.status != 200) {
          console.log("Erreur de récupération des projets");
          } else {
            const projectData = response.data;
            // Mise à jour des listes en fonction des tâches reçues
            projectData.tasks.forEach((task) => {
              const listIndex = this.lists.findIndex((list) => list.id === task.tasks_status);
              if (listIndex !== -1) {
                this.lists[listIndex].tasks.push({
                  id: task.idtask,
                  description: task.tasks_description,
                });
            }
      });
              }
      });        
    },
  };
  </script>
  <style src="../../style.css"></style>
  