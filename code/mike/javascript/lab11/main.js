new Vue({
    el: '#taskList',
    data: {
        newTask: '',
        tasks: [
            'Task 1',
            'Task 2'
        ]
    },
    methods: {
        addTask: function() {
            this.tasks.push(this.newTask);
        },
        deleteBt: function(index) {
            this.tasks.splice(index, 1);
        }
    }
})