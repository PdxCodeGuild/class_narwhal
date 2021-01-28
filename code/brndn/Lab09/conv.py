conv = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": .9144,
    "in": .0254
}

unit1 = input("\nConvert: ft, mi, m, km, yd, or in?\n>>> ")
number = input(f"\nHow many {unit1}?\n>>> ")
unit2 = input(f"\nConvert {number} {unit1} to: ft, mi, m, km, yd, or in?\n>>> ")

ans = float(number) * conv[unit1] / conv[unit2]

print(f"\n{number}{unit1} = {ans}{unit2}\n")