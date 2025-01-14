#Start
import turtle

t = turtle.Turtle()

t.goto(-50, 35)
t.speed(10000000000000000000000000000000000000000000000000000000000000000000000000000)
# colors change every 4th time
colors = ["red", "dark red", "black"]
for i in range (800000000000000):
    t.color(colors[i%3])
    t.forward(100 + i/2)
    t.left(180 + 3)

#End
turtle.exitonclick()