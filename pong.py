""" importing useful
    modules
"""

import turtle
import math
import os
#Setup the screen variable where all the magic is going to happen
win = turtle.Screen()
#Setting up the bgcolor ,title , and size of the window
win.bgcolor("black")
win.title("pong game ")
win.setup(width=800 , height=600)
win.tracer(0)

#Paddle A of the left side which is a turtle object
paddle_a = turtle.Turtle()
paddle_a.speed(-1)
paddle_a.shape("square")
paddle_a.color("white")
#how much to stretch
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.penup()
#position
paddle_a.goto(-350,0)

#Paddle B of the right side
paddle_b = turtle.Turtle()
paddle_b.speed(-1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 , stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball object which is going to move
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy =0.3

#Score of the players
score_a = 0
score_b = 0
#object to write on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} , Player B:{}".format(score_a, score_b), align='center', font=("Courier",24,"normal"))
#Function for controlling up and down of the left side using w ,s
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Right Side

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)
#checking for the collision
def collision():
    if math.sqrt((ball.xcor() -paddle_a.xcor())**2 + (ball.ycor() - paddle_a.ycor())**2) <  40:
            ball.setx(-310)
            ball.dx *=- 1
            os.system('aplay sound.wap&')
    if math.sqrt((ball.xcor() - paddle_b.xcor())**2 + (ball.ycor() - paddle_b.ycor())**2) < 70:
        ball.setx(310)
        os.system('aplay sound.wap&')
        ball.dx *= -1
#listening for the keyboard event
win.listen()
#binding the key with the Function
win.onkeypress(paddle_a_up , "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up , "Up")
win.onkeypress(paddle_b_down , "Down")
#infinite loop for keep the game running
while True:
    #checking for the collision
    collision()
    #updating the coordinates of the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #checking if ball has reached end and then change the direction
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1
    #if the ball hits corner then the opposite player got 1 point
    if ball.xcor() > 390:
        ball.goto(0,0)
        score_a += 1
        pen.clear()
        ball.dx *= -1
        pen.write("Player A : {} Player B: {}".format(score_a, score_b),align="center" , font=("Courier", 24, "normal"))


    if ball.xcor()  < -390:
        ball.goto(0,0)
        score_b +=1
        pen.clear()
        ball.dx *= -1
        pen.write("Player A: {} , Player B:{}".format(score_a, score_b), align='center', font=("Courier",24,"normal"))
    #updating the screen each time
    win.update()
