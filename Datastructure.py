#List in python(Allows repeatation)


myList=["Apple","Banana","Orange","Potato","Apple"]
for val in myList:
    print(val)
print(myList[2:])
print(myList[-1])

#Any data type can be inserted into the list data structure
myList2=["saurav",18,76.4,True]
print(type(myList2))
for val in myList2:
    print(myList2)

myList2.append("Kathmandu") #inserts element from last
print(myList2)
myList2.remove(True)
print(myList2)
myList2.pop() #removes element from last
print(myList2)
myList2.insert(1,"Lalitpur") #Inserts element at particular position
print(myList2)

city=["Kathmandu","Bhaktapur","Lalitpur"]
for c in city:
    print(c)

city.append("Kanchanpur")
city.insert(2,"Dhangadhi")
print(city)
city.remove("Dhangadhi")
city.pop()
print(city)

cities=city
print(cities)
city=city+cities #Appesnd the list
print(city)
city.clear() #Clears the entire list
print(city)

#A senence can be splitted to insert into a : list
strings="Hello vai kya halchal"
string2=strings.split()
print(string2)


val=[1,2,3,4,5,6,7]
print(val)
val.reverse() #Rvcerses the whole list from last
print(val)
add=sum(val)
print(add)
val.sort()  #Sorts the list
print(val)

#Printing the square of a list
myList=[1,2,3,4,5,6,7,8]
for val in myList:
    print(val*val)

for i in range(len(myList)):
    myList[i]=myList[i]**2

print(myList)

#Removing duplicates from a : list
list1=["Apple","Banana","Mango","Apple"]
list2=[]
for val in range(len(list1)):
    if list1[val] not in list2:
        list2.append(list1[val])
print(list2)
    




#Tuples
name=("saurav","pant","haha","haha")
print(type(name))
print(name)



myTuple=("saurav",19,85.1,2+3j,True)
print(myTuple)
print(type(myTuple))
print(myTuple[2])
print(myTuple[:2])
print(myTuple[2:])
print(myTuple[1:2])


var1,var2,var3,var4,var5=myTuple  #Tuples value can be copied into the variables
print(var1)
print(var2)
print(var3)

tup=("saurav") #single value cant be a tuple
print(type(tup))


#Set 
fruits={"Apple","Banana","Orange"}
print(fruits)
print(len(fruits))
print(type(fruits))
for val in fruits:
   print(val)
fruits.add("Litchi")
fruits.pop()
print(fruits)

set1={"a","b","c","d","e"}
set2={"a","e","i","o","u"}
set3=set1.union(set2)
print(set3)
set3=set1.difference(set2)
print(set3)
set3=set1.symmetric_difference(set2)
print(set3)\



#Dictionary in python(Key and value)

dis={
    "name":"saurav",
    "address":"lalitpur",
    "bool":True,
    "age":18
}
print(dis)
inList=dis.keys()
print(inList)
inList=dis.values()
print(inList)
dis["address"]="kanchanpur"
print(dis)


#Creating a dictionary and performing various operations
dict={
    "Name":"saurav",
    "Age":18,
    "Major subject":"Web development",
    "Gpa":3.4
}

print(dict)
list1=dict.keys()
list2=dict.values()

print(dict["Major subject"])

dict["Gpa"]=3.9
print(dict)
dict["Graduation year"]=2027
print(dict)
del dict["Age"]
print(dict)
for key in dict:
    print("key:",key,"Value:",dict[key])


for key in dict:
    if key=="Age":
        print("Age is found")
    if key=="Gpa":
        print("Gpa is found")


dict.clear()
print(dict)
