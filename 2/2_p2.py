input_file = open(r"2\input.txt","r")

game_values = input_file.readlines()

sets_power = 0

for line in game_values:
    parts = line.split(':')
    game_id = parts[0]
    game_id = game_id.replace('Game ','')
    sets = parts[1]
    sets = sets.split(';')
    
    is_valid = True
    red = 0
    green = 0
    blue = 0

    for set in sets:
        set = set.replace('\n','')
        cubes = set.split(',')

        for cube in cubes:
            cube = cube.split(' ')
            cube = cube[1] +","+ cube[2]
            cube = cube.split(',')
            if cube[1] == 'red':
                if int(cube[0]) > red:
                    red = int(cube[0])
            elif cube[1] == 'green':
                if int(cube[0]) > green:
                    green = int(cube[0])
            else:
                if int(cube[0]) > blue:
                    blue = int(cube[0])

    sets_power += red*green*blue

print(sets_power)



