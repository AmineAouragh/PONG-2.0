# Import required library
import turtle

# Create Screen
sc = turtle.Screen()
sc.title("PONG 2.0")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

# Left Paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=4, stretch_len=1)
left_pad.penup()  # Picks up the turtle’s Pen
left_pad.goto(-400, 0)

# Right Paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=4, stretch_len=1)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
left_player = 0
right_player = 0

# Displays the score

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_Player : 0     Right_Player : 0",
             align="center", font=("Courier", 24, "normal"))


# Functions to move paddle vertically

def left_paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def left_paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def right_paddle_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def right_paddle_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(left_paddle_up, "e")
sc.onkeypress(left_paddle_down, "x")
sc.onkeypress(right_paddle_up, "Up")
sc.onkeypress(right_paddle_down, "Down")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking Borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:  # POINT FOR THE LEFT_PLAYER
        hit_ball.goto(0, 0)   # START AGAIN FROM THE CENTER
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_Player : {}    Right_Player : {}".format(
                    left_player, right_player), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:  # POINT FOR THE RIGHT_PLAYER
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_Player : {}    Right_Player : {}".format(
                     left_player, right_player), align="center", font=("Courier", 24, "normal"))

    # Paddle Ball Collision
    if (360 < hit_ball.xcor() < 370) and (
            right_pad.ycor() + 40 > hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (-360 > hit_ball.xcor() > -370) and (left_pad.ycor() + 40 > hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
