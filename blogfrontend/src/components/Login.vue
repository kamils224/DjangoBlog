<template>
 <div class="row justify-content-center">
        <h4 v-if="showFailureMessage" class="bg-danger text-white text-center p-2 my-2">
            Authentication failed. Try again.
        </h4>
        <div class="form-group">
            <label>Username</label>
            <input class="form-control" v-model="$v.username.$model">
            <validation-error v-bind:validation="$v.username" />
        </div>
        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" v-model="$v.password.$model">
            <validation-error v-bind:validation="$v.password" />
        </div>
        <div class="text-center">
            <button class="btn btn-primary" v-on:click="handleAuth">Log in</button>
        </div>
 </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import { mapActions } from "vuex";
import ValidationError  from "./ValidationError";
export default {
    components: { ValidationError },
    data: function() {
        return {
            username: "kamil",
            password: "kamil",
            showFailureMessage: false,
        }
    },
    validations: {
        username: { required },
        password: { required }
    },
    methods: {
        ...mapActions(["authenticate"]),
        async handleAuth() {
            this.$v.$touch();
            if (!this.$v.$invalid) {
                let success = await this.authenticate({ username: this.username,
                    password: this.password });

                if (success) {
                    await this.$router.push("/");
                } else {
                    this.showFailureMessage = true;
                }
            }
        }
     }
  }
</script>

<style scoped>

</style>