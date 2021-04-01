const vm = new Vue({
    el:'#app',
    data:{
        userSearch = '',
        results: {}
    },
    methods:{
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                    keyword: "",
                    filter: `${keyword}`,// having this url: "https://favqs.com/api/quotes&filter=steve+jobs&type=author", is the same as adding "params" to axios.
                    type: "author"
                }
            }).then(response => {
                this.results = response.data;
            })
            // }).then(function(response) {
            //     this.quotes = response.data;
            // })
        }
    }
    
    
    
})