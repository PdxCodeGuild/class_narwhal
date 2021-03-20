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

numa = parseFloat(prompt("number"));
opp = prompt("add, subtract, multiply, divide");
numb = parseFloat(prompt("other number"));

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