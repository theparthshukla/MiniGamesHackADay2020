import turtle
import time
import random

delay = 0.1 #This literally prevents the snake game from self-destructing before it even starts

#setting up the window
gamescreen = turtle.Screen()
gamescreen.title("Snake")
gamescreen.bgcolor("black")
gamescreen.setup(width=1200, height=1200)
#prevents the screen from glitching
gamescreen.tracer(0) 

# Snake head
head = turtle.Turtle()
head.speed(0)
head.color("green")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop" #needs to be done to prevent a crash due to undefined direction

# initializes the score values
score = 0
highestscore = 0

# snake pellets
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

# score display
scoredisplay = turtle.Turtle()
scoredisplay.speed(0)
scoredisplay.shape("square")
scoredisplay.color("white")
scoredisplay.penup()
scoredisplay.hideturtle()
scoredisplay.goto(0, 350)
scoredisplay.write("Current Score: 0  High Score: 0", align="center", font=("Helvetica", 30, "normal"))

tail = []

# movement
def head_up():
    if head.direction != "down":
        head.direction = "up"

def head_down():
    if head.direction != "up":
        head.direction = "down"

def head_left():
    if head.direction != "right":
        head.direction = "left"

def head_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# game controls
gamescreen.listen()
gamescreen.onkeypress(head_up, "w")
gamescreen.onkeypress(head_down, "s")
gamescreen.onkeypress(head_left, "a")
gamescreen.onkeypress(head_right, "d")

#runner progtam
while True:
    gamescreen.update()

    #checks for a collision
    if head.xcor()>580 or head.xcor()<-580 or head.ycor()>580 or head.ycor()<-580:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #cuts the tail
        for segment in tail:
            segment.goto(1000, 1000)
        
        #resets the tail
        tail.clear()

        #resets delay
        delay = 0.1

        #resets score
        score = 0

        scoredisplay.clear()
        scoredisplay.write("Score: {}  High Score: {}".format(score, highestscore), align="center", font=("Helvetica", 30, "normal")) 


    #checks if it has touched the food
    if head.distance(food) < 20:
        #spawns food
        x = random.randint(-580, 580)
        y = random.randint(-580, 580)
        food.goto(x,y)

        #adds to tail
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        tail.append(new_segment)

        delay -= 0.001

        #score change
        score += 5

        if score > highestscore:
            highestscore = score
        
        scoredisplay.clear()
        scoredisplay.write("Score: {}  High Score: {}".format(score, highestscore), align="center", font=("Helvetica", 30, "normal")) 

    #moves the tail of the snake in a fashion where everything doesn't move all at once
    for index in range(len(tail)-1, 0, -1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x, y)

    #moves first part of tail to the head
    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x,y)

    move()    

    #checks if the snake eats itself
    for bead in tail:
        if bead.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            #removes the tail
            for segment in tail:
                segment.goto(1000, 1000)
        
            #clears tail
            tail.clear()

            #resets score
            score = 0

            #resets delay
            delay = 0.1
        
            # score update
            scoredisplay.clear()
            scoredisplay.write("Current Score: {}  High Score: {}".format(score, highestscore), align="center", font=("Helvetica", 30, "normal"))

    time.sleep(delay)

gamescreen.mainloop()