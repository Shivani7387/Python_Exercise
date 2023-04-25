# ------------------
# # ***********************************************************
# # Problem 1 
# # ***********************************************************
#  Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game
#import definations

def game():
    num = int(input("Please enter the number"))
    if (num%2==0):
        if(num%3==0):
            print("fizzbizz")
        elif(num%3==0):
            print("buzz")
choice='Y'
while(choice=="y" or choice=="Y"):
    game()
    choice = input("do yo want to continue,pree N/Y")
   

# # ***********************************************************
# # Problem 2
# # ***********************************************************

# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation

def mycalc(num1,num2,op):
    
    if(op == "add"):
        print(f"the addition of {num1} and {num2} is", definations.addition(num1,num2))
    elif(op == "Sqr"):
        print(f"the square of {num1} is", definations.sqr(num1))
    elif(op == "exp"):
        print(f"the exponential of {num1} to {num2} is",definations.exp(num1,num2))
    else:
        print("wrong choice")

num1 = int(input("enter the number1:"))
num2 = int(input("enter the number2:"))
op = input("enter the operation to perform (add,sqr,exp) :")
mycalc(num1,num2,op)    


