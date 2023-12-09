input_file = open(r"2\input.txt","r")

game_values = input_file.readlines()

sum_valid_games = 0

for line in game_values:
    parts = line.split(':')
    game_id = parts[0]
    game_id = game_id.replace('Game ','')
    sets = parts[1]
    sets = sets.split(';')
    
    is_valid = True
    
    for set in sets:
        red = 0
        green = 0
        blue = 0
        set = set.replace('\n','')
        cubes = set.split(',')

        for cube in cubes:
            cube = cube.split(' ')
            cube = cube[1] +","+ cube[2]
            cube = cube.split(',')
            if cube[1] == 'red':
                red += int(cube[0])
            elif cube[1] == 'green':
                green += int(cube[0])
            else:
                blue += int(cube[0])
        if red > 12 or green > 13 or blue > 14:
            is_valid = False
            break
    if is_valid:
        sum_valid_games += int(game_id)

print(sum_valid_games)