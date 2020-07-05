import turtle
import time 

delay =0.1 
#Set the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor('black')
window.setup(width=500,height=500)
window.tracer(0) 

#Snake head 

head = turtle.Turtle()
head.speed(0) #Speed animation
head.shape('square')
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food 
food = turtle.Turtle()
food.speed(0) #Speed animation
food.shape('circle')
food.color("green")
food.penup()
food.goto(0,100)
food.direction = "stop"

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y +20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y -20)

    if head.direction == 'left':
        x = head.ycor()
        head.setx(x -20)
    
    if head.direction == 'right':
        x = head.ycor()
        head.setx(x +20)

def up():
    if head.direction != "down":
        head.direction = "up"

def down():
    if head.direction != "up":
        head.direction = "down"

def left():
    if head.direction != "right":
        head.direction = "left"

def right():
    if head.direction != "left":
        head.direction = "right"

#synchronize keybord with the game 
window.listen()
window.onkeypress(up,"z")
window.onkeypress(right,"d")
window.onkeypress(left,"q")
window.onkeypress(down,"s")


#main game loop
while True:
    window.update()
    move()
    time.sleep(delay)

window.mainloop()