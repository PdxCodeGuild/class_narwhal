const Nasa = new Vue({
    el:'#Nasa',
    data:{
        start_date: "",
        end_date: "",
        results: {}
    },
    methods:{
        NEOFeed: function() {
            axios({
                url: "https://api.nasa.gov/planetary/feed",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                    start_date: this.start_date,
                    end_date: this.end_date, 
                }
            }).then(response => {
                this.results = response.data;
            })
        },
        NEOBrowse: function() {
            axios({
                url: "https://api.nasa.gov/neo/rest/v1/neo/browse/",
                method: "get",
                headers:{
                    "Authorization":`Token token="${AK}"`
                },
                params:{
                   
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
