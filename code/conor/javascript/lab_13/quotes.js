Vue.component('quote-me', {
    data: function() {
        return {
            filter: "",
            type: ""
        }
    },
    template: `
        <div>
            
        </div>
        `,
    methods: {
        getQuote: function() {
            this.$emit('quote', {type: this.type, filter: this.filter})
            this.filter = ""
            this.type = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        filter: "",
        type: "",
        results: {}
    },
    methods: {
        quoteMe: function(options) {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token=""`
                },
                params: {
                    filter: options.filter,
                    type: options.type,
                }
            }).then(response => {
                this.results = response.data
            })
        },
    }
})