# #Loops in python
# #for
# #while 

# #for loop
# for i in range(50): #runs from 0 to n-1
#     print(i)

myList=["name","address","location","number"]

for val in myList:
    print(val)
    
num=len(myList)
print(num)
for f in range(0, num):
    print(myList[f])



# #Printing characters of a string

myName="SAURAV"
for val in  myName:
    print(val)



for i in range(0, 10):
    print(i)


# #while loop

num=0
while num<10:
    print(num)
    num=num+1

# #Nested loop

for i in range(10):
    for j in range(i+1):
        print("*",end=" ")
    print()



for i in range(0,4):
    for j in range(4-i):
        print(j,end=" ")
        j=j-1
    print()


# #continue statement:Skips the particular step if condition is satisfied

name="SPIDERMAN"
for n in name:
    if n=="R":
        continue
    print(n)

# #break statement: Terminates the whole loop
for n in name:
    if n=="R":
        break
    print(n)


# #pass
for n in name:
    pass
print(n)
    

# #Program to print multiplication of any number
num=int(input("Enter any number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    print()

# #Count the bumber of digits in a number
num=int(input("Enter any number"))
digit=0
while num!=0:
    num=num//10
    digit=digit+1


print("No of digits is",digit)


# #Count the number of characters in a string
name=input("Enter any string")
count=0
for n in name:
    count=count+1
    pass

print(count)
   



#Factorial of number
num=int(input("Enter any number"))
fact=1
for i in range(1,num+1):
    fact=fact*i

print("The factorial is ",fact)

#Reverse a number
num=int(input("Enter any number"))
rem=0
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num//=10

print("The reverse is",rev)
#Fibonacci series



