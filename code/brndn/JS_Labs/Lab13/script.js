Vue.component('search-for', {
    data: function() {
      return {
        text: '',
      }
    },
    template: `
    <div>
      <input type="text" placeholder="Search for..." @keyup.enter="searchFor" v-model="text">
      <button @click="searchFor">search</button>
    </div>
    `,
    methods: {
      searchFor: function() {
        this.$emit('add', { text: this.text, id: this.id})
        this.text = ''
      }
    }
  })

const vm = new Vue({
    el: '#app',
    data: {
        results: {}
    },
    methods: {
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="939f9918054091444999a7f6b165633d"`
                },
                params: {
                    filter: this.text,
                }
            }).then(response => {
                this.results = response.data
            })
        }
    }
})

// const axios = require('axios').default;
// Vue.component('quote-item', {
//     },
//     props: ['quote'],
//     template: '<li>{{ quote.text }}</li>'
//     }),
// const vm = new Vue({
//     el: '#app',
//     data: {
//         results: {},
//         searchBy: '',
//     },
//     mounted () {
//         axios
//         .get('https://favqs.com/api/quotes')
//         .header(`Authorization: Token token="939f9918054091444999a7f6b165633d"`)
//         .then(response => {
//             this.results = response.data
//         })
//     },
    // methods: {
    //     loadQuotes: function() {
    //         axios({
    //             url: "https://favqs.com/api/quotes",
    //             method: "get",
    //             headers: {
    //                 "Authorization": `Token token="939f9918054091444999a7f6b165633d"`
    //             },
    //             params: {
    //                 filter: this.searchBy,
    //                 type: "author"
    //             }
    //         }).then(response => {
    //             this.results = response.data
    //         })
    //     }
    // }
})