#Exception handling in python can be performed using:
# try
# except
# else
# finally
a=2
b='c'
try:
    result=a/b
except ZeroDivisionError:  
    print("Error caught : Division by zero")
except TypeError:
    print("Both number must be of same data type ")
else:
    print("The answer is ",result)
finally:
    print("Block executed")


#Type error
a=input("Enter any number")
b=input("Enter any number")
try:
    res=a*b
    print(res)
except TypeError:
    print("The number is not a valid integer")
else:
    print("The number is",res)
finally:
    print("Block executed")