# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 
# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )

color1={1: "red" , 2: "Blue" , 3: "Orange"}
num=int(input("enter what to display:"))
try: 
    if num in color1.keys():
        print(color1[num])
    else:
        raise TypeError("Sorry, no numbers found")

except TypeError:
    print("plese enter the value between 1 to 3")
    
# 2) Write a program that creates a list of 5 elements of your choice 
# Now take the index that the user want the data of and print the value at that 
# location 
# Exception handle the code to  terminate gracefully by printing 
# Value not found if the index doesnot exists 

list1 =input("enter the elements of list : ").split(",")
i=int(input("enter the index of the list to get the value:"))
try:
    print(list1[i])
except IndexError:
    print("the index should be between 0 to ",len(list1))


# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)


from datetime import datetime, timedelta
 

try:
    dob=input("enter the date of birth dd/mm/yyyy: ")
    d = datetime.strptime(dob, "%d/%m/%Y")  
    print(d)
    print(datetime.today())
    new_date = datetime.today() - d
    print(new_date.days)
    if new_date.days > 100001:
        raise print("Exception occured : you lived for so long , may be you will die soon:)")
except TypeError:
    print("Exception occured")
    

