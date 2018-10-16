#"actual thing that moves around to draw things"
import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.color("yellow")
    for x in range (4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    abby = turtle.Turtle()
    abby.color("white")
    for x in range (3):
        abby.forward(100)
        abby.left(120)

    window.exitonclick()



draw_square()
draw_circle()
draw_triangle()
