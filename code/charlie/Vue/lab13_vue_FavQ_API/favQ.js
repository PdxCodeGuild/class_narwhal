// Vue.component('search',{
//     data: function() { 
//         return{

//         }
//     },
//     template:`
    
//     `,
//     props:['']

// })

const vm = new Vue({
    el:'#FavQ',
    data:{
        searchFilter: "",
        userSearch: "",
        results: {}
    },
    methods:{
        searchQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                    keyword: "",
                    filter: `${keyword}`, //"Oscar Wilde",         //`${keyword}`,// having this ---> url: "https://favqs.com/api/quotes&filter=steve+jobs&type=author", is the same as adding "params" to axios.
                    type: this.searchFilter
                }
            }).then(response => {
                this.results = response.data;
            })
            // }).then(function(response) {
            //     this.quotes = response.data;
            // })
        },

        loadQuotes: function(){
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                  // Implementing "0" parameters here returns a random array of quote objects
                }
            }).then(response => {
                this.results = response.data;
            })
        }
    },

    //This is where the list of random quotes is generated from.
    mounted: function(){
            this.loadQuotes();
    }

})
