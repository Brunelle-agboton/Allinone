<template>
    <div>
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center mb-2 border-bottom">
          <h1>Dashboard</h1>
          <div class="btn-toolbar mb-1 mb-md-0">
            <div class="btn-group me-2">
              <button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
              <button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
            </div>
            <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-1">
              <i class="bi bi-calendar"></i>
              This week
            </button>
          </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'MeetingPage',
};
</script>
<style src="../../style.css"> </style>
