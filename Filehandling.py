#File handling 


#open()=creates and opens a file
#close()=closes a file
#write()=overwrites o a file
#append():adds data to existing file without a=overwriting
#read():reads data from a file


f=open("file1.txt","w")
f.write("Hello welcome to Python tutorial")
f.close()
f=open("file1.txt","r")
f1=f.read()
print(f1)
f=open("file1.txt","a")
f.write("Learning python........")
f.close()
f=open("file1.txt","r")
f1=f.read()
print(f1)




f=open("details.txt","w")
f.write("I am saurav pant.I am 18 years old. I enjoy learning new tools and technologies \n")
f.close()
f=open("details.txt","r")
f2=f.read()
print(f2)
f=open("details.txt","a")
f.write("I study at Everest engineering college")
f.close()
f=open("details.txt","r")
f2=f.read()
print(f2)
