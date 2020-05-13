import turtle
import os


#setting up the main screen
gamescreen = turtle.Screen()
gamescreen.title("Pong")
gamescreen.bgcolor("black")
gamescreen.setup(width=1600, height=1200)
gamescreen.tracer(0)#prevents screen glitch

#ball creation
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# player 1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.shapesize(stretch_wid=6, stretch_len=2)
p1.penup()
p1.goto(-700, 0)

# player 2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.shapesize(stretch_wid=6, stretch_len=2)
p2.penup()
p2.goto(700, 0)

# Score
score_a = 0
score_b = 0

#paddle motion
def p1_up():
    y = p1.ycor()
    y += 20
    p1.sety(y)

def p1_down():
    y = p1.ycor()
    y -= 20
    p1.sety(y)

def p2_up():
    y = p2.ycor()
    y += 20
    p2.sety(y)

def p2_down():
    y = p2.ycor()
    y -= 20
    p2.sety(y)



#scoreidsplay
scoredisplay = turtle.Turtle()
scoredisplay.speed(0)
scoredisplay.color("white")
scoredisplay.penup()
scoredisplay.hideturtle()
scoredisplay.goto(0, 260)
scoredisplay.write("Player 1: 0  Player 2: 0", align="center", font=("Helvetica", 20, "normal"))

#controls
gamescreen.listen()
gamescreen.onkeypress(p1_up, "w")
gamescreen.onkeypress(p1_down, "s")
gamescreen.onkeypress(p2_up, "Up")
gamescreen.onkeypress(p2_down, "Down")

# runner program
while True:
    gamescreen.update()	

	#keeps the ball rolling
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #returning the ball
    if (ball.xcor() > 680 and ball.xcor() < 700) and (ball.ycor() < p2.ycor() + 40 and ball.ycor() > p2.ycor() -40):
        ball.setx(680)
        ball.dx *= -1

    if (ball.xcor() < -680 and ball.xcor() > -700) and (ball.ycor() < p1.ycor() + 40 and ball.ycor() > p1.ycor() -40):
        ball.setx(-680)
        ball.dx *= -1

	#ball border control
    if ball.ycor() > 480:
        ball.sety(480)
        ball.dy *= -1

    if ball.ycor() < -480:
        ball.sety(-480)
        ball.dy *= -1

    if ball.xcor() > 780:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        scoredisplay.clear()
        scoredisplay.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 20, "normal"))

    if ball.xcor() < -780:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        scoredisplay.clear()
        scoredisplay.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Helvetica", 20, "normal"))


    
