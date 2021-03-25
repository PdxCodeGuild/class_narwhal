let addItem = document.getElementById("addItem")
let addItemBtn = document.getElementById("addItemBtn")
let incomplete = document.getElementById("incomplete")
let complete = document.getElementById("complete")

addItemBtn.addEventListener('click', function() {
    let newItem = document.createElement('li')
    newItem.innerText = addItem.value
    incomplete.appendChild(newItem)

    let checkComp = document.createElement('button')
    checkComp.setAttribute('type', 'button')
    checkComp.innerText = 'Completed'
    newItem.appendChild(checkComp)

    let removeBtn = document.createElement('button')
    removeBtn.setAttribute('type', 'button')
    removeBtn.innerText = 'Remove'
    newItem.appendChild(removeBtn)

    removeBtn.addEventListener('click', function() {
        newItem.remove()
    })

    checkComp.addEventListener('click', function() {
        newItem.remove()

        let completedItem = document.createElement('li')
        completedItem.innerText = addItem.value
        completedItem.style.textDecoration = 'line-through'
        complete.appendChild(completedItem)

        let completeBtn = document.createElement('button')
        completeBtn.setAttribute('type', 'button')
        completeBtn.innerText = 'Remove'
        completedItem.appendChild(completeBtn)

        completeBtn.addEventListener('click', function() {
            completedItem.remove()
        })
    })
})