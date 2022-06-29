#Objective 2: challenges
#Circle properties challenge
#program asks the user to enter the diameter of a circle,Output the radius,Output the area,output the circumference and asks the user to enter the arc angle,then outputs the arc length
CircleDiameter = int(input("Enter the diameter of the circle "))
CircleRadius = CircleDiameter/2
CircleArea = 3.14*(CircleRadius*CircleRadius)
CircleCircumference = 3.14*CircleDiameter
print(CircleRadius,"Is the radius of your circle")
print(CircleArea,"Is the area of your circle")
print(CircleCircumference,"Is the circumference of your circle")
ArcAngle = int(input("Enter the arc angle of the circle "))
ArcLength = (CircleCircumference*ArcAngle)/360
print(ArcLength,"Is the length of the arc")
               
