Vue.component('quote', {
    props: ['quote'],
    template: '<div><p>{{ quote.body }}</p><p><a :href="quote.url">{{ quote.author }}</a></p></div>'
});



const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        search_term: 'Will Rogers',
        search_type: 'author',
        last_page: true,
        page: 1
        //page_number: 
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
        },

        goToNextPage: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.search_term, // "Will Rogers" "Jeff Bezos"
                    type: this.search_type, // keyword author "tag"
                    page: this.results.page + 1,
                    
                }
            }).then(response => {
                this.results = response.data
                this.last_page = response.last_page
                
                
            })
        },

        goToPreviousPage: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.search_term, // "Will Rogers" "Jeff Bezos"
                    type: this.search_type, // keyword author "tag"
                    page: this.results.page - 1
                }
            }).then(response => {
                this.results = response.data
                this.last_page = response.last_page
            })
        }
    },

    mounted: function(){
        this.loadRandom25()
    }
})