import turtle
import random
import time
text="Visigoth king roderic first made a pioneer attack,\n retreated and attacked with all his might,\
but his commanders were betrayed and the central force was \n surrounded by the Arabs, namely the Umayyads.\
In this battle,\n the Umayyads were 12,000 while the \n Visigoths were 35,000."
te="decisive Umayyad victory \n 711 battle of Guadalete (Iberian peninsula)"
t=turtle.Turtle()
turtle.bgcolor("sandybrown")
t.speed(100)
def umayyed():
    t.begin_fill()
    t.color("green")
    t.circle(10)
    t.end_fill()
def vizigot():
    t.begin_fill()
    t.color("red")
    t.circle(10)
    t.end_fill()
for i in range(6):
    x=random.randint(-500,-300)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
for i in range(17):
    a=random.randint(300,500)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
time.sleep(3)
t.clear()
for i in range(6):
    x=random.randint(-500,-300)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
for i in range(10):
    a=random.randint(300,500)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
for i in range(7):
    a=random.randint(-500,-300)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
time.sleep(3)
t.clear()
for i in range(6):
    x=random.randint(-500,-300)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
for i in range(17):
    a=random.randint(300,500)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
time.sleep(3)
t.clear()
for i in range(6):
    x=random.randint(-200,-100)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
for i in range(6):
    a=random.randint(-200,-100)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
for i in range(10):
    a=random.randint(300,500)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
time.sleep(3)
t.clear()
for i in range(6):
    x=random.randint(-200,-100)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
for i in range(6):
    a=random.randint(-200,-100)
    b=random.randint(-200,200)
    t.up(),t.goto(a,b)
    t.down()
    vizigot()
time.sleep(3)
t.clear()
for i in range(6):
    x=random.randint(-200,-100)
    y=random.randint(-200,200)
    t.up(),t.goto(x,y)
    t.down()
    umayyed()
time.sleep(3)
t.clear()
t.up(),t.goto(-100,50)
t.down()
t.color("black")
t.write(text, align="left", font=("Arial", 10, "bold"))
time.sleep(9)
t.clear()
t.color("red")
turtle.bgcolor("grey")
t.write(te, align="left", font=("Arial", 20, "bold"))
turtle.done()
###Endülüsün Fethi###
