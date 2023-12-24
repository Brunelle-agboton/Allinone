<template>
  <div class="list-container">
    <div class="card li-card">
      <div class="card-header li-title">{{ list.title }}</div>
      <div class="card-body">
        <ul class="list-group list-group-flush">
          <li v-for="task in list.tasks" :key="task.id" class="list-group-item li-li" @click="handleTaskClick(task)">
            <button type="button" @click="showModal(task)" data-test="mod" class="add-task">{{ task.description }}
            </button>
          </li>
        </ul>
        <div v-if="isAddingTask">
          <div class="mb-3">
            <textarea v-model="newTask" @keyup.enter="addTask" class="form-control" placeholder="Nouvelle tâche" ></textarea>
          </div>
          <div class="mb-3">
            <label for="dueDate">Expire le :<input type="date" v-model="dueDate"  class="form-control" id="dueDate" /></label>
            
          </div>
        </div>
      </div>
      <div class="card-footer text-center">
        <div v-if="!isAddingTask">
          <button @click="toggleAddingTask" class="btn btn-primary"><i class="bi bi-plus"></i></button>
        </div>
        <div v-else>
          <div class="row" style="margin: 5px;">
            <button @click="addTask" class="btn btn-success col-6">Ajouter</button>
            <button @click="toggleAddingTask" class="btn-close col-6">Fermer</button>
          </div>
        </div>
      </div>
    </div>
    <TaskForm :class="{ 'is-active': isModalVisible }" :task="selectedTask"/>

  </div>
</template>

<script>
import TaskForm from "@/components/equipe/TaskForm.vue";
//import {addTask} from "@services/adminServices";

export default {
  name: 'List-item',
  props: {
    list: {},
  },
  components: {
    TaskForm,
  },
  data() {
    return {
      isAddingTask: false,
      newTask: "",
      dueDate: '',
      isModalVisible: false,
      selectedTask: null,
    };
  },
  computed: {
  },
  methods: {
    showModal(task) {
      this.selectedTask = task;
      this.isModalVisible = true;
    },
    closeModal() {
        this.isModalVisible = false;
      },
    toggleAddingTask() {
      this.isAddingTask = !this.isAddingTask;
      if (!this.isAddingTask) {
        // Réinitialiser le champ lorsque l'utilisateur annule l'ajout
        this.newTask = "";
      }
    },
    handleTaskClick() {
      // Gérer le clic sur une tâche existante
    },
    editTask() {
      this.$emit('edit-task', this.list);
    },
    deleteTask() {
      this.$emit('delete-task', this.list);
    },
    addTask() {
      if (this.newTask.trim() !== "") {
        // Créez une copie de la liste avant d'apporter des modifications
        const updatedList = { ...this.list };
        updatedList.tasks.push({ added_at: Date.now(), description: this.newTask, finished_at: this.dueDate});

        // Émettez l'événement avec la liste mise à jour
        this.$emit('update-list', updatedList);

        // Réinitialisez le champ newTask
        this.toggleAddingTask();
        this.newTask = "";
      }
    },

  },
};
</script>
<style src="../../style.css"></style>
  