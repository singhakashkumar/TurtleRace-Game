from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=900)
user_bet = screen.textinput(title="Make your bet", prompt="Which colored turtle will win the race?")
rainbow = ["violet", "purple", "blue", "green", "black", "orange", "red"]
turtles = []


def get_turtle(color, ycor):
    temp = Turtle(shape="turtle")
    temp.color(color)
    temp.penup()
    temp.goto(-490, ycor)
    temp.pendown()
    return temp


for _ in range(7):
    turtles.append(get_turtle(rainbow[_], -300+(_*100)))

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 470:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                screen.textinput(title="You Won!", prompt="Would you like to race again?")
                print(f"You Won! The {winning_turtle} turtle is the winner!")
            else:
                screen.textinput(title="You Lost!", prompt="Would you like to race again?")
                print(f"You lost! The {winning_turtle} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()