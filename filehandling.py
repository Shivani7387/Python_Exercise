# f1=open("file1.txt","w+")
# with open("file1.txt","r+") as fo:
#     print(f1.read())    
#     f1.write("I was created with default test new \nhow you doing \ni am fine \nwhat is your name \n")

# # except FileNotFoundError:
    
# f1 = open("file1.txt","r+")
# #f1.read()    
f1=open("file1.txt","r+")
list1=f1.readlines()
f1.close()
f2=open("file1.txt","w+")
for i in list1:
    f2.write("HPCSA" + i)
f2.seek(0)
print(f2.read())
        
                
    

                

