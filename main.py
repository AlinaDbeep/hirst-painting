#getting the colors from a picture with colorgram

# import colorgram
# colors = colorgram.extract('picture.jpg', 30)


# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
    
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)



color_list = [(248, 233, 214), (126, 176, 167), (207, 241, 237), (217, 234, 238), (83, 110, 106), (40, 47, 57), (71, 96, 105), (247, 205, 212), (242, 160, 179), (88, 155, 137), (216, 134, 160), (151, 217, 185), (125, 174, 183), (221, 73, 126), (40, 53, 48), (141, 68, 97), (63, 157, 167), (169, 242, 74), (188, 161, 140), (103, 95, 83), (133, 219, 227), (58, 42, 50), (48, 74, 64), (53, 48, 43), (55, 62, 76), (233, 171, 164), (37, 76, 84), (116, 38, 70), (185, 187, 208), (129, 153, 69)]



dot = Turtle()
dot.penup()
dot.hideturtle()

dot.setheading(220)
dot.forward(300)
dot.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    dot.dot(30, random.choice(color_list))
    dot.forward(50)
    
    if dot_count %10 == 0:
        dot.setheading(90)
        dot.forward(50)
        dot.setheading(180)
        dot.forward(500)
        dot.setheading(0)
        
    



screen = Screen()
screen.exitonclick()