import turtle
sven = turtle.Turtle()
j = input("Input number you wished to be Doubled: ")

j = int(j)

b = 2

print(j * b)
mod = j % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("this is an ven number.")

t = input "please enter how big you want your square: ")
t = int (t)
sven.pu()
sven.goto(-200,200)
sven.pd()
for i in range(4):
    sven.forward(100*t)
    sven.right(90)
