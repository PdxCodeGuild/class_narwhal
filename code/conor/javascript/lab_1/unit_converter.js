// Python Lab 9

// Unit Converter

let conv = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254   
}

alert("Welcome to the Unit Converter")

let dist = parseInt(prompt("What is the distance you want to convert? "))

let begin_unit = prompt("What is the starting unit of measurement?\n(ft, mi, m, km, yd, or in) ")
let end_unit = prompt("which unit would you like to convert to?\n(ft, mi, m, km, yd, or in) ")

let value = conv[begin_unit]
let output = value * dist

let inv_value = conv[end_unit]
let inv_output = output / inv_value

alert(`${dist}${begin_unit} is ${inv_output}${end_unit}.`)