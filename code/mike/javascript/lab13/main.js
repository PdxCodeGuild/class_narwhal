Vue.component('get-quote', {
    data: function() {
        return {
            filter: "",
            type: ""
        }
    },
    template: `
        <div>
        <select v-model="type">
        <option disabled value="">Please select one</option>
        <option>keyword</option>
        <option>author</option>
        <option>tag</option>
        </select><br><br>
        <input type="type" placeholder="Enter Search Text Here" @keyup.enter="getQuote" v-model="filter"><br>
        <span>Search By: {{ filter }}</span><br><br>
            <button @click="getQuote" class="btn btn-primary">Get Quote</button>
        </div>
        `,
    methods: {
        getQuote: function() {
            this.$emit('quote', {type: this.type, filter: this.filter})
            this.filter = ""
            this.type = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        filter: "",
        type: "",
        results: {}
    },
    methods: {
        getQuote: function(options) {
            console.log(options)
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: options.filter,
                    type: options.type,
                }
            }).then(response => {
                this.results = response.data
            })
        },
    }
})
