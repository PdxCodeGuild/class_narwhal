let clock = setInterval(timeKeeper, 1000)

function timeKeeper() {
    console.log("clock")
    let timeNow = new Date()
    document.getElementById('clock').innerHTML = timeNow.toLocaleString('en-US', { timeZone: 'America/New_York' })
}

const vm = new Vue({
    el: '#app',
    data: {
        results: {"BTC": {"USD":20.00,"EUR":30.50}, 
                  "ETH": {"USD":5.00,"EUR":6.50}} 
     }
})
    // methods: {
    //     loadCrypto: function() {
    //         axios({
    //             url: "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR",
    //             method: "get",
    //             .then(response => {
    //                 this.results = response.data
    //             })
    //         })
    //     }
    // }
