import turtle

number1=5
print(number1)
number2=number1/2.0
print(number2)

n=0

list_badea=[3,7,5]
for i in list_badea :
	print(i)
	print(i*2)
	n+=i

print("This is the total : %.1f" %(n))

turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
turtle.circle(100)



turtle.mainloop()

