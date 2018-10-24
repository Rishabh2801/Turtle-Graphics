import turtle
x=0
turtle.speed(0)
turtle.bgcolor('black')
while x<500:
   if x%2==0:
         turtle.pencolor('red')
   elif x%3==0:
         turtle.pencolor('blue')
   else:
         turtle.pencolor('green')
   turtle.forward(x)
   turtle.left(90.91)
   x=x+1
