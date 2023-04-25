
# 1) Accept two numbers from the user and print 
# a) addition 
# b) first number squared 2 
# c) first number raised to number second number
#Solution ---

a= int(input("enter number1 :"))
b= int(input("enter number :"))
print(a ,b)
print("Addition :" , a+b)
print("Square of 1st no :", a**2)
print("first no raised to second no :", a**b)


#2) Accept String from user and output upper case of the input string 


str1 = input("enter first string :")
print("UPPER CASE :", str1.upper())


# 3) Define a variable named "raise_salary_percentage" and get the salary raise 
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
# print the incremented salary to the console


raised_salary_percentage = float(input("enter the raised salary percentage :"))
name="gaurav"
existing_salary=50000 
print("the incremented salary is : ", existing_salary + (existing_salary * raised_salary_percentage/100) )


#4) Get the height from the user in cms and display the user height back to console
#in foot/feet and inches 


height=float(input("enter the height in centimeters :"))
print("the height in feet : " , 0.0328 * height ,"ft")
print("the height in inches : " , 0.394 * height , "in")


# 5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees


d = int(input("enter the amount ($) : "))
print(" $",d, " = ", d*82 ,"INR" )


# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"

src=input("From :")
dst=input("To :")
fare=int(input("fare :"))
disc=float(input("discount :"))
print(f"fare from {src} to {dst} is {fare-(fare*disc/100)} INR with has a discount of {disc}%")
