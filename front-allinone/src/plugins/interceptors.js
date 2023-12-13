import {AuthService} from "../services";

export default ({ app: { $axios }, res }) => {

    $axios.setHeader('Content-Type', 'application/json');
    $axios.setHeader('X-Requested-With', 'XMLHttpRequest');

    $axios.interceptors.request.use(function (config) {

        const token = AuthService.getToken()
        if (token) {
            config.headers = {"Authorization": "Bearer " + token};
            console.log(config.headers);
        }

        return config;
    }, function (error) {
        return Promise.reject(error);
    });

    $axios.interceptors.response.use(function (response) {
        if (response.headers.authorization) {
            const token = response.headers.authorization.split('Bearer ');
            if (process.server) {
                res.setHeader('Set-Cookie', `token_mysite=${token[1]}; Path=/`)
            } else {
                //const cookies = new Cookies();
                //cookies.set('token_mysite', token, { path: '/' });
            }
        }

        return response;
    }, function (error) {
        if (error.response.status === 401) {
            //this.$store.commit('user/logout');
        }

        return Promise.reject(error);
    });

}
