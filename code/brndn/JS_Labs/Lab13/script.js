Vue.component('quote-item', {
  data: function() {
    return {
      text: '',
    }
  },
  props: ['quote'],
  template: `<div class="results">
              <h2>{{ quote.body }}</h2>
              <h4>-<a :href="quote.url">{{ quote.author }}</a></h4>
            </div>`,
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
      searchBy: '',
      results: {},
      type: '',
  },
  methods: {
      randomQuotes: function() {
          axios({
              url: "https://favqs.com/api/quotes",
              method: "get",
              headers: {
                  "Authorization": `Token token="939f9918054091444999a7f6b165633d"`
              },
          }).then(response => {
            this.results = response.data
            })
      },
      loadQuotes: function() {
          axios({
              url: "https://favqs.com/api/quotes",
              method: "get",
              headers: {
                  "Authorization": `Token token="939f9918054091444999a7f6b165633d"`
              },
              params: {
                  filter: this.searchBy,
                  type: this.type,
              }
          }).then(response => {
              this.results = response.data
            })
      },
  },
  mounted: function() {
    this.randomQuotes()
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
// })