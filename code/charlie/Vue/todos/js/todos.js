let vmtodo = new Vue({
    el:'#vmtodo',
    data:{
        newTodo: '',
        completed: false,
        todos: []
    },
    methods:{
        addTodo: function(){
            this.todos.push({
                title: this.newTodo,
                completed: false,
            })
        },
        removeTodo: function(index){
            console.log(index)
            console.log("You don't suck!")
            this.todos.splice(index, 1)
        },
        completeTodo: function(index){
            this.todos[index].completed = !this.todos[index].completed;
        }
    }
})

alert("Connected!!");