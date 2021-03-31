/*  Author: Charles Spahn
    Project: Vue.js Todo
    Due Date: Mar. 29, 2021
 */

const vmtodo = new Vue({
    el:'#vmtodo',
    data:{
        newTodo: "",
        completed: false,
        newId: 1,
        todos: []
    },
    methods:{
        addTodo: function(){
            this.todos.push({title: this.newTodo, completed: false, id: this.newId});
            this.newId++;
            this.newTodo = "";
        },
        removeTodo: function(todo){
            console.log(todo);
            console.log("You don't suck!");
            this.todos.splice(this.todos.indexOf(todo), 1);//Remove the item @ "index", deleteCount === 1.
        },
        completeTodo: function(todo){
            //Toggle between true and false for the completed attribute
            //accesing "todos" array with the indexOf function to determine which todo to modify.
            this.todos[this.todos.indexOf(todo)].completed = !this.todos[this.todos.indexOf(todo)].completed;
            //The (not)"!" operator allows for this button to be a toggle.
        }
    },
    computed:{
        incompleteTodos: function(){
            return this.todos.filter(function(todo){
                return todo.completed === false;
            })
        },
        completeTodos: function(){
            return this.todos.filter(function(todo){
                return todo.completed === true;
            })
        }
    }
})
alert("Connected!!");