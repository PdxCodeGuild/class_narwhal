//user input
let amount = parseInt(prompt('\nEnter amount: '))
let unit_1 = prompt('Enter input unit: ')
let unit_2 = prompt('\nEnter output unit: ')

// conversion table
let convert = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

// multiply
let m_units = convert[unit_1]
let m_solution = units * amount

// divide
let d_units = convert[unit_2]
let d_solution = m_solution / d_units

//prints solution
prompt(`${amount}${unit_1} is `)