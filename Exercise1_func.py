# 1) Accept two numbers from the user and print 
# a) addition 
# b) first number squared 2 
# c) first number raised to number second number
#Solution -
def q1a_addition(num1,num2):
    return num1+num2

def q1b_sqrd(num1):
    return num1**2

def q1c_expo(num1,num2):
    return num1**num2
num1,num2=int(input("enter num1:")),int(input("enter num2:"))
print("addition is:",q1a_addition(num1,num2))
print("square is:",q1b_sqrd(num1))
print("exponential is:",q1c_expo(num1,num2))

#2) Accept String from user and output upper case of the input string 

def q2_upper(str1):
    return str1.upper()
str1=input("enter string:")
print("uppercase:",q2_upper(str1))

# 3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console

def q3_salary(sal,perct):
    return (sal+(sal*perct/100))
sal,perct=900,int(input("enter increment percent:"))
print("reviced salary of gaurav:",q3_salary(sal,perct))

#4) Get the height from the user in cms and display the user height back to console
#in foot/feet and inches 

def q4_height(height):
    return 0.0328*height,0.394*height
height=float(input("enter height in cm:"))
print("height in feet and inches :",q4_height(height))

# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees
def q5_dollorto_rupees(currency):
    return currency*82
currency=float(input("enter amount in $:"))
print ("amount in rupees:",q5_dollorto_rupees(currency))

# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
def q6_distance(src,dst,amt,dis):
   return print(f"fare from {src} to {dst} is {amt-(amt*dis/100)} INR with has a discount of {dis}")
src,dst,amt,dis=input("enter source:"),input("enter dist:"),int(input("enter amount:")),int(input("enter discount:"))
q6_distance(src,dst,amt,dis)
    

    