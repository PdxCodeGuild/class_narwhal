// JS Lab1-3 19 Mar 21
// Python Lab11 Simple Calculator


// class Clcultr {
//     constructor(a, b) {
//         this.a = a;
//         this.b = b;

//     }
//     add() {
//         return this.a + this.b;
//     }

//     subtract() {
//         return this.a - this.b;
//     }

//     multiply() {
//         return this.a * this.b;
//     }

//     divide() {
//         return this.a / this.b;
//     }
// }


// let nmbrs = new Clcultr(parseFloat(prompt("#")), parseFloat(prompt("other #")));
// let clcl = nmbrs.${prompt("add, subtract, multipy, divide")}`;
/* 
let clcultr = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
}
*/

let numa = document.getElementById("numa")
let numb = document.getElementById("numb")
let plusBtn = document.getElementById("plus")
let minusBtn = document.getElementById("minus")
let timesBtn = document.getElementById("times")
let divideBtn = document.getElementById("divide")
let results = document.getElementById("results")
let clearBtn = document.getElementById("clear")

plusBtn.addEventListener('click', Clcultr)
minusBtn.addEventListener('click', Clcultr)
timesBtn.addEventListener('click', Clcultr)
divideBtn.addEventListener('click', Clcultr)
clearBtn.addEventListener('click', function() {
    results.innerText = "";
    numa.value = "";
    numb.value = "";
})

function Clcultr(event) {
    let a = parseFloat(numa.value);
    let b = parseFloat(numb.value);
    if (event.target.id == 'plus') {
        var result = a + b;
    } else if (event.target.id == 'minus') {
        var result = a - b;
    } else if (event.target.id == 'times') {
        var result = a * b;
    } else if (event.target.id == 'divide') {
        var result = a / b;
    }
    console.log(numa.textContent);
    numa.value = result;
    numb.value = "";
}
/*
if (opp == "add") {
    clcl = clcultr.add(numa, numb);
} else if (opp == "subtract") {
    clcl = clcultr.subtract(numa, numb);
} else if (opp == "multiply") {
    clcl = clcultr.multiply(numa, numb);
} else if (opp == "divide") {
    clcl = clcultr.divide(numa, numb);
}
*/
/* 
Loop:
while (opp != "quit") {
    
    numa = clcl;
    opp = prompt(`'add' to, 'subtract' from, 'multiply', 'divide' ${numa} \n ('quit' to quit Clcultr)`);
    if (opp == "quit") {
        break Loop;
    }
    numb = parseFloat(prompt(`${opp} what number`));
    
    if (opp == "add") {
        clcl = clcultr.add(numa, numb);
    } else if (opp == "subtract") {
        clcl = clcultr.subtract(numa, numb);
    } else if (opp == "multiply") {
        clcl = clcultr.multiply(numa, numb);
    } else if (opp == "divide") {
        clcl = clcultr.divide(numa, numb);
    }
    
    alert(clcl);
}
*/