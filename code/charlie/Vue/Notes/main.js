let vm = new Vue({
    el: '#app',
    data: {
      message: 'Test_1 === Hello Vue!'
    }
  })
  
let app2 = new Vue({
el: '#app-2',
data: {
    message: 'You loaded this page on ' + new Date().toLocaleString()
}
})

let app3 = new Vue({
    el: '#app-3',
    data:{
        seen:true
    }
})

let app4 = new Vue({
    el:'#app-4',
    data:{
        todos:[
            {text: 'Learn Javascript'},
            {text: 'Learn Vue'},
            {text: 'Build something grandiose'}
        ]        
    }
})

let app5 = new Vue({
    el: '#app-5',
    data: {
      message: 'I love elif'
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
      }
    }
  })

let app6 = new Vue({
el: '#app-6',
data: {
    message: 'Hello Vue!'
}
})

let app7 = new Vue({
  el: '#app-7',
  data: {
    message: '!efil ot yek eht si cisuMusic is the key to life!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  },
  computed:{
    reversedMessage: function(){
      return this.message.split('').reverse().join('')
    }
  }
})
