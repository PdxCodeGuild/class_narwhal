'''
- simple unit converter -
-  lab09 26 jan 20201   -
-    composer: brndn    -
-        v: 1.1         -
'''

#this allows the user to convert a unit from a dict to another unit in the dict

#units in relation to "m"
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

try:
    ans = round(float(number) * conv[unit1] / conv[unit2], 2) #user's number of units converted to "m", then to end unit

    print(f"\n{number}{unit1} = {ans}{unit2}\n")

except ValueError:             #accounts for user entering unit not in the dict
    print("\nInvalid Entry\n")

except KeyError:               #accounts for user entering a non-number for "number"
    print("\nInvalid Entry\n")

