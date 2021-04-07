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
            this.$emit('list', {zipCode: this.zipCode})
            this.zipCode = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        list: [],
        city: [],
        zipCode: "",
        results: {}
    },
    methods: {
        getWeather: function(options) {
            console.log(options)
            axios({
                method: "get",
                url: `https://api.openweathermap.org/data/2.5/forecast`,
                headers: {
                },
                params: {
                    zip: options.zipCode,
                    units: "imperial",
                    appid: API_key
                }
            }).then(response => {
                this.results = response.data
                this.results.list.forEach(forecast => forecast.date = new Date(forecast.dt * 1000))
            })
        }
    }
})
