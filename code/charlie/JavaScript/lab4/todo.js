const getTodoBtn = document.getElementById("get-todo");
const todoInputText = document.getElementById("todo-text");
const compUl = document.getElementById("complete");
const incompUl = document.getElementById("incomplete");


function appendTodo(){
    const inputText = todoInputText.value;

    const finishBtn = document.createElement("button");
    finishBtn.innerText = 'Done';
    finishBtn.addEventListener('click', function(){
        compUl.appendChild(this.parentElement);
        this.parentElement.style.textDecoration = "line-through";
        this.remove();
    })

    const deleteBtn = document.createElement("button");
    deleteBtn.innerText = 'remove';

    deleteBtn.addEventListener('click', function(){
        this.parentElement.remove();
    })

    const tempLi = document.createElement("li");
    tempLi.innerText = todoInputText;
    tempLi.appendChild(deleteBtn);
    tempLi.appendChild(finishBtn);
    incompUl.appendChild(tempLi);
}

getTodoBtn.addEventListener('click', appendTodo);
todoInputText.addEventListener('keyup', function(event){
    if(event.key === 'enter'){
        appendTodo();
    }
})