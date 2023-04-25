

import definations as dt

num1=int(input("enter number1 :"))
num2=int(input("enter number2 :"))

print("addition is : ",dt.addition(num1,num2))
print("squared of number1 :",dt.sqr(num1))
print("exponential of num2 to num1 :",dt.exp(num1,num2))

str1=input("enter the string to convert to UPPER CASE :")
print(dt.up(str1))

sal=float(input("enter the current salary:"))
per=float(input("enter the increament percentage:"))
print("the raised salary",dt.sal(sal,per))

height=float(input("enter the height (cm):"))
l = dt.ht(height)
print("the height in feet :", l[0], "ft")
print("the height in inches is :", l[1], "in")

currency=int(input("enter the amount in $ :"))
print(f"the {currency} in rupees : " , dt.cur(currency))

src=input("enter the source:")
dst=input("enter the destination:")
f=int(input(f"enter the fare from {src} to {dst} :"))
d=int(input("enter the dicount to be applied:"))
print(f"the fare from {src} to {dst} is : " , dt.fre(f,d))
