import turtle
from pygame import mixer
from time import sleep
mixer.init()

#mixer.music.load("bounce.mp3")

win = turtle.Screen()
win.bgcolor("black")
win.title("Pong By @msans")
win.setup(width=800,height=600)
win.tracer(0) #stops window from updating itself
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.goto(-350,0)
paddle_a.color("green")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.goto(350,0)
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Scoring
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0 , 260)
pen.hideturtle()
pen.write("Player A: 0 Player B: 0", align="center", font=(("Courier" , 25 , "normal")) )
#Functions
def paddle_a_Up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_Down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_Up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_Down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard Bindings
win.listen()
win.onkeypress(paddle_a_Up,"w")
win.onkeypress(paddle_a_Down,"s")
win.onkeypress(paddle_b_Up,"Up")
win.onkeypress(paddle_b_Down,"Down")


#Main Game Loop
while True:
    win.update()

    #Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()


    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()

    
    if ball.xcor() > 390:
        ball.goto(0,0) 
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b) , align="center" , font=(("Courier" , 25, "normal")))
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()

    

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1   
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b) , align="center" , font=(("Courier" , 25, "normal")))
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()

#Paddle and ball Collisions
    if ball.xcor() > 330 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()

    if ball.xcor() < -330 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        mixer.music.play()
        sleep(0.06)
        mixer.music.stop()
