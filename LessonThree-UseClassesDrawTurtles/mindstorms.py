#"actual thing that moves around to draw things"
import turtle

#code to draw a square
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.color("yellow")
    for x in range (4):
        brad.forward(100)
        brad.right(90)

#code to draw a circle
def draw_circle():
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)

#code to draw a triangle
def draw_triangle():
    abby = turtle.Turtle()
    abby.color("white")
    for x in range (3):
        abby.forward(100)
        abby.left(120)

    window.exitonclick()


#calling the three functions
draw_square()
draw_circle()
draw_triangle()
