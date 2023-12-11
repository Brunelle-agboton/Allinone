import axios from '../services/caller.service';


const apiUrl = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});

export const login = (data) => {
    return apiUrl.post('/login', data, {
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
        },
      });
};
const getToken = () => {
    return localStorage.getItem('access_token');
  }
  
  export const decodeToken = () => {
    const token = getToken()
    try {
      if (token) {
        const [headerEncoded, payloadEncoded] = token.split(".");
        const payload = JSON.parse(atob(payloadEncoded));
        return { header: JSON.parse(atob(headerEncoded)), payload };
      } else {
        // Vous pouvez renvoyer `null` ou une structure d'erreur ici
        return null;
      }
    } catch (error) {
      // Gérer les erreurs de décodage ici
      console.error("Erreur de décodage du token :", error);
      // Vous pouvez renvoyer `null` ou une structure d'erreur ici
      return null;
    }
  }
  const saveToken = (token) => {
    localStorage.setItem('access_token', token);
  }

apiUrl;
export const AuthService = {
    getToken, decodeToken, saveToken
  }
  