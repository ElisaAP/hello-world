
import  turtle

turtle.shape("turtle")
turtle.color("green")

i = 1

for i in range(3):
    turtle.forward(180)
    turtle.left(90)
    i = i + 1

turtle.forward(180)

turtle.exitonclick()
