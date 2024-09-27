#Object oriented programming in Python

#Sample class
class student:
    def __init__(self, name, roll): #Constructor :Initialzies the attributes of class
        self.name = name
        self.roll = roll
    def __str__(self):
        return (f"{self.name},{self.roll}")

s1=student("Saurav",25) #Object of class
print(s1.name)
print(s1.roll)
print(s1)


class Person:
     
    def __init__(self, name, age,roll): 
        self.name = name
        self.age = age
        self.roll=roll
    def printMe(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("Roll:",self.roll)
p=Person("saurav",18,25)
p.printMe()
p.roll=40 #Changing the value of attribute of class
p.printMe()
del p.roll #deletes the attribute of class



    




