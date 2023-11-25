<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1 client-page">
        <div class="client-list">
            <a href="/cld"><client-card
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
      clients: [
        // Liste de vos clients existants
        {
          name: "Client 1",
          logo: "test.jpeg",
          description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.",
        },
        {
          name: "Client 2",
          logo: "test.jpeg",
          description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.",
        },
        {
          name: "Client 2",
          logo: "test.jpeg",
          description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.",
        },
        {
          name: "Client 2",
          logo: "test.jpeg",
          description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.",
        },{
          name: "Client 2",
          logo: "test.jpeg",
          description: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.",
        },
        // Ajoutez d'autres clients ici
      ],
      isModalVisible: false,
    };
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
          client.logo = "test.jpeg";
          client.description = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam quasi cumque eaque nemo autem voluptatibus.";
          this.clients.push(client)
          });
          console.log(response.data)
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