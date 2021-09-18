# By @LaKhWaN
# Ping Pong Game.

import turtle

wn = turtle.Screen()
wn.title('Ping Pong @LaKhWaN')
wn.bgcolor('white')
wn.setup(width=800,height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Text
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

# Block A
block_a= turtle.Turtle()
block_a.speed(0)
block_a.shape('square')
block_a.color('black')
block_a.shapesize(stretch_wid=5,stretch_len=1)
block_a.penup()
block_a.goto(-350,0)


# Block B
block_b= turtle.Turtle()
block_b.speed(0)
block_b.shape('square')
block_b.color('black')
block_b.shapesize(stretch_wid=5,stretch_len=1)
block_b.penup()
block_b.goto(350,0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

# Functions
def block_a_up():
    y = block_a.ycor()
    y+=20
    block_a.sety(y)

def block_a_down():
    y = block_a.ycor()
    y-=20
    block_a.sety(y)

def block_b_up():
    y = block_b.ycor()
    y+=20
    block_b.sety(y)

def block_b_down():
    y = block_b.ycor()
    y-=20
    block_b.sety(y)
    
# Keyboard Binding
wn.listen()
wn.onkeypress(block_a_up,'w')
wn.onkeypress(block_a_down,'s')

wn.onkeypress(block_b_up,'Up')
wn.onkeypress(block_b_down,'Down')

# Game Loop
while True:
    wn.update()

    # Ball Movment
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1

    # Collision
    if ball.xcor()> 340 and (ball.ycor() < block_b.ycor()+40 and ball.ycor() > block_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
        
    if ball.xcor()< -340 and (ball.ycor() < block_a.ycor()+40 and ball.ycor() > block_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1 
