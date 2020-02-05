import Axios from "axios";
const loginUrl = 'http://127.0.0.1:8000/api-token-auth/';

export default {
    state: {
        jwt: localStorage.getItem('access_token') || null,
    },
    getters:{
        authenticatedAxios(state){
            return Axios.create({
                headers: {
                    "Authorization": `Token ${state.jwt}`
                }
            })
        },
        loggedIn(state){
            return state.jwt!=null;
        }
    },
    mutations:{
        setAuthenticated(state, token){
            localStorage.setItem('access_token', token);
            this.state.auth.jwt = token;
        },
        clearAuthentication(state){
            state.jwt=null;
            localStorage.removeItem('access_token');
        }
    },
    actions:{
        destroyToken(context){
            if(context.getters.loggedIn){
                context.commit('clearAuthentication');
            }
        },
        async authenticate(context, credentials){
            try {
                let response = await Axios.post(loginUrl, credentials);
                if (response.statusText === "OK"){

                    context.commit("setAuthenticated", response.data.token);
                return true;
            }
            return false;
            }catch{
                return false;
            }

        }
    },




}