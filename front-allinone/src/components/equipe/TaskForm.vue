<template>
  <div class="modal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <form @submit.prevent="saveTask">
          <div class="form-group">
            <label for="title">Title:</label>
            <input v-model="editedTask.title" class="form-control" id="title" />
          </div>
          <div class="form-group">
            <label for="description">Description:</label>
            <textarea v-model="editedTask.description" class="form-control" id="description"></textarea>

          </div>
          <div class="form-group">
            <label for="dueDate">Due Date:</label>
            <input type="date" v-model="editedTask.dueDate"  class="form-control" id="dueDate" />
          </div>
          <div class="row" style="justify-content:end; margin-top: 6px;">
            <button type="button" class="btn btn-secondary col-3" @click="closeModal">close</button>
            <button type="submit" class="btn btn-primary col-3">Edit</button>
          </div>
        </form>
      </div>
    </div>
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
      isModalVisible: true,
      editedTask: { ...this.task },
    };
  },
  methods: {
    closeModal(){
      this.isModalVisible = false;
    },
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
  <style>

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
}
  </style>
  