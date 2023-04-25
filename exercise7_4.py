class negative_number_error(Exception):
    print("the list contains the unwanted elements")

class positive_number_error(Exception):
    print("the list contains the unwanted elements")
    
class homogenous_list_error(Exception): 
    print("the list contains the unwanted elements") 


def create_positive_numbered_list(my_int_list1):
    my_int_list1=input("enter positive list elements").split(",")
    for i in range(len(my_int_list1)):
        my_int_list1[i]= int(my_int_list1[i])
        if my_int_list1[i]>=0:
            print(my_int_list1)
        else:
            raise negative_number_error
            
    
def create_negative_numbered_list(my_int_list2):
    my_int_list2=input("enter negative list elements").split(",")
    for i in range(len(my_int_list2)):
        my_int_list2[i]= int(my_int_list2[i])
        if my_int_list2[i]<0:
            print(my_int_list2)
        else:
            raise positive_number_error


def create_heterogenous_list(my_int_list3):
   # for cnt in range(input("enter negative list elements (type,element)")):
        ch = int(input("Please choose a datatype of the element to be added  \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n"))
        if ch == 1:
            my_int_list3.append(int(input("enter the integer elemnents: ")))
        elif ch == 2:
            my_int_list3.append(float(input("enter the float elemnts: ")))
        elif ch == 3:
            my_int_list3.append(input("enter the float elemnts: "))
        elif ch == 4:
            my_int_list3.append(tuple(input("enter the float elemnts: ").split(",")))
    
        for i in range(len(my_int_list3)):
            if type(my_int_list3[0]) != type(my_int_list3[i]):
                
                print(my_int_list3)
        else:
            raise homogenous_list_error
        


def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            # elif choice ==4:
            #     print("Lists created are as below \n ----------------------")
            #     print(f"1 : {my_int_list1}")
            #     print(f"2 : {my_int_list2}")
            #     print(f"3 : {my_het_list3}")
                
            #     while True:
            #         check =int(input("Which of the below list you would want to search from "))
                    
            #         if  check == 1:
            #             find_an_element(my_int_list1)
            #             break
            #         elif check == 2:
            #             find_an_element(my_int_list2)
            #             break
            #         elif check ==3:
            #             find_an_element(my_het_list3)    
            #             break
            #         else:
            #             print("Please choose something from the above")
            elif choice ==5:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
            
my_exception_store()   