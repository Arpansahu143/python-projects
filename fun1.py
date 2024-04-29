import turtle


screen = turtle.Screen()
screen.bgcolor("white")
turtle = turtle.Turtle()
turtle.color("red")
turtle.pensize(3)
turtle.speed(2)


turtle.begin_fill()
turtle.left(50)
turtle.forward(133)
turtle.circle(50, 200)
turtle.right(140)
turtle.circle(50, 200)
turtle.forward(133)
turtle.end_fill()


turtle.hideturtle()
import turtle

def draw_letter(letter, size):
    turtle.write(letter, font=("Arial", 14, "normal"))
    turtle.forward(size)


screen = turtle.Screen()
screen.bgcolor("white")
turtle = turtle.Turtle()
turtle.color("black")
turtle.pensize(2)
turtle.speed(2)


turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

draw_letter("A", 30)
draw_letter("r", 20)
draw_letter("p", 20)
draw_letter("a", 20)
draw_letter("n", 20)


turtle.hideturtle()

