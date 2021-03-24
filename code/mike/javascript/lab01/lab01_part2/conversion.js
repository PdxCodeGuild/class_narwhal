/*
# Measurement for converting distance
measurement = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

print('Welcome to the Unit Converter')

distance = float(input(f'What is the distance? ')) #User inputs distance to convert to meters

measure_from = input('What distance type do you want to input from?\n(ft, mi, m, km, yd, or in)\n') # use the user's input to get the measurement type

measure_to = input('What distance type do you want to output to?\n(ft, mi, m, km, yd, or in)\n')

calc = float(measurement[measure_from] / measurement[measure_to])

print(f'{int(distance)} {measure_from} is {distance * calc:8f} {measure_to}')
*/

let measurement = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254   
}

// alert("Welcome to the Unit Converter")

// let distance = parseInt(prompt("What is the distance? "))

// let measure_from = prompt("What distance type do you want to input from?\n(ft, mi, m, km, yd, or in)\n")
// let measure_to = prompt("What distance type do you want to output to?\n(ft, mi, m, km, yd, or in)\n")
// let calc = (measurement[measure_from] / measurement[measure_to])
// let newCalc = distance * calc.toFixed(4)

// alert(`${distance} ${measure_from} is ${newCalc} ${measure_to}`)

let measureFromInput = document.getElementById("measureFromInput");
let measureToInput = document.getElementById("measureToInput");
let num = document.getElementById("num");
let calcBt = document.getElementById("calcBt");
let result = document.getElementById("result")


calcBt.addEventListener('click', function() {
  // let results = parseFloat(num.value) * parseFloat(umCalc.value)
  let measureFrom = measureFromInput.value
  let measureTo = measureToInput.value
  let umCalc = (measurement[measureFrom] / measurement[measureTo])
  let calc = parseFloat(num.value) * umCalc

  result.innerText = `${num.value}${measureFrom} converts to ${calc.toFixed(4)}${measureTo}`
})


