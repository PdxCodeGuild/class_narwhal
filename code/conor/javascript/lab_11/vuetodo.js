const app = new Vue({
    el: '#app',
    data: {
      incomplete: [],
      complete: [],
      todoItem: '',
  
    },
    methods: {
      appendList: function() {
        this.incomplete.push(this.todoItem)
        this.todoItem='' 
      },
      deleteBtn: function(index) {
        this.incomplete.splice(index, 1)
      },
      checkOff: function(index) {
        this.complete.push(this.todoItem)
        this.incomplete.splice(index, 1) 
      },
      compltedDeleteBtn: function (index) {
        this.complete.splice(index, 1)
      }
    }
  })