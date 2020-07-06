import turtle
import time 
import random

delay =0.1 
#the Score
sc =0 
HightSc = 0
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
#The snake body
body=[]

#Score
score = turtle.Turtle()
score.speed(0) #Speed animation
score.shape('square')
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,210)
score.write("Score: 0 Highest score : 0",align="center",
font=("Arial",20,"normal"))

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y +20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y -20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x -20)
    
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x +20)

def up():
    #to prevent the snake from touching 
    #himself if he's going down and wants to go up
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

    #add the border
    if (head.xcor()>240 or head.xcor()<-240 or 
    head.ycor()>240 or head.ycor()<-240 ):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        # Hide the body (off the visual screen)
        for b in body :
            b.goto(800,800)
        body.clear()
        #reset score
        sc=0
        score.clear()
        score.write("Score:{} Highest score :{}".format(sc,HightSc) ,align="center",
font=("Arial",20,"normal"))



    # If the snake eats the food 
    if head.distance(food)<20 :
        #change the food place in a random place
        x= random.randint(-240,240)
        y= random.randint(-240,240)
        food.goto(x,y)
        # the snake gets bigger 
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('square')
        new_body.color("red")
        new_body.penup()
        body.append(new_body)
        # Increase Score
        sc+=1
        if sc > HightSc :
            HightSc=sc
        score.clear()
        score.write("Score:{} Highest score :{}".format(sc,HightSc) ,align="center",
font=("Arial",20,"normal"))
    #move the tail and so on 
    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    #Move if the snake is not just a head
    if len(body)>0:
        x= head.xcor()
        y= head.ycor()
        body[0].goto(x,y)


    move()
    #If the head touches his body
    for b in body :
        if b.distance(head)<20 :
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            # Hide the body (off the visual screen)
            for b in body :
                b.goto(800,800)
            body.clear()
            #reset score
            sc=0
            score.clear()
            score.write("Score:{} Highest score :{}".format(sc,HightSc) ,align="center",
    font=("Arial",20,"normal"))

    time.sleep(delay)

window.mainloop()
