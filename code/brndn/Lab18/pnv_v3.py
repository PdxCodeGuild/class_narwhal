'''
=-=-= Lab18 04 Feb 2021 =-=-=
=-=- Peaks & Valleys V.2 -=-=
=-=-=- Composer: brndn -=-=-=
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

x = 9

water_volume = 0

print('\n')

while x > 0:
    line = ''
    for i in data:
        if i < x and '\N{CACTUS}' in line:
            line += '\N{DROPLET}'
            water_volume += 1
        elif i < x:
            line += '  '
        elif i >= x:
            line += '\N{CACTUS}'
    print(line)
    x -= 1

print(f'\nWater Volume: {water_volume} water units\n')