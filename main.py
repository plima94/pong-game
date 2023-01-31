from turtle import Turtle, Screen
from paddle import Paddle

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)



paddle = Turtle()
screen.update()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)
paddle.penup()
paddle.setposition(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
