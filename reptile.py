import turtle

turtle.title("Wacky shapes")
t = turtle.Turtle()

turtle.bgcolor("red")

t.shape("arrow")

for i in range(4):
    t.right(90)
    t.forward(90)


t.goto(100,100)

t.circle(60)

t.fd(100)

t.begin_fill()
t.fd(100)
t.lt(120)
t.pensize(10)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

t.clear()

c = t.clone()
t.color("magenta")
c.color("cyan")
t.circle(100)

t.pensize(1)

c.circle(60)

n=10
while n <= 40:
    t.circle(n)
    n = n+5

t.reset()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while (True):
    for i in range(6):
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)


turtle.hideturtle()
turtle.mainloop()