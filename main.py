# import colorgram
from turtle import Turtle, Screen
from colours import colours
import random as rand

# REQUIREMENTS OF PROJECT
# 10x10 grid
# randomly coloured grid of dots (20px) wide spaced by 50px gap in between

# create our Screen object
scr = Screen()
scr.colormode(255) # change to support rbg 255 color coding

# create out Turtle object
dotty = Turtle()
dotty.speed("fastest")

# instantiate main variables
dot_size = 20
gap_size = 50
dot_grid_count = 10

# we want to start out drawing from the bottom left.
starting_x_pos = -(((dot_grid_count-1)/2 * dot_size) + ((dot_grid_count-1)/2 * gap_size))
starting_y_pos = starting_x_pos

print(f"({starting_x_pos},{starting_y_pos})")

dotty.penup() # no drawing lines
dotty.goto(starting_x_pos, starting_y_pos) # move turtle to starting point

def move_x():
    """
    Will get the current position of the turtle and create a new position for it to be moved to
    :return: the new position coordinates as a tuple (x, y)
    """
    current_pos_x = dotty.pos()[0]
    current_pos_y = dotty.pos()[1]
    new_pos_x = current_pos_x + dot_size + gap_size
    new_pos = (new_pos_x, current_pos_y)
    return new_pos

def move_y_reset_x():
    """
    Resets the x position to the starting x position, but moves up 1 y space (dot size + gap_size)
    :return: the new position coordinates as a tuple (x,y)
    """
    current_pos_y = dotty.pos()[1]
    new_pos_y = current_pos_y + dot_size + gap_size
    new_pos = (starting_x_pos, new_pos_y)
    return new_pos

# execution of the drawing
# using a nested for loop we can draw each dot
for y in range(0, dot_grid_count):
    for x in range(0, dot_grid_count):
        dotty.dot(20, rand.choice(colours))
        dotty.goto(move_x())
    dotty.goto(move_y_reset_x())

# close screen only on click (prevents screen flashing on once and then off fairly instantaneously
scr.exitonclick()







# COLORGRAM.PY
# Extract 6 colors from an image.
# colors = colorgram.extract('/Users/ckritikos/Documents/Screenshots/hirst.png', 30)
#
# colors_list = []
# for x in range(0, len(colors)):
#     color_obj = colors[x]
#     #print(color_obj.rgb)
#     red = color_obj.rgb[0]
#     green = color_obj.rgb[1]
#     blue = color_obj.rgb[2]
#     color_tuple = (red, green, blue)
#     colors_list.append(color_tuple)
# print(colors_list)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s


