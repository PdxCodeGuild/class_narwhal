var app = new Vue({
    el: '#app',
    data: {
      title: 'Vue todo app by Rich',
      newTodo: ''
    },
    methods: {
      addTodo() {
        console.log(this.newTodo);

      }
    }
  })