const vm = new Vue({
    el: '#app',
    data: {
        results: {}
    },
    methods: {
        getWeather: function() {
            axios({
                url: "https://openweathermap.org/api",
                method: "get",
                appid: api.openweathermap.org/data/2.5/weather?q={city name}&appid=65ea4eb0a22a297b64ef7411081e98a8,
                params: {
                    
                }
            }).then(response => {
                this.results = response.data
            })
        }
    }
})