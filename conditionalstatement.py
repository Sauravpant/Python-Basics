#Conditional statements
# if
# elif
# else

a=int(input("enter the value of a"))
b=int(input("Entre the value of b"))
if a>b:
    print("a is greter than b")
else:
    print("b is greater than a")

# elif
marks=85
if marks>90:
    print("Grade obtained is A")
elif marks>80 and marks<90:
    print("Grade is A-")
else:
    print("Fail")


age=19
if age<10:
    print("Child")
elif age>10 and age<20:
    print("Teen")
elif age>30 or age<40:
     print("Young")

ip1,op,ip2=input("Enter the expression").split()
ip1=int(ip1)
ip2=int(ip2)
if op=="+":
    print("The result is",ip1+ip2)
elif op=="-":
    print("The result is",ip1-ip2)
elif op=="*":
    print("The result is",ip1*ip2)
elif op=="/":
    print("The result is",ip1/ip2)
else:
    print("Enter the operator aming +,-,*,/")
