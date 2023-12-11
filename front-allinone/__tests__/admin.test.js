import { mount} from '@vue/test-utils';
import { createApp } from 'vue';
import ProjectPage from '../src/components/admin/ProjectPage.vue';

/************************************** Test sur les fonctionnalites projets */
const app = createApp({});
const localVue = app.use;

// Mocker les méthodes et services nécessaires
jest.mock('@/services/adminServices', () => ({
  getListProject: jest.fn(() => Promise.resolve({ data: [] })),
}));

// Monter le composant pour les tests
const wrapper = mount(ProjectPage, { localVue, global: {
  stubs: ["router-link", "router-view"], // Composants de substitution (`Stubs`) pour router-link et router-view au cas où ils sont affichés dans notre composant
},});

describe('ProjectPage.vue', () => {
  // Teste l'initialisation du composant
  it('Initialise projects a un tableau vide et isModalVisible a false', () => {
    expect(wrapper.vm.projects).toEqual([]);
    expect(wrapper.vm.isModalVisible).toBe(false);
  });  

  // Tester l'ouverture de la modal après l'appel de la méthode showModal
  it('Affiche le modal quand showModal est appelle', async () => {
    await wrapper.vm.showModal();
    expect(wrapper.vm.isModalVisible).toBe(true);
    // Vérifie si la modal est affichée dans le DOM
    expect(wrapper.find('#backdrop').isVisible()).toBe(true);
  });

  // Teste la fermeture de la modal après l'appel de la méthode closeModal
  it('Cache le modal quand closeModal est appelle', async () => {
    await wrapper.vm.closeModal();
    expect(wrapper.vm.isModalVisible).toBe(false);
    // Vérifier si la modal est cachée dans le DOM
    expect(wrapper.find('#backdrop').isVisible()).toBe(false);
  });

});
