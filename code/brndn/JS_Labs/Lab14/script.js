const cityInput = document.getElementById('input-city');
const vm = new Vue({
    el: '#app',
    data: {
        location: '',
        overcast: '', 
        currentTemp: '',
        minTemp: '',
        maxTemp:'',
        sunrise: '',
        sunset: '',
        pressure: '',
        humidity: '',
        wind: '',
    },
    methods: {
        getWeather() {
            console.log(this.location);
            let url = 'http://api.openweathermap.org/data/2.5/weather?q='+this.location+'&units=imperial&APPID=65ea4eb0a22a297b64ef7411081e98a8';
            axios
                .get(url)
                .then(response => {
                    this.overcast = response.data.weather[0].description;
                    this.currentTemp = response.data.main.temp;
                    this.minTemp = response.data.main.temp_min;
                    this.maxTemp = response.data.main.temp_max;
                    this.sunrise = new Date(response.data.sys.sunrise*1000).toLocaleTimeString("en-US").slice(0,4);
                    this.sunset = new Date(response.data.sys.sunset*1000).toLocaleTimeString("en-US").slice(0,4);
                    this.pressure = response.data.main.pressure;
                    this.humidity = response.data.main.humidity + '%';
                    this.wind = response.data.wind.speed + 'm/s';
        })
        .catch(error => {
            console.log(error);
        });
      },
    },
    beforeMount() {
        this.getWeather();
    },
  });