
# # Operators
# # SECTION 1: ARITHMETIC OPERATORS ( + - * / // % ** )
# # 30 Questions
# # Take two integers from user and print their sum.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# sum=a+b
# print(sum)

# # Take two integers and print subtraction result.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# sum=a-b
# print(sum)

# # Take two floats and print multiplication result.
# a=float(input("Enter the first num.:="))
# b=float(input("Enter the second num.:="))
# result=a*b
# print(result)

# # Take two numbers and print division result.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# result=a/b
# print(result)

# # Take two integers and print floor division result.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# result=a//b #its means not print decimal value
# print(result)

# # Take two integers and print remainder using %.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# result=a%b
# print(result)

# # Take a number and print its square using **.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# result=a**b
# print(result)

# # Take a number and print its cube.
# num=int(input("Enter the value"))
# cube=num**3
# print(cube)

# # Take two numbers and calculate average.
# a=int(input("Enter the first num.:="))
# b=int(input("Enter the second num.:="))
# avrange=(a+b)/2
# print(avrange)

# # Take length and width from user and calculate area.
# length=int(input("Enter the length"))
# width=int(input("Enter the width"))
# area=length*width
# print(area)

# # Take radius and calculate area of circle (3.14 * r * r).
# radius=int(input("Enter the radius"))
# area=3.14*radius*radius
# print("The area of circle is ",area)

# # Take principal, rate, time and calculate simple interest.
# pr=int(input("Enter the principal"))
# rate=int(input("Enter the rate"))
# time=int(input("Enter the time"))
# intrest=(pr*time*rate)/100
# print("The simple intrest is ",intrest)

# # Take total marks of 5 subjects and calculate percentage.
# print("Give me marks")
# m=float(input("Mathes:="))
# p=float(input("physics:="))
# c=float(input("chemistry:="))
# h=float(input("Hindi:="))
# e=float(input("English:="))
# per=(m+p+c+h+e)/5
# print("Percentage is ",per)

# # Take salary and eincrease it by 10%.
# salary=int(input("Enter the salary= "))
# incr=(salary*10)/100
# result=salary+incr
# print("After increase 10% ",result)

# # Take a number and divide it by 2 using /= operator.
# num=int(input("Enter the num:="))
# num/=2
# print(num)

# # Take a number and multiply it by 5 using *= operator.
# num=int(input("Enter the num:="))
# num*=5
# print(num)

# Take two numbers and swap them using arithmetic operators.
print("Before swaping")
a=int(input("a="))
b=int(input("b="))
a=a+b
b=a-b
a=a-b
print("After swaping")
print("a=",a)
print("b=",b)

# # Take a number and check if it is even using %.
# num=int(input("Enter the num:="))
# if(num%2==0):
#     print(num,"is Even")
# else:
#     print(num,"is not even")

# # Take a number and check if it is odd using %.
# num=int(input("Enter the num:="))
# if(num%2!=0):
#     print(num,"is odd")
# else:
#     print(num,"is not odd")

# # Take total seconds and convert into minutes (use // and %).
# second=int(input("Enter the total second="))
# minute=second//60
# sec=second%60
# print("On convert sec to min is ")
# print(minute,"minutes and ",sec,"seconds")

# # Take temperature in Celsius and convert to Fahrenheit.
# temp=int(input("Enter the temp in celsius="))
# convert=(9/5*temp)+32
# print("tempreature in fahrenheit is =",convert)

# # Take two numbers and print their power result.
# Base=float(input("Enter the num.="))
# power=float(input("Enter the power"))
# result=Base**power
# print("result is =",result)

# # Take price and discount %, calculate final price.
# price=float(input("Enter the price = "))
# dis=float(input("Enter the discount is ="))
# find=(price*dis)/100
# final=price-find
# print("Final=",final)

# # Take a 3-digit number and find sum of digits using % and //.
# a=int(input("Enter the 3-digit  num="))
# d1=a%10
# a//=10
# d2=a%10
# a//=10%10
# d3=a
# sum=d1+d2+d3
# print("The sum of digit is",sum)

# # Take two numbers and print remainder without using % (use formula).
# a=int(input("Enter the 1st num="))
# b=int(input("Enter the 2nd num="))
# diviser = a//b
# remainder=(a-(b*diviser))
# print("Remainder= ",remainder)

# # Take a number and print half of it.
# num=int(input("Enter the num:="))
# half=num/2
# print("half is:=",half)

# # Take base and height and calculate area of triangle.
# base=float(input("Enter the base of triangle:="))
# height=float(input("Enter the height of triangle:="))
# area=(base*height)/2
# print("Area of triangle is :=",area)

# # Take a number and print its square root using ** 0.5.
# num=int(input("Enter the num:="))
# Squareroot=num**0.5
# print("the square root of num is :=",Squareroot)

# # Take monthly salary and calculate yearly salary.
# salary=int(input("Enter the monthly salary :-"))
# yearly=salary*12
# print("Monthly salary is :=",yearly)

# # Take total bill and number of people, calculate per person share.
# bill=float(input("Enter the total bill:="))
# person=int(input("Enter the person:="))
# per=bill/person
# print("The bill of per person is :=",per)
