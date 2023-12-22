<template>
    <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="row">
      <ListItem v-for="list in lists" :key="list.id" :list="list" class="col-md-3" />
    </div>
    </div>
  </template>
  
  <script>
  import ListItem from "@/components/equipe/List-item.vue";
  
  export default {
    data() {
      return {
        lists: [
          { id: 1, title: "To Do", tasks: [] },
          { id: 2, title: "In Progress", tasks: [] },
          { id: 3, title: "Done", tasks: [] },
          { id: 3, title: "Archived", tasks: [] },
        ],
      };
    },
    components: {
      ListItem,
    },
  };
  </script>
  <style src="../../style.css"></style>
  