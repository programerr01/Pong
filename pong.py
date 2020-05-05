import turtle
import math
import os
win = turtle.Screen()
win.bgcolor("black")
win.title("pong game ")
win.setup(width=800 , height=600)
win.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(-1)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(-1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 , stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy =0.3

#Score
score_a = 0
score_b = 0
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {} , Player B:{}".format(score_a, score_b), align='center', font=("Courier",24,"normal"))
#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Keyboard binding

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

def collision():
    if math.sqrt((ball.xcor() -paddle_a.xcor())**2 + (ball.ycor() - paddle_a.ycor())**2) <  20:
            ball.setx(-310)
            ball.dx *=- 1
            os.system('afplay bounce.wap&')
    if math.sqrt((ball.xcor() - paddle_b.xcor())**2 + (ball.ycor() - paddle_b.ycor())**2) < 40:
        ball.setx(340)
        ball.dx *= -1
win.listen()
win.onkeypress(paddle_a_up , "w")
win.onkeypress(paddle_a_down, "s")

win.onkeypress(paddle_b_up , "Up")
win.onkeypress(paddle_b_down , "Down")
while True:
    collision()

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)


    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

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

    win.update()
