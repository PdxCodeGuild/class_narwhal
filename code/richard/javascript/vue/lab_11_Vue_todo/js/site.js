var app = new Vue({
    el: '#app',
    data: {
      title: 'Vue todo app by Rich',
      newTodo: '',
      todos: []
    },
    methods: {
      
      addTodo() {
        // console.log(this.newTodo);
        this.todos.push({
          title: this.newTodo,
          done: false
        })
        this.newTodo = "";
      },

      removeTodo(todo) {
        const todoIndex = this.todos.indexOf(todo);
        this.todos.splice(todoIndex, 1);
      }
    }
  })