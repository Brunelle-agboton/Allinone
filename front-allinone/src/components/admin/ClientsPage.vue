<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1 client-page">
        <div class="client-list">
            <a href="/cld" class="client"><client-card
                v-for="(client, index) in clients"
                :key="index"
                :client="client"
            /></a>
        </div>
      <button @click="showModal" class="btn btn-primary add-button" data-bs-toggle="modal" data-bs-target="#backdrop">Ajouter</button>
      <ClientForm1 v-show="isModalVisible" @close="closeModal" />
    </div>
</template>
<script>
import ClientCard from './ClientCard.vue';
import ClientForm1 from '../_Forms/ClientForm1.vue';
import {getListClient} from '@/services/adminServices';

export default {
  name: 'ClientsPage',
  components: {
      ClientCard,
      ClientForm1,
  },
data() {
    return {
      clients: [],
      isModalVisible: false,
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
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
      getListClient()
        .then((response) => {
          response.data.forEach((client) => {
          client.logo = "icon.png";
          this.clients.push(client)
          });
          // console.log(response.data)
        })
        .catch((error) => {
          console.error(error)
        });
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>

<style src="../../style.css"> </style>