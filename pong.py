import turtle
from playsound import playsound
import pygame
from pygame import mixer
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor(0.2,0.6,0.2)
screen.setup(width=800, height=600)

mixer.init()
# mixer.music.load(r"F:\python\2.wav")
# mixer.music.set_volume(0.04)
# mixer.music.play(-1)
# playsound(,False)
screen.tracer(0)

#socre
score_a=0
score_b=0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")  
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("navy blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 \t\t Player B: 0", align="center",font=("courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#keyboard binding
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "i")
screen.onkeypress(paddle_b_down, "j")

#main game loop
while True:
    screen.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        # miss = mixer.Sound(r'F:\python\4.mp3')
        # miss.set_volume(0.08)
        # miss.play()
        score_a += 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {}".format(score_a,score_b), align="center",font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        # miss = mixer.Sound(r'F:\python\4.mp3')
        # miss.set_volume(0.08)
        # miss.play()
        score_b += 1
        pen.clear()
        pen.write("Player A: {} \t\t Player B: {}".format(score_a,score_b), align="center",font=("courier", 24, "normal"))

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1