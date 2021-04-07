const vm = new Vue({
    el:'#Nasa',
    data:{
        start_date: "",
        end_date: "",
        APOD: {},
        NEOResults: {},
        results: {}

    },
    methods:{
        NEOFeed: function() {
            axios({
                url: "https://api.nasa.gov/neo/rest/v1/feed",
                method: "get",
                headers:{

                },
                params:{
                    "start_date": this.start_date,
                    "end_date": this.end_date, 
                    "api_key" : `${AK}` 
                }
            }).then(response => {
                this.NEOResults = response.data;
                console.log(this.NEOResults);
            })
        },
        NEOBrowse: function() {
            axios({
                url: "https://api.nasa.gov/neo/rest/v1/neo/browse",
                method: "get",
                headers:{

                },
                params:{
                    "api_key" : `${AK}` 
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

                },
                params:{
                    "api_key" : `${AK}` 
                }
            }).then(response => {
                this.APOD = response.data;
                console.log(response.data);
            })
        }
    },
    //This is where the Astronomy Picture Of the Day is generated from.
    mounted: function(){
            this.loadAPOD();
    }

})
