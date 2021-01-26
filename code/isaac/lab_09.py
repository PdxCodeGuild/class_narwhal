
Homedep_or = input("What is the length of what you need?  ")

Homedep1_or = input("What are the input units that you looking for?  ")

unit_mea = input("What unit of measurement would you like this in? ") 

total = float(Homedep_or)

conversion_table = {"Ft" : 0.3048, "Mi" : 1609.34, "Met" : 1, "Kilo" : 1000, "Yd" : 0.9144, "In" : 0.0254}

meters = conversion_table[unit_mea]*total 

output =  meters/conversion_table[Homedep1_or]


print(Homedep_or)
print(f"Your conversion in meters is {meters}")
print(f"Your conversion is {output}")