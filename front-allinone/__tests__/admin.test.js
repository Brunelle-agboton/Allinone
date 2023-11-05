import { mount } from "@vue/test-utils";
import ProjectPage from '../src/components/ProjectPage.vue';

/************************************** Test sur les fonctionnalites projets */
/**Vérifie que le composant ProjectPage se rend correctement sans erreurs. */
describe('ProjectPage', () => {
  it('renders without errors', () => {
    const wrapper = mount(ProjectPage);
    expect(wrapper.exists()).toBe(true);
  });
});

/**Vérifie que la modal s'ouvre et se ferme correctement lorsqu'on appelle les méthodes showModal et closeModal */
it('shows and closes the modal', async () => {
  const wrapper = mount(ProjectPage);
  const showModalButton = wrapper.get('[data-test="mod"]');
  
  // Vérifie que la modal n'est pas visible au départ
  expect(wrapper.findComponent({ name: 'ProjectForm1' }).exists()).toBe(false);

  // Clique sur le bouton pour ouvrir la modal
  await showModalButton.trigger('click');

  // Vérifie que la modal est maintenant visible
  expect(wrapper.findComponent({ name: 'ProjectForm1' }).exists()).toBe(true);

  // Appelle la méthode pour fermer la modal
  await wrapper.vm.closeModal();

  // Vérifie que la modal est fermée
  expect(wrapper.findComponent({ name: 'ProjectForm1' }).exists()).toBe(false);
});
