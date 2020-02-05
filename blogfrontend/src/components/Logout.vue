<template>
    <div></div>
</template>

<script>
    export default {
        name: "Logout",

        created() {
            this.$store.dispatch('destroyToken')
                .then(()=>{
                this.$router.push('/list');
            });
        }
    }
</script>

<style scoped>

</style>