//alert("hello rich")  // test

// 1. Selectors
const todoInput = document.querySelector('.todo-input');
const todoButton = document.querySelector('.todo-button');
const todoList = document.querySelector('.todo-list');


// 2. Event Listeners
todoButton.addEventListener('click', addTodo);

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