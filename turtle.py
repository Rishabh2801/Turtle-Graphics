import turtle  
x=0
turtle.speed(0)
turtle.bgcolor('black')
while x<500:     # This while loop is for stop making spirals so when x reaches 500 it stops making more spirals
   if x%2==0:    # If x is even or divisible by 2 then the color will be red
         turtle.pencolor('red')
   elif x%3==0:
         turtle.pencolor('blue')  # for making visually appealing i made another color which will be activated when it is divisible by 3
   else:
         turtle.pencolor('green')  # if above 2 condition is false then it takes green color so with three colors it looks fantastic
   turtle.forward(x)
   x=x+1
   turtle.left(90.91)

