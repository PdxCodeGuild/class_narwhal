const Nasa = new Vue({
    el:'#Nasa',
    data:{
        searchFilter: "",
        userSearch: "",
        results: {}
    },
    methods:{
        searchAPOD: function() {
            axios({
                url: "https://api.nasa.gov/planetary/apod",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                    keyword: "",
                    filter: `${keyword}`, 
                    type: this.searchFilter
                }
            }).then(response => {
                this.results = response.data;
            })
        },

        loadAPOD: function(){
            axios({
                url: "https://api.nasa.gov/planetary/apod",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                  
                }
            }).then(response => {
                this.results = response.data;
            })
        }
    },

    //This is where the Astronomy Picture Of the Day is generated from.
    mounted: function(){
            this.loadAPOD();
    }

})
