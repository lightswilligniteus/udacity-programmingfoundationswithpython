#"actual thing that moves around to draw things"
import turtle

#code to draw a square
def draw_square(some_turtle):
    for x in range (4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.color("yellow")
    for i in range(1, 37):
        draw_square(brad)
        brad.right(10)

#code to draw a circle
#def draw_circle():
#    angie = turtle.Turtle()
#    angie.color("blue")
#    angie.circle(100)

#code to draw a triangle
#def draw_triangle():
#    abby = turtle.Turtle()
#    abby.color("white")
#    for x in range (3):
#        abby.forward(100)
#        abby.left(120)

#    window.exitonclick()


#calling the three functions
draw_art()
