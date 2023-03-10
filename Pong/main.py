import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("skyblue")
win.setup(width=800, height=600)
win.tracer(0)

# getting the score
score_a = 0
score_b = 0

# paddle a
pada = turtle.Turtle()
pada.speed(0)
pada.shape("square")
pada.shapesize(stretch_wid=6, stretch_len=1)
pada.color("black")
pada.penup()
pada.goto(-350, 0)

# paddle b
paba = turtle.Turtle()
paba.speed(0)
paba.shape("square")
paba.shapesize(stretch_wid=6, stretch_len=1)
paba.color("black")
paba.penup()
paba.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.color("tomato")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0    Player B: 0", align="center", font=("Arial", 20, "bold"))


# function
def pada_up():
    y = pada.ycor()
    y += 20
    pada.sety(y)


def pada_down():
    y = pada.ycor()
    y -= 20
    pada.sety(y)


def paba_up():
    y = paba.ycor()
    y += 20
    paba.sety(y)


def paba_down():
    y = paba.ycor()
    y -= 20
    paba.sety(y)


# restricting paddle movement
def paddles(self, d, dx):
    if d == 'left':
        self.x -= dx

    else:
        self.x += dx


# keyboard input
win.listen()
win.onkeypress(pada_up, "w")
win.onkeypress(pada_down, "s")
win.onkeypress(paba_up, "Up")
win.onkeypress(paba_down, "Down")

while True:
    win.update()
    # set ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # boundaries
    if ball.ycor() > 290:
        ball.sety(-290)
        ball.dy *= 1.00

    if ball.ycor() < -290:
        ball.sety(290)
        ball.dy *= 1.00

    if ball.xcor() > 340:
        ball.goto(0, 0)
        ball.dx *= -1.00
        score_a += 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Arial", 20, "bold"))

    if ball.xcor() < -340:
        ball.goto(0, 0)
        ball.dx *= -1.00
        score_b += 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Arial", 20, "bold"))

    if pada.ycor() > 300:
        pada.goto(-350, -300)

    if pada.ycor() < -300:
        pada.goto(-350, 300)

    if paba.ycor() > 300:
        paba.goto(350, -300)

    if paba.ycor() < -300:
        paba.goto(350, 300)

    # touch point with ball and paddle
    if (335 < ball.xcor() < 350) and (paba.ycor() + 100 > ball.ycor() > paba.ycor() - 100):
        ball.setx(335)
        ball.dx *= -1.00
        winsound.PlaySound('pongsound.wav', winsound.SND_ASYNC)

    if (-335 > ball.xcor() > -350) and (pada.ycor() + 100 > ball.ycor() > pada.ycor() - 100):
        ball.setx(-335)
        ball.dx *= -1.00
        winsound.PlaySound('pongsound.wav', winsound.SND_ASYNC)

# dev notes:
# ball to wrap on all 4 sides
# write a readme for each project
# make a github account
# write up long term project
