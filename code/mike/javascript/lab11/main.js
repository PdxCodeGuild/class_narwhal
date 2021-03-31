Vue.component('task-item', {
    data: function() {
        return {
            editing: false
        }
    },
    props: ['task'],
    template: `
        <li>
            <template>{{ task.text }}</template>
            <input type="checkbox" v-model="task.completed" class="mx-2">
            <button @click="$emit('remove', task)" class="mx-2 btn btn-secondary btn-sm">Del</button>
        <li>
        `
})

Vue.component('add-task', {
    data: function() {
        return {
            text: "",
            id: 1
        }
    },
    template: `
        <div>
            <input type="text" placeholder="New Task" @keyup.enter="addTask" v-model="text">
            <button @click="addTask" class="btn btn-primary">Add</button>
        </div>
        `,
    methods: {
        addTask: function() {
            this.$emit('add', { text: this.text, completed: false, id: this.id })
            this.id++
            this.text = ""
        }
    },
})


const vm = new Vue({
    el: '#app',
    data: {
        tasks: [],
        text: "",
        id: 1
    },
    methods: {
        addTask: function(task) {
            this.tasks.push(task)
        },
        removeTask: function(task) {
            this.tasks.splice(this.tasks.indexOf(task), 1)
        }
    },
    computed: {
        incompleteTasks: function() {
            return this.tasks.filter(function(task) {
                return task.completed === false
            })
        },
        completeTasks: function() {
            return this.tasks.filter(function(task) {
                return task.completed === true
            })
        }
    },
})