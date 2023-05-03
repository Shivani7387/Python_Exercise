# Dictionary Exercise
def dict_display_capitals(capitals):
    a = capitals.keys()
    print("no of elements in the given Dictionary :", len(a))
   

def dict_add_element(capitals):
    b=input("enter the key for the same value:")
    a=input("enter the next element to add in the dictionary:")
    capitals[b]=a
    print(capitals)
   
        
def dict_add_elements(capitals):
    a=input("enter the new values to add:").split(",")
    list(a)
    for i in range(len(a)):
        capitals.update({i:a[i]})
    print(capitals)
        

def dict_remove_element(capitals):
    capitals.pop(input("enter the key two delete the corresponding value: "))
    print(capitals)

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    capitals= {}
    for dict_elem in input('for ex:  India : New Delhi , USA : Washington DC, Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        temp_list = dict_elem.split(":")
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()
