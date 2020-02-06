export default {
    state: {
        ratio: 0.0,
    },
    getters: {
        getRatio() {
            return this.ratio;
        }
    },
    mutations: {
        setRatio(state, ratio) {
            this.state.ratio = ratio;
        }
    },
    actions: {
    },
}