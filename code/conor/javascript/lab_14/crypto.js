Vue.component('coin-me', {
    data: function() {
        return {
            filter: ""
        }
    },
    template: `
        <div>
            <div>
                <h3>Which Crypto Coin would you like to Search?</h3>
                <input type="type" placeholder="Enter Search Text Here" @keyup.enter="getCrypto" v-model="filter">
                    <button @click="getCrypto">Search</button>
            </div>
        </div>
        `,
    methods: {
        getCrypto: function() {
            this.$emit('crypto', this.filter)
            this.filter = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        topTenCrypto: [],
        NYSETime: "",
        HomeTime: "",
        displayCoin: ""
    },
    methods: {
        // loadCrypto: function () {
        //     axios({
        //         url: "https://min-api.cryptocompare.com/data/price?",
        //         method: "get",
        //         params: {
        //             tryConversion: true,
        //             fsym: "BTC",
        //             tsyms: "USD,JPY,EUR"
        //         }
        //     }).then(response => {
        //         this.results = response.data
        //     })
        // },
        topTen: function () {
            axios({
                url: "https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10",
                method: "get",
                params: {
                    tsym: "USD"
                }
            }).then(response => {
                this.topTenCrypto = response.data.Data
            })
        },
        searchCoin: function (coinFilter) {
            // console.log(coinFilter)
            this.displayCoin = coinFilter
            axios({
                url: "https://min-api.cryptocompare.com/data/pricemultifull?",
                method: "get",
                params: {
                    tryConversion: true,
                    fsyms: coinFilter,
                    tsyms: "USD,JPY,EUR"
                }
            }).then(response => {
                this.results = response.data.DISPLAY[coinFilter]
                // console.log(response.data)
                // console.log(response.data.DISPLAY)
            })
        }
    },
    mounted: function () {
        // this.loadCrypto()
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