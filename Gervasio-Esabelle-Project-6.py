#Esabelle Gervasio
#Project 6
#Traffic Light with functions

from graphics import *


#setting the window size and naming the window
win= GraphWin("Traffic light" , 500, 500)


#function that draws the box of the light
def draw_body(x, y, length, width):
    body = Rectangle(Point(x,y), Point(width, length))
    body.setOutline("black")
    body.setFill("white")
    body.draw(win)

#function that draws the lamp circles
def draw_lamp(color, x, y, radius):
    lamp = Circle(Point(x, y), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.draw(win)

#function that draws the traffic light
def draw_traffic_light(x, y):
    draw_body(20, 20, 170, 80)
    draw_lamp("red", 50,45, 20)
    draw_lamp("yellow", 50,95, 20)
    draw_lamp("green", 50,145, 20)
draw_traffic_light(20,20)
