import turtle
import random

#to create a racetrack / window / screen
raceTrack = turtle.Screen()
raceTrack.bgcolor('black')

#create a object turtle
jack = turtle.Turtle()
jack.shape("turtle") #to create a shape for the object jack

martin = turtle.Turtle()
martin.shape("turtle")

drake = turtle.Turtle()
drake.shape("turtle")


#to select a color for jack
jack.penup()
jack.color('white')
jack.shapesize(2)
jack.speed(1)
jack.left(90)


martin.penup()
martin.color("grey")
martin.forward(50)
martin.left(90)
martin.shapesize(2)


drake.penup()
drake.color("red")
drake.backward(50)
drake.left(90)
drake.shapesize(2)

distanceJack = random.randint(50,100)
distanceMartin = random.randint(50,100) 
distanceDrake = random.randint(50,100) 
jack.forward( distanceJack )
martin.forward(distanceMartin)
drake.forward(distanceDrake)

print("Distance Jack covered :", distanceJack)
print("Distance Martin covered :", distanceMartin)
print("Distance Drake covered :", distanceDrake)

#to find the winner
if distanceJack > distanceDrake and distanceMartin < distanceJack:
    print("Jack is the winner")
elif distanceDrake > distanceJack and distanceDrake > distanceMartin:
    print("Drake is the winner")
##Take home check if there s a tie between the turtles
elif distanceDrake == distanceJack == distanceMartin:
    print("Its a tie!")
    

    
else:
    print("The winner is Martin")
    

#screen should wait until user manually closes it
raceTrack.exitonclick()
