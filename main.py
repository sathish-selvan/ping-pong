import turtle

window = turtle.Screen()
window.title("ping pong")
window.bgcolor("black")
window.setup(width=800, height =600)
window.tracer(0)
#score
score_a = 0
score_b = 0
##pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center",font=("Courier",34,"normal"))
#batA
bat_A = turtle.Turtle()
bat_A.speed(0) 
bat_A.shape("square")
bat_A.color("white")
bat_A.shapesize(stretch_wid=5,stretch_len=1)
bat_A.penup()
bat_A.goto(-350,0)
#batB
bat_B = turtle.Turtle()
bat_B.speed(0) 
bat_B.shape("square")
bat_B.color("white")
bat_B.shapesize(stretch_wid=5,stretch_len=1)
bat_B.penup()
bat_B.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(0) 
ball.dx=0.2
ball.dy=0.2
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
#func
def bat_A_up():
    y = bat_A.ycor()
    y += 20
    bat_A.sety(y)
def bat_A_down():
    y = bat_A.ycor()
    y -= 20
    bat_A.sety(y)
def bat_B_up():
    y = bat_B.ycor()
    y += 20
    bat_B.sety(y)
def bat_B_down():
    y = bat_B.ycor()
    y -= 20
    bat_B.sety(y)
window.listen()
window.onkeypress(bat_A_up,"w")
window.onkeypress(bat_A_down,"s")
window.onkeypress(bat_B_up,"Up")
window.onkeypress(bat_B_down,"Down")

while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() - ball.dy)

    #boundary
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    
    if bat_A.ycor() >= 260:
        bat_A.sety(260)
    if bat_A.ycor() <= -260:
        bat_A.sety(-260)

    if bat_B.ycor() >= 260:
        bat_B.sety(260)
    if bat_B.ycor() <= -260:
        bat_B.sety(-260)

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(str(score_a),str(score_b)), align="center",font=("Courier",34,"normal"))
    
    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(str(score_a),str(score_b)), align="center",font=("Courier",34,"normal"))
    if ball.xcor() >= 340 and ball.xcor() <= 350 and ball.ycor()<= bat_B.ycor()+40 and ball.ycor() >= bat_B.ycor()-40 :
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor()<= bat_A.ycor()+40 and ball.ycor() >= bat_A.ycor()-40 :
        ball.setx(-340)
        ball.dx *= -1