import turtle as t_module
from turtle import Screen
import random 
import colorgram

tim = t_module.Turtle()
s = t_module.Screen()

color_list = [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203)]

random_color = random.choice(color_list)

s.colormode(255)

tim.color("white")
position = -80
tim.setpos(-80, position)

def draw_dot():
  random_color = random.choice(color_list)
  tim.color(random_color)
  tim.dot(10)
  tim.penup()
  tim.color(random_color)
  tim.forward(20)
  tim.color(random_color)

def draw_art():
  for _ in range(10):
    draw_dot()
  global position
  new_position = position + 20
  tim.goto(-80, new_position)
  position = new_position 

for _ in range(10):
  draw_art()

s.exitonclick()