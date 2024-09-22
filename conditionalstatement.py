# #Conditional statements
# # if
# # elif
# # else

# a=int(input("enter the value of a"))
# b=int(input("Entre the value of b"))
# if a>b:
#     print("a is greter than b")
# else:
#     print("b is greater than a")

# # elif
# marks=85
# if marks>90:
#     print("Grade obtained is A")
# elif marks>80 and marks<90:
#     print("Grade is A-")
# else:
#     print("Fail")


# age=19
# if age<10:
#     print("Child")
# elif age>10 and age<20:
#     print("Teen")
# elif age>30 or age<40:
#      print("Young")

# ip1,op,ip2=input("Enter the expression").split()
# ip1=int(ip1)
# ip2=int(ip2)
# if op=="+":
#     print("The result is",ip1+ip2)
# elif op=="-":
#     print("The result is",ip1-ip2)
# elif op=="*":
#     print("The result is",ip1*ip2)
# elif op=="/":
#     print("The result is",ip1/ip2)
# else:
#     print("Enter the operator aming +,-,*,/")




#Exercise
#1. To check whether number is even or odd

var=int(input("Enter any number:"))
if var%2==0:
    print("The number is even")

else:
    print("The number is odd")

#2. Assigning grade

mark=int(input("Enter the grade of student:"))
if mark>=90 and mark<=100:
    print("A")
elif mark>=80 and mark<=89:
    print("B")
elif mark>=70 and mark<=79:
    print("C")
elif mark>=60 and mark<=69:
    print("D")
elif mark>=0 and mark<=59:
    print("F")
else:
    print("Invalid mark. Enter valid mark")

#3. Leap year: Year divisible by 4
year=int(input("Enter the year"))
if year%4==0:
    print("The year is leap year")
else:
    print("The year is not leap year")



#4.Largest among 3 numbers

num1,num2,num3=input("Enter any 3 numbers").split()
num1=int(num1)
num2=int(num2)
num3=int(num3)
if num1>num2 and num1>num3:
    print(num1," is greatest")
elif num2>num1 and num2>num3:
    print(num2,"is greatest")
else:
    print(num3,"is greatest")

#5.Quadratic equation solver

a,b,c=input("Enter the value of a,b and c").split()
a=int(a)
b=int(b)
c=int(c)
discriminant=b*b-4*a*c
if discriminant>0:
    print("The roots are real")
    root1=(-b+discriminant**0.5)/(2*a)
    root2=(-b-discriminant**0.5)/(2*a)
    print("Root 1:",root1,"Root2:",root2)

elif discriminant==0:
    print("Roots are equal:")
    root=(-b)/(2*a)
    print(root)
else:
    print('Roots are imaginary')


