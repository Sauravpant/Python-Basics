#Function in python
#Syntax:
# def functionName(parameters):
#     
#     Purpose: 
#     
    
#end def



def myFunction(): #Function defination
    print("Hello World")

myFunction() #Function call


#Function as parameters
def fun(name):
    print("Hello",name)

fun("saurav")


#Function to add 2numbers
def sum(a,b):
    print(a+b)

sum(2,3)

#Global and local scope

a=2  #Global variable
b=5
def add(x,y): #Local variable
    return x+y
var=add(a,b) 
print(var)
print(add(a,b))


#Function returning multiple values
def funct(a,b):
    sum=a+b
    diff=a-b
    return (sum,diff)

res1,res2=funct(4,3)
print(res1)
print(res2)

#Default paramters
def show(name="Keshav"):
    print("Name:",name)
show("Suarav")
show()
    
#Function returns none as return value by default

#Passing list
myList=["kathmandu","Lalitpur","Bhaktapur","Kanchanpur"]
def printList(city):
    for n in city:
        print(n)

printList(myList)
    

def nothing():
    pass
nothing()


#Function to calculate the slope
def slope(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    return m
print(slope(1,2,3,4))


#Lambda function(Anonymous function)
#Syntax:lambda arguments: expression
slope=lambda x1,y1,x2,y2:(y2-y1)/(x2-x1)
print(slope(1,2,3,4))


#To calculate the average of 2 numbers 
avg=lambda a,b: (a+b)/2
print("Average is",avg(10,20))


#Function to calculate the area of circle
rad=5
pi=3.14
def circle(radius):
    return (pi*(radius**2))
print("Area of circle is:",circle(10))


def sumOfNumber(num):
    sum=0
    while num!=0:
        sum=sum+num%10
        num//=10
    return sum

print(sumOfNumber(345))


#Recursive function to calculate the factorial of a number
def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)
print(factorial(5))

#To check whether the number is plaindrome

        


