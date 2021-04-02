Vue.component('get-quote', {
    data: function() {
        return {
            filter: "",
            type: ""
        }
    },
    template: `
        <div>
        <select v-model="filter">
        <option disabled value="">Please select one</option>
        <option>keyword</option>
        <option>author</option>
        <option>tag</option>
        </select><br>
        <input type="type" placeholder="Enter Search Text Here" @keyup.enter="getQuote" v-model="type"><br>
        <span>Search By: {{ filter }}</span><br>
            <button @click="getQuote" class="btn btn-primary">Get Quote</button>
        </div>
        `,
    methods: {
        getQuote: function() {
            this.$emit('quote', {type: this.type, type: this.filter})
            this.filter = ""
            this.type = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        results: {}
    },
    methods: {
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token=""`
                },
                params: {}
            }).then(response => {
                this.results = response.data
            })
        },
        getQuote: function(quote) {
            this.quotes.push(quote)
        }
    }
})
