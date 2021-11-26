import os
import random
import readchar

POS_X = 0
POS_Y = 1
NUM_MAP_OBJETCS = 11

obstacle_definition = """\
#######       ######
                    
####          ##  ##
####     #######  ##
######            ##
           ####     
           ####                
           ####     
######             #
           ####     
           ####                
           ####     
####          ##  ##
####     #######  ##
######            ##\
"""

my_position = [3, 1]
tail_length = 0
tail = []
map_objets = []

end_game = False
died = False

# Create obstacle map

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

LONG_X = len(obstacle_definition[0])
LONG_Y = len(obstacle_definition)


#Main loop
while not end_game:
    os.system("cls")
    # Generate random map objets
    while len(map_objets) < NUM_MAP_OBJETCS:
        new_position = [random.randint(0, LONG_X - 1), random.randint(0, LONG_Y - 1)]

        if new_position not in map_objets and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objets.append(new_position)

    print("+" + "-" * (LONG_X * 2) + "+")

    for coordinate_y in range(LONG_Y):
        print("|", end="")
        for coordinate_x in range(LONG_X):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_objet in map_objets:
                if map_objet[POS_X] == coordinate_x and map_objet[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_objet

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell:
                    map_objets.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[coordinate_y][coordinate_x] == " #":
                char_to_draw = " #"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * (LONG_X * 2) + "+")
    print("La cola {}".format(tail))

    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % LONG_Y]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % LONG_Y]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % LONG_X, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % LONG_X, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position[POS_Y] = new_position

    os.system("cls")

if died == True:
    print("HAS MUERTO")