import turtle

wn = turtle.Screen()
wn.bgcolor("purple")
wn.screensize(1000,1000)
a = turtle.Turtle()
a.pensize(2)
a.shape("classic")
a.speed(0)
a.color("orange")
b = turtle.Turtle()
b.pensize(2)
b.shape("classic")
b.speed(0)
b.color("silver")
c = turtle.Turtle()
c.pensize(2)
c.shape("classic")
c.speed(0)
c.color("yellow")
d = turtle.Turtle()
d.pensize(2)
d.shape("classic")
d.speed(0)
d.color("green")
e = turtle.Turtle()
e.pensize(2)
e.shape("classic")
e.speed(0)
e.color("blue")
f = turtle.Turtle()
f.color("red")
f.pensize(2)
f.shape("triangle")
f.speed(0)

def start(turtle,x,y):
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(x, y)
    turtle.showturtle()
    turtle.pendown()

f.hideturtle()
start(a,-72.5,7.5)
start(b,200,200)
start(c,-200,-200)
start(d,-200,200)
start(e,220,-220)
i = 1

while i < 120:
    a.fd(150)
    a.rt(170)
    b.fd(i*2.2)
    b.lt(135.234)
    b.lt(90.121)
    c.fd(50+i)
    c.rt(90.728)
    d.fd(i)
    d.rt(90.352)
    d.left(45.342)
    e.fd(i*2)
    e.rt(170)
    e.lt(85)
    i+=1

a.hideturtle()
b.hideturtle()
c.hideturtle()
d.hideturtle()
e.hideturtle()
f.penup()

for i in range(10):
    f.fd(100)
    f.stamp()
    f.bk(100)
    f.rt(45)
f.hideturtle()

wn.exitonclick()