import time
import turtle
import random
# window screen set up
wn = turtle.Screen()
wn.title("Snake Game")
wn.setup(600, 600)
wn.tracer(0)
s = turtle.Screen()
s.bgcolor("turquoise")
delay = 0.1
# Snake body
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.color("orange")
head.goto(0, 0)
head.direction = "stop"
# food
food = turtle.Turtle()
food.speed(0)
food.color("black")
food.shape("circle")
food.penup()
food.goto(0, 150)
segments = []

#


def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


#
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# movement
def up_movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)


def down_movement():
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)


def left_movement():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)


def right_movement():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)


# main game loop
while True:
    wn.update()
    #my adjustments
    if head.xcor() > 290:
        head.goto(-290, 0)
    if head.xcor() < -290:
        head.goto(290, 0)
    if head.ycor() > 290:
        head.goto(0, -290)
    if head.ycor() < -290:
        head.goto(0, 290)
    #
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("arrow")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    up_movement()
    right_movement()
    left_movement()
    down_movement()
    time.sleep(delay)

wn.mainloop()
done()
