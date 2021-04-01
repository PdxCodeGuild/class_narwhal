const vm = new Vue({
    el: '#app',
    data: {
        //random25: {},
        results: {},
        search_term: 'Jeff Bezos',
        search_type: 'author'
    },
    methods: {
        loadRandom25: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
            }).then(response => {
                this.results = response.data
            })
        },
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.search_term, // "Will Rogers" "Jeff Bezos"
                    type: this.search_type // keyword author "tag"
                }
            }).then(response => {
                this.results = response.data
            })
        }
    },

    mounted: function(){
        this.loadRandom25()
    }
})