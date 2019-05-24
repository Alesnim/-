export default new Vuex.Store({
    state: {
        socket: {
            isConnected: false,
            message: '',
            reconnectError: false,
            messagesList: []
        },
    },
    mutations: {
        SOCKET_ONOPEN(state, event) {
            Vue.prototype.$socket = event.currentTarget
            state.socket.isConnected = true
        },
        SOCKET_ONCLOSE(state, event) {
            state.socket.isConnected = false
        },
        MESSAGE_TO_WEBSOCKET(state, message) {
            state.message = message;
        },
    },
    actions: {
        sendMessage: function(context, message) {

            Vue.prototype.$socket.send(message);
            context.state.socket.messagesList.push({
                author: context.state.auth.username,
                content: message
            })
        }
    }
})