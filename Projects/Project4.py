#Start
import turtle

t = turtle.Turtle()


t.speed(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
colors = ["red", "dark red", "pink", "black"]
for i in range (800000000000000):
    t.color(colors[i%4])
    t.forward(0.1 + i/14)
    t.left(45 + 1)

#End
turtle.exitonclick()