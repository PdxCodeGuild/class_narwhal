Vue.component('get-weather',{
    data: function() {
        return {
            zipCode: "",
        }
    },
    template: `
        <div>
        <input type="text" placeholder="Enter Zip Code" @keyup.enter="getWeather" v-model="zipCode"><br>
        <button @click="getWeather" class="btn btn-primary">Get Weather</button>
        </div>
        `,
    methods: {
        getWeather: function() {
            console.log()
            this.$emit('result', {zipCode: this.zipCode})
            this.zipCode = ""
        }
    }
})


const vm = new Vue({
    el: '#app',
    data: {
        zipCode: "",
        image: "http://openweathermap.org/img/wn/10d@2x.png",
        results: {}
    },
    methods: {
        getWeather: function(location) {
            console.log(location)
            axios({
                method: "get",
                url: `https://api.openweathermap.org/data/2.5/weather`,
                params: {
                    zip: location.zipCode,
                    units: "imperial",
                    appid: API_key
                }
            }).then(response => {
                this.results = response.data
                this.results.date = new Date(this.results.dt * 1000).toDateString("en")
                this.results.image = `http://openweathermap.org/img/wn/${this.results.weather[0].icon}@2x.png`
            }).catch(error => {
                console.log(error)
            })
        },
    }
})
