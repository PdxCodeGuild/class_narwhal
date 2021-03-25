//alert("hello rich")  // test

// 1. Selectors
const todoInput = document.querySelector('.todo-input');
const todoButton = document.querySelector('.todo-button');
const todoList = document.querySelector('.todo-list');
const filterOption = document.querySelector('.filter-todo');


// 2. Event Listeners
todoButton.addEventListener('click', addTodo);
todoList.addEventListener('click', deleteCheck);
filterOption.addEventListener('click', filterTodo)


// 3. Functions

function addTodo(event) {
    // Prevent the form from submitting
    event.preventDefault(); 
    // Create a Todo DIV
    const todoDiv = document.createElement('div');
    todoDiv.classList.add("todo");
    // Create an LI
    const newTodo = document.createElement('li');
    newTodo.innerText = todoInput.value;
    newTodo.classList.add('todo-item');
    todoDiv.appendChild(newTodo);
    // Create a Checkmark button
    const completedButton = document.createElement('button');
    completedButton.innerHTML = '<i class="fas fa-check"></i>';
    completedButton.classList.add("complete-btn");
    todoDiv.appendChild(completedButton);
    // Create a trash button
    const trashButton = document.createElement('button');
    trashButton.innerHTML = '<i class="fas fa-trash"></i>';
    trashButton.classList.add("trash-btn");
    todoDiv.appendChild(trashButton);
    // Append all the things above to the list
    todoList.appendChild(todoDiv);
    // clear out todo input value
    todoInput.value = "";
}


function deleteCheck(event) {
    // alert("working")
    const item = event.target;

    // delete the todo
    if(item.classList[0] === "trash-btn") {
        item.parentNode.remove();
    }

    // check mark - mark done
    if(item.classList[0] === "complete-btn") {
        const todo = item.parentElement;
        todo.classList.toggle("completed");
    }
}


function filterTodo(event) {
    //alert("filter todo working");
    const todos = todoList.children; // children   .slice(1:)
    console.log(todos);
    //todos.forEach(function(todo) {   // rewrite to be a for loop  change to todos[i]
    // let todo;
    for (let i = 0; i < todos.length; i++) {
        console.log(todos[i]);
        switch(event.target.value) {
            case "all": 
                todos[i].style.display = 'flex';
                console.log("all")
                break;
            case "completed":
                console.log("completed")
                if (todos[i].classList.contains('completed')){
                    todos[i].style.display = 'flex';
                } else {
                    todos[i].style.display = 'none';
                }
                break;
            case "uncompleted":
                console.log("uncompleted")
                if (!todos[i].classList.contains('completed')) {
                    todos[i].style.display = 'flex';
                } else {
                    todos[i].style.display = 'none';    
                }
                break;
        }
    };
}

