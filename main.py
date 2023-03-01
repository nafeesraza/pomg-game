import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
pdl_r = Paddle(350)
pdl_l = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()
src = t.Screen()
src.setup(800, 600)
src.title("pong")
src.tracer(0)

src.listen()
src.onkeypress(pdl_r.up, "Up")
src.onkeypress(pdl_r.down, "Down")
src.onkeypress(pdl_l.up, "a")
src.onkeypress(pdl_l.down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    src.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(pdl_r) < 50 and ball.xcor() > 320 or ball.distance(pdl_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #ball missed right paddle
    if ball.xcor() > 380:
        #ball.goto(0,0)
        #ball.bounce_x()
        ball.reset_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        #ball.goto(0,0)
        #ball.bounce_x()
        ball.reset_position()
        scoreboard.r_point()





src.exitonclick()


