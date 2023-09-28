<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-2 flex-1">
        <div class="client-list">
            <a href="/cld"><client-card
                v-for="(client, index) in clients"
                :key="index"
                :client="client"
            /></a>
        </div>
      <button @click="addNewClient" class="btn btn-primary add-button">Ajouter</button>
    </div>
</template>
<script>
import ClientCard from './ClientCard.vue';

export default {
  name: 'ClientsPage',
components: {
    ClientCard,
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
    };
  },
  methods: {
    addNewClient() {
      // Ajoutez la logique pour ajouter un nouveau client à la liste
      // par exemple, en poussant un nouvel objet client dans le tableau this.clients
    },
  },
};
</script>

<style scoped>
/* Styles pour la liste de clients */
.client-list {
  margin: 5em;
  flex-wrap: wrap;
  justify-content: center;
}
a {
    display: flex;
    flex-wrap: wrap;
    list-style: none;
    text-decoration: none;
}
.add-button {
    display: flex;
    margin-left: 74em;
    margin-top: 10px;
    align-self: flex-end;
    background-color: #002060;
  }
</style>