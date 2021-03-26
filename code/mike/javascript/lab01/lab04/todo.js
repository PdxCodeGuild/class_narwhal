let tasksUl = document.getElementById("tasksUl")
let newTasks = document.getElementById("newTasks")
let newTask = document.getElementById("newTask")
let addBt = document.getElementById("addBt")
let completedUl = document.getElementById("completedUl")


function addCallback(event) {
    console.log(event)
    let task = newTask.value
    let liNew = document.createElement('li')
    liNew.innerText = task
    let completeBt = document.createElement('button')
    completeBt.innerText = "Completed"
    completeBt.addEventListener('click', function(){
        console.log(event)
        let completedTask = task
        let liComplete = document.createElement('li')
        liComplete.innerText = completedTask
        let deleteBt = document.createElement('button')
        deleteBt.innerText = "Delete"
        deleteBt.addEventListener('click', function (){
            deleteBt.parentElement.remove()
        })
        liComplete.appendChild(deleteBt)
        completedUl.appendChild(liComplete)
        completeBt.parentElement.remove()
    })
    liNew.appendChild(completeBt)
    tasksUl.appendChild(liNew)

}

addBt.addEventListener('click', addCallback)
newTask.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    console.log(event)
    }
})
