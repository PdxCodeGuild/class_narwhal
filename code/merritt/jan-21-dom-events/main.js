let num1 = document.getElementById("num1")
let num2 = document.getElementById("num2")
let calcBtn = document.getElementById("calc")
let resultsUl = document.getElementById("results")
let clearBtn = document.getElementById("clear")

// function callback(event) {
//     // console.log(event)
//     let result = parseFloat(num1.value) + parseFloat(num2.value)

//     resultsUl.innerText = result
// }

// num1.addEventListener('input', callback)
// num2.addEventListener('input', callback)
document.body.addEventListener('mousemove', function(event) {
    console.log(event.x, event.y)
})

function addCallback(event) {
    // console.log(event)
    let result = parseFloat(num1.value) + parseFloat(num2.value)

    let li = document.createElement('li')
    li.innerText = result

    let btn = document.createElement('button')
    btn.innerText = "-"
    btn.addEventListener('click', function() {
        btn.parentElement.remove()
    })

    li.appendChild(btn)
    resultsUl.appendChild(li)
}

calcBtn.addEventListener('click', addCallback)
num1.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    }
})
num2.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    }
})

// calcBtn.addEventListener('click', function(event) {
//     // console.log(event)
//     let result = parseFloat(num1.value) + parseFloat(num2.value)

//     let li = document.createElement('li')
//     li.innerText = result

//     let btn = document.createElement('button')
//     btn.innerText = "-"
//     btn.addEventListener('click', function() {
//         btn.parentElement.remove()
//     })

//     li.appendChild(btn)
//     resultsUl.appendChild(li)
// })

clearBtn.addEventListener('click', function() {
    resultsUl.innerHTML = ""
})