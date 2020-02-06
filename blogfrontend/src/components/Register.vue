<template>
        <div class="container">
        <div class="row justify-content-center">
            <h4 v-if="showFailureMessage" class="bg-danger text-white text-center p-2 my-2">
                Authentication failed. Try again.
            </h4>
            <div class="col-md-4">
                <div class="form-group">
                    <label>Username</label>
                    <input class="form-control" v-model="$v.username.$model">
                    <validation-error v-bind:validation="$v.username"/>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" class="form-control" v-model="$v.password.$model">
                    <validation-error v-bind:validation="$v.password"/>
                </div>
                <div class="form-group">
                    <label>First name</label>
                    <input class="form-control" v-model="$v.firstName.$model">
                    <validation-error v-bind:validation="$v.firstName"/>
                </div>
                <div class="form-group">
                    <label>Last Name</label>
                    <input class="form-control" v-model="$v.lastName.$model">
                    <validation-error v-bind:validation="$v.lastName"/>
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input class="form-control" v-model="$v.email.$model">
                    <validation-error v-bind:validation="$v.email"/>
                </div>
                <div class="text-center">
                    <button class="btn btn-primary" v-on:click="handleUserCreate">Register</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {required} from "vuelidate/lib/validators";
    import {mapActions} from "vuex";
    import ValidationError from "./ValidationError";
    export default {
        name: "Register",
        components: {ValidationError},
        data: function () {
            return {
                username: "jakisuser",
                password: "password",
                firstName: "John",
                lastName: "Doe",
                email: "email@example.com",
                showFailureMessage: false,
            }
        },
        validations: {
            username: {required},
            password: {required},
            firstName: {required},
            lastName: {required},
            email: {required},
        },
        methods: {
            ...mapActions(["createUser"]),
            async handleUserCreate() {
                this.$v.$touch();
                if (!this.$v.$invalid) {
                    let success = await this.createUser({
                        username: this.username,
                        password: this.password,
                        first_name: this.firstName,
                        last_name: this.last_name,
                        email: this.email,
                    });

                    if (success) {
                        await this.$router.push("/login");
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