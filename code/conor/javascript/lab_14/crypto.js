
const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        topTenCrypto: [],
        NYSETime: "",
        HomeTime: ""
    },
    methods: {
        loadCrypto: function () {
            axios({
                url: "https://min-api.cryptocompare.com/data/price?api_key=",
                method: "get",
                params: {
                    tryConversion: true,
                    fsym: "BTC",
                    tsyms: "USD,JPY,EUR"
                }
            }).then(response => {
                this.results = response.data
            })
        },
        topTen: function () {
            axios({
                url: "https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&api_key=",
                method: "get",
                params: {
                    tsym: "USD"
                }
            }).then(response => {
                this.topTenCrypto = response.data.Data
            })
        }
    },
    mounted: function () {
        this.loadCrypto()
        this.topTen()

        const timeKeeper = ()=> {
            
            console.log("clock")
            let timeNow = new Date()
            this.NYSETime = timeNow.toLocaleString('en-US', { timeZone: 'America/New_York' })
            this.HomeTime = timeNow.toLocaleString()
        }
        let clock = setInterval(timeKeeper, 1000)
    }
})