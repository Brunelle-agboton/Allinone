import axios from '../services/caller.service';
import store from '@/store/store';
//import router from '../router';

const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});
axios.defaults.withCredentials = true

export const authenticate = (data) => {
    return apiUrl.post('/login', data, {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
        },
      });
};

export const logout = () => {
  localStorage.removeItem("access_token"); 
  return Promise.resolve();
}

const getToken = () => {
    return localStorage.getItem('access_token');
  }
  
  export const decodeToken = () => {
    const token = getToken();
    try {
      if (!token) {
        // Aucun token disponible
        return null;
      }
      const [headerEncoded, payloadEncoded] = token.split(".");
      if (!headerEncoded || !payloadEncoded) {
        // Le token ne contient pas les parties attendues
        console.error("Le token ne contient pas les parties attendues.");
        return null;
      }
      const header = JSON.parse(atob(headerEncoded));
      const payload = JSON.parse(atob(payloadEncoded));
  
      // Vérification de l'expiration du token
      const currentTimestamp = Math.floor(Date.now() / 1000);
      if (payload.exp && payload.exp < currentTimestamp) {
        console.log("Le token a expiré.");
        clearToken();

        store.commit('clearAuthState');
        return this.$router.push('/auth');
      }
      return { header, payload };
    } catch (error) {
      // Gérer les erreurs de décodage ici
      console.error("Erreur de décodage du token :", error);
      return null;
    }
  };
  
  const saveToken = (token) => {
    localStorage.setItem('access_token', token);
  }
  const clearToken = () => {
    localStorage.removeItem('access_token');
  };
apiUrl;
export const AuthService = {
    getToken, decodeToken, saveToken
  }
  