 



const vm = new Vue({
    el: '#app',
    data: {
        variables:   {
            "data": [
              {
                "Passenger Class": "First",
                "Sex": "female",
                "Age": 22,
                "Sibling_Spouse": 1,
                "Parent_Child": 0,
                "Fare": 7.25,
                "Cabin": "Unknown",
                "Embarked": "Southampton",
                "Cabin Class": "U",
                "Title": "Mr",
                "Title Type": "Adult",
                "Family Size": 2,
                "Family Size_category": "Couple",
                "Fare_category": 1,
                "Age_category": "adult - young"
              }
            ]
          },
        prediction: {},
    },
    
    methods: {
        generatePrediction: function() {
            axios({
                url: "https://go.rapidminer.com/am/api/deployments/464d78e9-f21c-48cb-91fa-b638cf8b565e",
                method: "post",
                data: this.variables,
            }).then(response => {
                //response.data = 100 * response.data
                this.prediction = response.data
            })
        },
    },

    mounted: function(){
        this.generatePrediction()
    }


})


