#Input and output
print("Numer is",5)

var=input("Enter the value") 
print(var)


var1,var2=input("Enter your name").split() #split function assigns value to multiple variables
print("Name is: ",var1)

print("Second:",var2)
velocity=int(input("Enter the velocity"))
time=int(input("Enter the time in seconds"))
acc=velocity/time
print(acc)
