import turtle

#create oval
def draw_elliptical(draw):
    turtle.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        turtle.circle(50,90)    # Long curved part
        turtle.circle(50/2,90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    flower = turtle.Turtle()
    flower.color("black")
    flower.shape("arrow")
    flower.speed(20)

    for i in range(1,13):
        draw_elliptical(flower)
        flower.right(10)

    flower.left(30)
    flower.forward(200)

    window.exitonclick()


draw_art()
