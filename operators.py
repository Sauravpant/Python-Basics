#Arithmetic operators:

a=2
b=3
print(a+b) #Addition
print(a/b)  #Division
print(a//b) #Floor value
print(a-b) #subtraction
print(a*b) #Multiplication
print(a**b) #Exponential


#Conditional Operators:

a=True
b=False
c=5
d=6
print(a and b)
print(a or b)
print(not a)
print(not b)
print(c>d)
print(d>c)

#Bitwise operator
print (1 & 1) #AND operation of each bit
print(5 | 6)   #OR operation of each bit
print(~5)
print(5^8)  #XOR operator
print(c<<2) #Shift left
print(c>>2)  #Shift right
print(d<<2)

#Comparison operator
print(5>6) #greater than
print(5<6) #samller than
print(5==5)  #equals to
print(5<=6)  #less than or equals to
print(5>=6)   #gretaer than or equlas to
print(5!=6)  #not equals to


#Assisnment operator

a=3 
b=4
a=b  
a+=b  #equivalent to a=a+b  
a-=b  #equivalent to a=a-b
a/=b #equivalent to a=a/b
a%=b #equivalent to a=a%b
a*=b #equivalent to a=a*


#Some special operators

fruits=["apple","banana"]
fruit=fruits
print(fruits is fruit) # Returns true if both are equivalent
print("apple" is fruits) 
print("mango" is not  fruits) #Returns true if not found
print("mango" in fruits)  #Returns true if  found
