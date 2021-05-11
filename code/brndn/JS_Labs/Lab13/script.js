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
        page: '1',
        show: false,
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
                this.show = false
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
                    page: this.page,
                }
            }).then(response => {
                  this.results = response.data
                  this.show = true
                  console.log(this.results)
            })
        },
        pageDown: function() {
            var newPage = Number(this.page)
            if (newPage > 1) {
                newPage -= 1
                this.page = String(newPage)
                this.loadQuotes()
            } 
        },
        pageUp: function() {
            var newPage = Number(this.page)
            newPage += 1
            this.page = String(newPage)
            this.loadQuotes()
        },
    },
    mounted: function() {
        this.randomQuotes()
    }
})