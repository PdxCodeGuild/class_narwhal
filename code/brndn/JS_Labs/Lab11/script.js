const vm = new Vue({
    el: '#toDoApp',
    data: {
        newDo: '',
        toDos: [],
        newID: 0,
        editing: false,
    },
    computed: {
        incomplete: function() {
            return this.toDos.filter(function(todo) {
                return todo.completed === false
            })
        },
        complete: function() {
            return this.toDos.filter(function(todo) {
                return todo.completed === true
            })
        },
    },
    methods: {
        addDo: function() {
            this.toDos.push({text: this.newDo, completed: false, id: this.newID, editing: false})
            this.newID++
            this.newDo = ''
        },
        removeDo: function(todo, event) {
            this.toDos.splice(this.toDos.indexOf(todo), 1);
        },
        clearDo: function() {
            this.toDos = []
        },
        editDo: function(todo, event) {
            todo.editing = todo.editing ? false : true
        },
    }
})