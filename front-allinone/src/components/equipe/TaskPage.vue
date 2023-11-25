<template>
  <div class="task">
    <h3>{{ task.title }}</h3>
    <p>{{ task.description }}</p>
    <p>Due Date: {{ task.dueDate }}</p>
    <!-- Add more details as needed -->
    <div>
      <button @click="editTask">Edit</button>
      <button @click="deleteTask">Delete</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TaskPage',
  data() {
    return {
      task: {title: "", description: ""}};
  },
  props: {
    
  },
  methods: {
    editTask() {
      // Handle editing logic
    },
    deleteTask() {
      // Handle deleting logic
    },
  },
};
</script>
<style src="../../style.css"> </style>