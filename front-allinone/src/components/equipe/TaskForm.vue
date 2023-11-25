<template>
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <label for="title">Title:</label>
      <input v-model="editedTask.title" id="title" />
  
      <label for="description">Description:</label>
      <textarea v-model="editedTask.description" id="description"></textarea>
  
      <label for="dueDate">Due Date:</label>
      <input type="date" v-model="editedTask.dueDate" id="dueDate" />
  
      <!-- Ajoutez plus de champs de formulaire au besoin -->
  
      <button @click="saveTask">Save</button>
  </div>
  </template>
  
  <script>
  export default {
    name: 'TaskForm',
    props: {
      task: Object,
    },
    data() {
      return {
        editedTask: { ...this.task }, // Créez une copie de la tâche pour éviter la mutation directe
      };
    },
    methods: {
      saveTask() {
        // Gérez la logique de sauvegarde en utilisant this.editedTask
      },
    },
  };
  </script>
  Dans ce code, j'ai ajouté une propriété editedTask dans les données du composant, initialisée avec une copie de la tâche reçue en tant que prop. Vous pouvez ensuite utiliser this.editedTask dans vos méthodes sans modifier directement la prop task. Cette approche vous aidera à éviter la mutation directe des props.
  
  
  
  
  
  
  
  <script>
export default {
  name: 'TaskForm',
  props: {
    task: Object,
  },
  data() {
    return {
      editedTask: { ...this.task }, // Créez une copie de la tâche pour éviter la mutation directe
    };
  },
  methods: {
    saveTask() {
      // Handle saving logic using this.editedTask
    },
    editTask() {
      // Émettez l'événement avec la copie éditée de la tâche
      this.$emit('edit-task', { ...this.editedTask });
    },
    deleteTask() {
      this.$emit('delete-task', this.editedTask.id);
    },
  },
};
</script>

  
  <style scoped>
  .task-form {
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px;
    border-radius: 5px;
  }
  </style>
  