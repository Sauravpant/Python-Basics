#String and string manipulation
name="saurav pant"
print(name)
st=name.upper() #Converts all charcaters to uppercase
print(st)
st1=st.lower() #Converts all characters to lower
print(st1)

print(name[-1])
print(name[0]) #Prints character at 1 index
print(name[2])
print(name[5])
print(name[7])
print(name[:2]) #Prints charcter before index 2
print(name[2:]) #Prints charcter after index 2
print(name[3:8]) #Prints charcter in between index 3 and 8
for val in name:
    print(val)
words=name.split()  #Splits the string to seperate wods
print(words)
name2=" ".join(name) #Adds between 2 characters
print(name2)

